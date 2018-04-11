# pivotnbt

A simple python script to quickly scan the local subnet for hosts running multiple network interfaces that could potentailly be used
as pivot points during a penetraiton test. The script makes use of a number of features within NetBios that cause the target host to 
reply to queries for a hostnames given IP address with a list of all known interfaces and their  IP addresses.   

# Usage

python pivotnbt.py <IP Range>

Example: python pivotnbt.py 192.168.1.0/24

#
