#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

def scan_ports(target, ports):
    print(f"🔍 Scanning {target}...")
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  
        result = s.connect_ex((target, port))  # 0 means open, else closed
        if result == 0:
            print(f"✅ Port {port} is OPEN")
        s.close()

# Example Usage
scan_ports("scanme.nmap.org", [22, 80, 443])


# In[ ]:




