#%% 3.1
nat = "ip nat inside source list ACL interface FastEthernet0/1 overload"
print(nat)
nat = nat.replace('Fast', 'Gigabit')
print(nat)



#%% 3.2
MAC = 'AAAA:BBBB:CCCC'
print(MAC)
MAC = MAC.replace(':', '.')
print(MAC)


#%% 3.3
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
print(config)
array = config.strip().split()
vlans = array[-1].split()
print(vlans)


#%% 3.4
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
print(command1)
print(command2)
com1 = command1.split()
com2 = command2.split()
com1 = set(com1[-1].split(','))
com2 = set(com2[-1].split(','))
vlans = com1 & com2
vlans = list(vlans)
print(vlans)



#%% 3.5
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
print(vlans)
vlans = set(list(vlans))
print(vlans)


#%%3.6
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
print(ospf_route)
ospf_route = ospf_route.replace('O', 'OSPF')
result = ospf_route.split(' ')
print('Protocol:', result[0])
print('Prefix:', result[1])
print('AD/Metric:', result[2])
print('Next-Hop:', result[4])
print('Last update:', result[5])
print('Outbound Interface:', result[6])



#%% 3.7
mac = 'AAAA:BBBB:CCCC'
print(mac)
mac = mac.replace(':', '')
mac = bin(int(mac,16))
print(mac)


#%% 3.8
ip = '192.168.3.1'
ip = [int(i) for i in ip.split('.')]
print(ip)
a = [192,  168,  3,  1]
b = [bin(i)[2:] for i in a]
print (b)






#%% 3.9
num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']

print(num_list)
a = input('Введите значение, чтобы найти в списке ')
a = int(a)
num_list.reverse()
index=num_list.index(a)
print('index of last appearence{}'.format(len(num_list)-index))
print('*'*50)


print(word_list)
a = input('Введите значение, чтобы найти в списке ')
word_list.reverse()
index=word_list.index(a)
print('index of last appearence{}'.format(len(word_list)-index))
print('*'*50)