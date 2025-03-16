#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

requests = {}  # Store request timestamps by IP
LIMIT = 5  # Max requests allowed
WINDOW = 5  # Time window in seconds

def detect_dos(ip):
    now = time.time()
    requests.setdefault(ip, []).append(now)
    requests[ip] = [t for t in requests[ip] if now - t <= WINDOW]  # Keep only recent requests

    if len(requests[ip]) > LIMIT:
        print(f"🚨 DoS detected from {ip}!")
        return True
    return False

# Simulating requests
for _ in range(7):  
    detect_dos("192.168.1.1")
    time.sleep(0.5)  # Simulating time between requests


# In[ ]:





# In[ ]:




