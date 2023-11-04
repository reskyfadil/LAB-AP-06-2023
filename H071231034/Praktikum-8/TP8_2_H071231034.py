import re

def check_ip(ip_str):
    pola_ipv4 = r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.' \
                   r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.' \
                   r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.' \
                   r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
    
    pola_ipv6 = r'^(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}$'
    
    if re.match(pola_ipv4, ip_str):
        return "IPv4"
    elif re.match(pola_ipv6, ip_str):
        return "IPv6"
    else:
        return "Bukan keduanya"

ip = "192.168.1.1"
print(check_ip(ip))

ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
print(check_ip(ip))

ip = "bukan ip"
print(check_ip(ip))