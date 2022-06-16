from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

ip_address = open("list_ip.txt") #open a file list_ip.txt, before you start this code you must create file a containing the ip address
file_ip = ip_address.readlines()
password = getpass('Enter a password: ')

for host in file_ip:
    device = {
        "device_type" : "cisco_ios",
        "ip" : host,
        "username" : "cisco",
        "password" : password,
        "delay_factor_compat": True,
        "fast_cli": False,
    }
    print('\nSuccessfull Login to {0}'.format(host.rstrip("\n")))
    with ConnectHandler(**device) as net_connect:
        #net_connect.enable() #_This code used for send enable command
        print('Please Wait a Minutes !!')
        try:
            start_time = datetime.now()
            terlen0 = net_connect.send_command("ter len 0")
            showrun = net_connect.send_command("show run")
            showtech = net_connect.send_command("show tech-support", delay_factor=12)
        finally:
            end_time = datetime.now()
        print(f"Execute time: {end_time - start_time}\n")
        print('Program is Completed !!')
        print('Check the your txt file -> showrun-{0}.txt'.format(host.rstrip("\n")))
        print('Check the your txt file -> showtechsupport-{0}.txt'.format(host))
        #Save the command to txt file
        save_showrun = open("showrun-{0}.txt".format(host.rstrip("\n")),"w")
        save_showrun.write(showrun)
        save_showrun.close()
        save_techsupport = open("showtechsupport-{0}.txt".format(host.rstrip("\n")),"w")
        save_techsupport.write(showtech)
        save_techsupport.close()


        