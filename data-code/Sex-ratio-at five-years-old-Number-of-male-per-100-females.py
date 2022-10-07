#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import plotly as py


# In[2]:


#!pip install numpy pandas plotly


# In[3]:


df = pd.read_csv("sex-ratio-at-five-years-old.csv")
print(df.head())


# In[4]:


print(df.tail())


# In[5]:


df.isnull().sum()


# In[10]:


# df_countries = df.groupby( ['Entity','Year']).sum()

# df_countries


# In[6]:


df['category'] = ''
def set_cat(row):
    if row['Sex_ratio_by_age_five_year_olds'] <= 90:
        return '90 and lower'
    if row['Sex_ratio_by_age_five_year_olds'] > 90 and row['Sex_ratio_by_age_five_year_olds'] <= 100:
        return '90-100'
    if row['Sex_ratio_by_age_five_year_olds'] > 100 and row['Sex_ratio_by_age_five_year_olds'] <= 105:
        return '100-105'
    if row['Sex_ratio_by_age_five_year_olds'] > 105 and row['Sex_ratio_by_age_five_year_olds'] <= 110:
        return '105-110'
    if row['Sex_ratio_by_age_five_year_olds'] > 110 and row['Sex_ratio_by_age_five_year_olds'] <= 115:
        return '110-115'
    if row['Sex_ratio_by_age_five_year_olds'] > 115 and row['Sex_ratio_by_age_five_year_olds'] < 120:
        return '115-120'
    if row['Sex_ratio_by_age_five_year_olds'] >= 120:
        return '120 and higher'

df_group = df.assign(category=df.apply(set_cat, axis=1))


# In[7]:


df_group


# In[10]:


#Plotly Components
import plotly.express as px
import json
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
catg = df_group['category'].unique()
dts = df_group['Year'].unique()
# with open("countries.geojson", "r") as geo:
#     mp = json.load(geo)
for template in ["none"]:
    fig = px.choropleth(df_group,
                    locations=df_group['Entity'],
                    color="category",

                    color_discrete_map={
                        '90 and lower': '#fffcfc',
                        '90-100' : '#ffdbdb',
                        '100-105' : '#ffbaba',
                        '105-110' : '#ff9e9e',
                        '110-115' : '#ff7373',
                        '115-120' : '#ff4d4d',
                        '120 and higher' : '#ff0d0d'},
                    category_orders={
                      'category' : [
                          '90 and lower',
                          '90-100',
                          '100-105',
                          '105-110',
                          '110-115',
                          '115-120',
                          '120 and higher'
                      ]
                    },
                    animation_frame="Year",
                    title='Sex Ratio by age five year olds',
                    labels={'Sex_ratio_by_age_five_year_olds':'Sex Ratio'},
                    hover_name='Entity',
                    locationmode='country names',
                    template=template
                    )


# In[15]:


fig.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)',
},
    showlegend=True,
    legend_title_text='Sex ratio',
    font={"size": 16, "color": "#808080", "family" : "calibri"},
    margin={"r":0,"t":40,"l":0,"b":0},
    legend=dict(orientation='v'),
    geo = dict(bgcolor='rgba(0,0,0,0)', lakecolor='#e0fffe')
)

# Adjust map geo options
fig.update_geos(showcountries=True, showcoastlines=False,
                showland=False, fitbounds="locations",
                subunitcolor='white',visible=False, resolution=50)
fig.update_traces(marker_line_width=0)
fig.show()


# In[16]:


import plotly.express as px
import plotly
plotly.offline.plot(fig, filename='Sex_ratio_by_age_five_year_olds.html')

