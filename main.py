from sch import IP, get_mac_info

if __name__ == '__main__':
    print(IP.from_ip('192.168.1.1'))
    print(get_mac_info('D4:5D:64:11:22:33'))
