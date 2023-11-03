import re

def ipv4(input_str):
    parts = input_str.split('.')
    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False

    return True

def ipv6(input_str):
    parts = input_str.split(':')
    if len(parts) != 8:
        return False

    for part in parts:
        if not re.match(r'^[0-9a-zA-Z]{1,4}$', part):
            return False

    return True

def check_ip_addresses():
    N = int(input("Masukkan jumlah baris input: "))
    results = []

    for i in range(N):
        input_str = input()
        
        if ipv4(input_str):
            results.append("IPv4")
        elif ipv6(input_str):
            results.append("IPv6")
        else:
            results.append("Bukan IP Address")

    for result in results:
        print(result)

check_ip_addresses()