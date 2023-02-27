import os
from datetime import datetime
import time

os.popen('netsh interface ip delete arpcache').read()
time.sleep(5)
scan_ip = os.popen('ipconfig').read()
scan_arp = os.popen('arp -a').read()

ip_scan_list = scan_ip.split('\n')
arp_scan_list = scan_arp.split()


ip_count = ip_scan_list.index('이더넷 어댑터 이더넷:')
gateway_count = ip_count + 6
del ip_scan_list[:gateway_count]
gateway_info = ip_scan_list[0]
gateway_ip = gateway_info[26:]

arp_count = arp_scan_list.index(gateway_ip)

arp_list = arp_scan_list[arp_count:]
gateway_mac = arp_list[1]

now = datetime.now()

f = open('d:\\options\\' + 'Arp_Options' + '-' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
        + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + ".txt", "w")
f.write(gateway_ip + ' ' + gateway_mac)
f = open('d:\\options\\' + 'Arp_Options' + '-' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
        + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + ".txt", "r")
lines = f.readlines()
for line in lines:
    line = line.split()
    print(line)
f.close

if arp_list[0] == line[0]:
    if arp_list[1] == line[1]:
        print('arp 공격이 탐지되지 않았습니다')
    else:
        print('arp 공격이 탐지되었습니다.')

#test case
# print(gateway_mac)
# print(gateway_ip)
# print('/')
print(arp_list)

# del scan_list[:8]
# count = scan_list.count("TCP")
# scan_list.count("SYN_RECEIVED")
# print(count)