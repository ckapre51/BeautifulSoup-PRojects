#!/usr/bin/env python
# coding: utf-8

# # Desktop Notifier for COVID-19
# 

# In[80]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier


# In[81]:



header = {"User-Agent":"Chrome"}
req=Request("https://www.worldometers.info/coronavirus/country/india/",headers = header)
html = urlopen(req)


# In[82]:


html.status


# In[83]:


obj = bs(html)


# In[84]:


corona_cases = obj.find("div",{"class":"maincounter-number"}).span.text


# In[85]:


deaths = list(obj.find("div",{"class":"content-inner"}).div.next_siblings)[7].span.text


# ### Notifier
# 

# In[86]:


notifier = ToastNotifier()


# In[87]:


message = "\nTotal Cases : "+ corona_cases +"\nDeath : "+deaths


# In[88]:


message


# In[89]:


notifier.show_toast(title="COVID-19 Update", msg=message, duration=5, icon_path="bell.ico")


# In[ ]:




