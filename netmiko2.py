#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'admin',
    'password': 'cisco',
}

with open('iosv_l2_config.cfg') as f:
    lines = f.read().splitlines()
print(lines)

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_config_set(lines)
print(output)