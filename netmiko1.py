#!/usr/bin/env python3

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.21',
    'username': 'admin',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print(output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (10,12):
    print("Creating VLAN " + str(n))
    config_commands = ['vlan ' + str(n), 'name Python_VLAN_' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print(output)