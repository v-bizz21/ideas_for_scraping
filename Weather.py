#!/usr/bin/env python
# coding: utf-8
# In[1]:
from bs4 import BeautifulSoup
import requests
import pandas as pd
# In[5]:
website = 'https://weather.com/it-IT/tempo/oggi/l/ITXX0067:1:IT?Goto=Redirected'
# In[6]:
response = requests.get(website)
# In[7]:
response.status_code
# In[8]:
soup = BeautifulSoup(response.content, 'html.parser')
# In[9]:
soup
# In[28]:
title = soup.find_all(class_ = "WeatherDetailsListItem--icon--1En_X Icon--icon--2aW0V Icon--darkTheme--1PZ-8")
title
# In[31]:
measurements = [titles.get_text() for titles in title]
measurements
# In[32]:
value = soup.find_all(class_ = "WeatherDetailsListItem--wxData--kK35q")
value
# In[34]:
values = [val.get_text() for val in value]
values
# In[37]:
#creating a dataframe
city = 'Rome'
weather_info = pd.DataFrame({'City': city, 'Measure': measurements, 'Value': values})
# In[38]:
weather_info