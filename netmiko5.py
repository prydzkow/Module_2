#!/usr/bin/env python3

from netmiko import ConnectHandler
from getpass import getpass

#-------------------------------------------------
#Getting username and password
username = input('Enter your SSH username: ')
password = getpass()

#-------------------------------------------------
#Configuring all switches with VLANs
with open('iosv_l2_config.cfg') as f:
    lines = f.read().splitlines()
#print(lines)

with open('all_switches.txt') as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print ('Connecting to device" ' + device)
    ip_address = device
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': ip_address, 
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_config_set(lines)
    print(output)

#-------------------------------------------------
#Configuring core switches - ports
with open('iosv_l2_core_config.cfg') as f:
    lines = f.read().splitlines()
#print(lines)

with open('core_switches.txt') as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print ('Connecting to device" ' + device)
    ip_address = device
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': ip_address, 
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_config_set(lines)
    print(output)

#-------------------------------------------------
#Configuring access switches - ports
with open('iosv_l2_access_config.cfg') as f:
    lines = f.read().splitlines()
#print(lines)

with open('access_switches.txt') as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print ('Connecting to device" ' + device)
    ip_address = device
    iosv_l2 = {
        'device_type': 'cisco_ios',
        'ip': ip_address, 
        'username': username,
        'password': password
    }
    net_connect = ConnectHandler(**iosv_l2)
    output = net_connect.send_config_set(lines)
    print(output)


