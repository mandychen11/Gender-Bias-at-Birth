#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns; sns.set_theme()
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
import graphviz

import warnings
warnings.filterwarnings('ignore')

#!pip install --quiet jupyterlab==1.2 "ipywidgets==7.5"
#!pip install --quiet -U plotly
#!pip install --quiet pycountry_convert
from pycountry_convert import country_alpha2_to_country_name, country_name_to_country_alpha3
import os


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#!pip install pycountry-convert


# In[3]:


df = pd.read_csv('https://www.ctdatacollaborative.org/sites/default/files/The%20Global%20Dataset%2014%20Apr%202020.csv', dtype = 'object')
df.head()


# In[4]:


df.drop(df.columns[0], axis=1, inplace=True)


# In[5]:


df.replace('-99', np.nan, inplace=True)
df.replace(-99, np.nan, inplace=True)
df.replace('00', np.nan, inplace=True)


# In[6]:


df.describe(include='all')


# In[7]:


df['yearOfRegistration'].value_counts()


# In[8]:


#What types of sexual Exploitation were forced on the victims?
gh=df.typeOfSexConcatenated.unique()
df_sample=pd.DataFrame(gh)
udf_sample = df_sample.drop(0)
udf_sample


# In[9]:


#Which types of Victim Exploitation Practiced
explo=df.typeOfExploitConcatenated.unique()
df_sample=pd.DataFrame(explo)
udf_sample = df_sample.drop(1)
udf_sample


# In[10]:


#Victims Age and Gender Distribution.
#The folllowing values represent the sum victims age group classified by gender. We continue to observe that more females are trafficked over time and in this gender group, the most trafficked age range are 09--17 year olds, and 30--38 for males.

dFage = df.groupby(['gender', 'ageBroad']).size().reset_index()
dFage.rename(columns={0: 'Number of Trafficked Individuals'}, inplace=True)
print(dFage)

display('Age and Gender distribution of Trafficked persons')


# In[11]:


dFage = df.groupby(['gender', 'ageBroad']).size().reset_index()
dFage.rename(columns={0: 'Trafficked Persons'},
             inplace=True)  # Number of Trafficked Individuals

for template in ["none"]:
    fig = px.histogram(dFage, x='ageBroad', y='Trafficked Persons', color='gender',title='Victims Age and Gender Distribution', height=600, width=800,
                 template=template, labels={'ageBroad': 'Age Group(per group)', 'Trafficked Persons':'Number Of Trafficked Persons(per person)'},
             color_discrete_map={
        'Female': 'rgb(203, 67, 53)',
        'Male': 'rgb(52, 152, 219)'},
             category_orders={'ageBroad': ['0--8', '9--17', '18--20', '21--23', '24--26', '27--29', '30--38', '39--47', '48+']})
    

    fig.show()


# In[12]:


# ! pip install chart-studio


# In[13]:


import plotly.express as px
import plotly
plotly.offline.plot(fig, filename='Victims_Age_and_Gender_Distribution.html')


# In[14]:


from matplotlib import pyplot as plt
import numpy as np
from pylab import *
import seaborn as sns
import matplotlib
from matplotlib import style
import matplotlib.pyplot as plt
#Human trafficking development over time
sns.set_theme()
sns.set_style("whitegrid")
df_1 = sns.FacetGrid(df, col='gender', height=5, aspect=1.5)
df_1.map(sns.histplot, 'yearOfRegistration', kde = True, color='navy', edgecolor='black', linewidth=2)
df_1.set(xlabel='Year Of Registration(per year)', ylabel='Number Of Trafficked Persons(per person)')

df_1.savefig('trafficking_gender.png')

#The distribution of victims by gender in different years


# In[ ]:




