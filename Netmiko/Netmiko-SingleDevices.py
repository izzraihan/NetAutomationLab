from netmiko import ConnectHandler
from datetime import datetime
from getpass import getpass

#Define IP Address & Username for login to SSH
ip_address = input("Enter IP address: ")
username = input("Enter username: ")

device = {
    "device_type": "cisco_ios",
    "ip": ip_address,
    "username": username,
    "password": getpass('Enter Password: '),
    #"secret": getpass('Enter Enable Password: '), #_This code used for input enable password, if you have a user with high privillege level, you could disable this code
    "delay_factor_compat": True,
    "fast_cli": False,
    }
print('Successfull Login to {0}'.format(ip_address.rstrip("\n")))

#calling to dictionary -> "device"
with ConnectHandler(**device) as net_connect:
    #net_connect.enable() #_This code used for send enable command
    print('Please Wait a Minutes !!')
    try:
        start_time = datetime.now()
        output = net_connect.send_command("show tech-support", delay_factor=4)
    finally:
        end_time = datetime.now()
    print(f"Execute time: {end_time - start_time}")
    print('Program is Completed !!\n')
    print('Check the your txt file -> showtechsupport-{0}.txt'.format(ip_address.rstrip("\n")))

    #Save output command to txt file
    save_file = open("showtechsupport-{0}.txt".format(ip_address.rstrip("\n")),"w")
    save_file.write(output)
    save_file.close()
