#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Hands-on Lab : Web Scraping**
# 

# Estimated time needed: **30 to 45** minutes
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# * Extract information from a given web site 
# * Write the scraped data into a csv file.
# 

# ## Extract information from the given web site
# You will extract the data from the below web site: <br> 
# 

# In[46]:


#this url contains the data you need to scrape
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"


# The data you need to scrape is the **name of the programming language** and **average annual salary**.<br> It is a good idea to open the url in your web broswer and study the contents of the web page before you start to scrape.
# 

# Import the required libraries
# 

# In[47]:


# Your code here
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Download the webpage at the url
# 

# In[48]:


#your code goes here
data = requests.get(url).text


# Create a soup object
# 

# In[49]:


#your code goes here
soup = BeautifulSoup(data, 'html.parser')


# Scrape the `Language name` and `annual average salary`.
# 

# In[55]:


#your code goes here
table = soup.find('table')
lang_list = list()
sal_list = list()
for row in table.find_all('tr'):
    cols = row.find_all('td')
    lang_name = cols[1].getText()
    lang_list.append(lang_name)
    salary = cols[3].getText()
    sal_list.append(salary)
    print("{}-->{}".format(lang_name, salary))
df = pd.DataFrame(lang_list, sal_list)
df.columns=df.iloc[0]
# df.rename(columns={'':'Average Annual Salary', '':'Language'})
df = df[1:]
df


# Save the scrapped data into a file named *popular-languages.csv*
# 

# In[58]:


# your code goes here
df.to_csv('popular-languages.csv')


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# |  Date (YYYY-MM-DD) |  Version | Changed By  |  Change Description |
# |---|---|---|---|
# | 2020-10-17  | 0.1  | Ramesh Sannareddy  |  Created initial version of the lab |
# 

#  Copyright &copy; 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork928-2022-01-01).
# 
