import argparse
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


def parse_led_config(led_config: str):
    _config = {}
    for line in led_config.split('\n'):
        if '=' in line:
            _config[line.split('=')[0]] = line.split('=')[1]
    return _config

def get_led_config():
    global root_dir
    _led_config = {}
    _led_list = os.scandir(root_dir + 'sys/class/leds')
    for _led in _led_list:
        with open(_led.path + "/uevent") as f:
            _config = parse_led_config(f.read())
            _led_config[_config['OF_NAME']] = {
                'path': _led.path,
                'config': _config
            }
    return _led_config

def list_leds(_led_config):
    for led_name, led_info in _led_config.items():
        print(led_name)

def get_led_status(_led_config, led_name):
    if led_name in _led_config:
        with open(_led_config[led_name]['path'] + "/brightness") as f:
            status = 'On' if int(f.read()) else 'Off'
            print(status)
    else:
        print("LED not found")

def set_led_status(_led_config, led_name, status):
    if led_name in _led_config:
        with open(_led_config[led_name]['path'] + "/brightness", 'w') as f:
            if status == 'on':
                f.write('1')
            elif status == 'off':
                f.write('0')
            else:
                print("Invalid status")
    else:
        print("LED not found")

def parse_request_args(_path: str):
    _args = {}
    if '?' in _path:
        _query = _path.split('?')[1]
        for _arg in _query.split('&'):
            _key, _value = _arg.split('=')
            _args[_key] = _value
    return _args

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            data = '<!DOCTYPE html><html lang="en"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta charset="UTF-8"><title>Led Control Web</title></head><body><h1>Led Control Web</h1>'
            for led_name, led_info in led_config.items():
                with open(led_info['path'] + "/brightness") as f:
                    status = int(f.read())
                    data += f'<li><span>{led_name}</span> <mark>{"On" if status else "Off"}</mark> <a href="/set?led_name={led_name}&status={"off" if status else "on"}"><button>{"Off" if status else "On"}</button></a></li>'
            data += '</ul></body></html>'
            self.wfile.write(data.encode('utf-8'))
        elif self.path.startswith('/set'):
            self.send_response(302)
            args = parse_request_args(self.path)
            led_name = args['led_name']
            status = args['status']
            set_led_status(led_config, led_name, status)
            self.send_header('Content-type', 'text/html')
            self.send_header('Location', '/')
            self.end_headers()


def web_server(_host, _port):
    httpd = HTTPServer((_host, _port), Handler)
    httpd.serve_forever()

def main():
    global root_dir, led_config
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['list', 'get', 'set', 'web'])
    parser.add_argument('led_name', nargs='?')
    parser.add_argument('status', nargs='?', choices=['on', 'off'])
    parser.add_argument('--root', nargs='?', help='Root directory')
    parser.add_argument('--host', nargs='?', help='Web host IP address, default is 0.0.0.0')
    parser.add_argument('--port', nargs='?', help='Web port number, default is 8082')
    args = parser.parse_args()
    if 'root' in args:
        if args.root:
            root_dir = args.root
            if sys.platform.startswith('win32'):
                if len(root_dir) == 1:
                    root_dir += ':/'
                elif root_dir[-1] != '/':
                    root_dir += '/'
            else:
                if root_dir[-1] != '/':
                    root_dir += '/'
        else:
            root_dir = '/'

    led_config = get_led_config()
    if args.action == 'list':
        list_leds(led_config)
    elif args.action == 'get':
        get_led_status(led_config, args.led_name)
    elif args.action =='set':
        set_led_status(led_config, args.led_name, args.status)
    elif args.action == 'web':
        _host = '0.0.0.0'
        _port = 8082
        if 'host' in args:
            if args.host:
                _host = args.host
        if 'port' in args:
            if args.port:
                _port = int(args.port)
        web_server(_host, _port)
    else:
        print("Invalid action")

if __name__ == '__main__':
    led_config = {}
    root_dir = '/'
    main()