list_ip = [ ]

import platform    
import subprocess  
import sys

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'     
    
    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]     
   
    return subprocess.call(command) == 0


def ip_to_int(my_ip):
           return int(my_ip.replace('.',''))


if __name__ == "__main__":

           min_ip = sys.argv[1]

           max_ip = sys.argv[2]

           for i in range(0,256):
               for j in range(0,256): 
                   for k in range(0,256):
                       for y in range(0,256):
                           list_ip.append(str(i)+'.'+str(j)+'.'+str(k)+'.'+str(y))
                           if min_ip < list_ip[-1] < max_ip:
                                      ping(list_ip[-1])
                                      print('ping OK')
