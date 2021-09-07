
# Port Scanner

A Port Scanner built using python3 which scans open ports on the target machine. You can change the port number in the for loop, by default it will scan first 100 ports on the machine and it will check for any service and return the output as the open port number along with service (if it was able to find). The script can accept multiple domains (seperated by comma) as well as can convert domain names to IP 


## Installation

Installation on Linux

```bash
  git clone https://github.com/toufique10/Port-Scanner
```
    
## Deployment

Run the Script against a single Target

```bash
  python3 google.com
```
Run the Script against multiple Targets

```bash
  python3 google.com,192.168.0.101,nmap.org,bing.com
```
  
## FAQ

#### Is the script as good as Nmap

No, this script is just for understanding how things might work in the background.

#### Will the script scan all the ports

No, you manually need to set the range in the for loop.

#### Is the script accurate

It depends on the value of sock.settimeout, by default it has been set to 0.5 seconds, the higher the value of sock.settimeout, the greater is the accuracy and vice versa.

  
