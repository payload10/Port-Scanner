import socket
from IPy import IP		


# Convert into IP
def check_ip(ipaddr):
	
	# This try block is for checking IP address.
	try:
		IP(ipaddr)
		return ipaddr
	
	# This except block is for converting Domain name into an IP address	
	except ValueError:
		return socket.gethostbyname(ipaddr)


# Get Banner
def get_banner(s):
	return s.recv(1024)

# Scan ports
def port_scan(ipaddress,port):
	try: 
		sock = socket.socket()			# Descriptor
		sock.settimeout(0.5)			# set time out .
		sock.connect((ipaddress,port))
		try:
			banner = get_banner(sock)
			print("\033[1;32m[+] Port " + str(port) + " is Open" + " : " + str(banner.decode().strip('\n')))
		except:
			print("\033[1;32m[+] Port " + str(port) + " is Open")
	
	except:
		pass


# Scan Target
def scan(target):
	converted_ip = check_ip(target)
	print('\n')
	print("\033[1;36m[+] Scanning Target " + '\033[1;31m' + str(target))
	for port in range(1,100):
		port_scan(converted_ip,port)


# Display in Yellow.
targets = input('\033[1;33mEnter Target (if multiple targets seperate by comma): ')		# IP or Domain

if ',' in targets:
	ipaddresses = []
	ipaddresses = targets.split(',')
	for target in ipaddresses:
		scan(target.strip(" "))
else:
	scan(targets)
		
		
		
		
		
		
		
		






