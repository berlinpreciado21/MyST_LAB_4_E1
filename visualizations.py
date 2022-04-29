#!/usr/bin/env python
# coding: utf-8

# In[15]:


import plotly.express as px


# In[16]:


def grafica_btc(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de BTC/USDT"))

    return fig.show()


# In[17]:


def grafica_ltc(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de LTC/USDT "))

    return fig.show()


# In[18]:


def grafica_eos(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de XRP/USDT "))

    return fig.show()


# In[ ]:




