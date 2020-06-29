#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pprint
r = requests.get('https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences')
r.json()


# In[2]:


pprint.pprint(r.json())


# In[3]:


pprint.pprint(r.json()['free'])


# In[4]:


pprint.pprint(r.json()['free'][0])


# In[5]:


x = r.json()['free']
print(x)


# In[12]:


y = x
for i in y:
    print(i.values())


# In[8]:


y[0]


# In[9]:


y[1]


# In[10]:


y[2]


# In[27]:


for i in x:
    for conf in i.values():
        print(conf)

