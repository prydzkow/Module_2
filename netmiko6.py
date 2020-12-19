#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

#-------------------------------------------------
#Getting username and password
username = input('Enter your SSH username: ')
password = getpass()

#-------------------------------------------------
#Configuring Ports on Router
with open('iosv_config.cfg') as f:
    lines = f.read().splitlines()
#print(lines)

with open('routers.txt') as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print ('Connecting to device" ' + device)
    ip_address = device
    iosv = {
        'device_type': 'cisco_ios',
        'ip': ip_address, 
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**iosv)
    output = net_connect.send_config_set(lines)
    print(output)