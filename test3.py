import time


global now_time


now_time = 'Arp_Options' + '-' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
+ '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second)

f2 = open('d:\\options\\' + now_time + ".txt", "w")
f2.write(gateway_ip + ' ' + gateway_mac)
f2.close