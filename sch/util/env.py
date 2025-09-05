import json as _json
import os


def json_to_env(json_file='env.json', env_file='.env'):
    with open(env_file, 'w', encoding='utf-8') as f:
        _data = _json.load(open(json_file, 'r', encoding='utf-8'))
        for _item in _data:
            _name = _item['name']
            _value = _item['value']
            f.write(f'{_name}={_value}\n')

def env_to_json(env_file='.env', json_file='env.json'):
    _data = open(env_file, 'r', encoding='utf=8').read()
    _list = []
    for _line in _data.split('\n'):
        if '=' in _line:
            _sep = _line.split('=')
            _name = _sep[0]
            _value = _sep[1]
            _list.append({
                'name': _name,
                'value': _value
            })
    _json.dump(_list, open(json_file, 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

def load_env(env_file='env.json'):
    _data = _json.load(open(env_file, 'r', encoding='utf-8'))
    for _item in _data:
        _name = _item['name']
        _value = _item['value']
        os.environ[_name] = _value