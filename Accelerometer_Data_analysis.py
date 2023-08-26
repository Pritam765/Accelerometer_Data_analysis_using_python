#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv(r"C:\Users\ptt920460\Downloads\Data Science\Data_analysis\accdata.csv")
print(data.head())


# In[3]:


data.describe()


# In[4]:


data.info()


# In[5]:


data.shape


# In[6]:


fig = px.line(data,x="Date",y=["accel_x","accel_y","accel_z"],
            title="Acceleration data over time")

fig.show()


# In[7]:


data["hour"]=pd.to_datetime(data["Time"]).dt.hour
data["day_of_week"]=pd.to_datetime(data["Date"]).dt.day_name()
agg_data=data.pivot_table(index="hour",columns="day_of_week",
                          values=["accel_x","accel_y","accel_z"],
                         aggfunc="mean")


fig=go.Figure(go.Heatmap(x=agg_data.columns.levels[1],
                        y=agg_data.index,
                        z=agg_data.values,
                        xgap=1,ygap=1,
                        colorscale="RdBu",
                        colorbar=dict(title="Average Acceleration")))
              
fig.update_layout(title="By Average Acceleration by Hour of Day and Day of Week")
fig.show()              
              


# In[8]:


data["accel_mag"] = (data["accel_x"] **2 + data["accel_y"] ** 2 + data["accel_z"] **2) ** 0.5


# In[9]:


fig = px.scatter(data, x="Time",
                y= "accel_mag",
                title="Magnitude of acceleartion over time")
fig.show()


# In[11]:


fig = px.scatter_3d(data, x="accel_x",
                y= "accel_y",
                z="accel_z")
fig.show()


# In[12]:


fig = px.histogram(data,x="accel_mag",nbins=50,
                  title="Aceelearation magnitude histogram")

fig.show()


# In[ ]:




