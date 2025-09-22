def get_mac_info(mac_address: str):
    from .mac_table import mac_table
    if ':' in mac_address:
        mac_str = mac_address.replace(':', '')
    elif '-' in mac_address:
        mac_str = mac_address.replace('-', '')
    else:
        mac_str = mac_address
    mac_str = mac_str.upper().strip()
    if len(mac_str) >= 6:
        return mac_table.get(mac_str[:6], "Unknown MAC address")
    else:
        print("Invalid MAC address format")
        return "Invalid MAC address format"