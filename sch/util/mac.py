def get_mac_info(mac_address: str):
    from .mac_table import mac_table
    mac_str = (
        mac_address
        .replace(":", "")
        .replace("-", "")
        .replace(".", "")
        .upper()
        .strip()
    )
    if len(mac_str) >= 6:
        return mac_table.get(mac_str[:6], "Unknown MAC address")
    else:
        print("Invalid MAC address format")
        return "Invalid MAC address format"
