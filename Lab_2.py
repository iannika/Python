#%% 5.1
ip = input('Enter IP: ')
ip_1 = int(ip.split('.')[0])
if 1 <= ip_1 <= 127:
    print('unicast')
elif 128 <= ip_1 <= 191:
    print('unicast')
elif 192<= ip_1 <= 223:
    print('unicast')
elif 224 <= ip_1 <= 239:
    print('multicast')
elif ip == '255.255.255.255':
    print('local broadcast')
elif ip == '0.0.0.0':
    print('unassigned')
else:
     print('unused')


#%% 5.2
mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
mac_cisco = [i.replace(':', '.') for i in mac]
print(mac_cisco)




#%% 5.3

access_template = ['swinchport mode access', 'swinchport access vlan', 'spanning-tree portfast', 'spanning-tree bpdugusrd enable']
trunk_template = ['swinchport trunk encapsulation dot1q', 'swinchport mode trunk', 'swinchport trunk allowed vlan']
fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
'trunk':{'0/1':['add','10','20'],
'0/2':['only','11','30'],
'0/4':['del','17']} }

for intf, vlan in fast_int['access'].items():
    print('int FastEthernet' + intf)
for command in access_template:
    if command.endswith('access vlan'):
        print(' {} {}'.format(command, vlan))
    else: 
        print(' {}'.format(command))


for intf, vlan in fast_int['trunk'].items():
    print('int FastEthernet' + intf)
for command in trunk_template:
    if not command.endswith('vlan'):
        print(' ' * 7, command)
    else:
        if vlan[0] == 'add':
            print(' ' * 7, command, 'add', ','.join(vlan[1:]))
        elif vlan[0] == 'only':
            print(' ' * 7, command, 'remove', ','.join(vlan[1:]))
        elif vlan[0] == 'del':
            print(' ' * 7, command, ','.join(vlan[1:]))


