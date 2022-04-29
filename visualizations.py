#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px


# # Midprice graph

# In[2]:


def grafica_btc(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de BTC/USDT"))

    return fig.show()


# In[3]:


def grafica_ltc(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de LTC/USDT "))

    return fig.show()


# In[4]:


def grafica_eos(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del midprice de XRP/USDT "))

    return fig.show()


# # Ask

# In[5]:


def grafica_btca(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Ask",color="Exchange",title=("Grafica del ask de BTC/USDT"))

    return fig.show()


# In[6]:


def grafica_ltca(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Ask",color="Exchange",title=("Grafica del ask de LTC/USDT "))

    return fig.show()


# In[7]:


def grafica_eosa(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del ask de XRP/USDT "))

    return fig.show()


# # Bid

# In[8]:


def grafica_btcb(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Bid",color="Exchange",title=("Grafica del bid de BTC/USDT"))

    return fig.show()


# In[9]:


def grafica_ltcb(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Bid",color="Exchange",title=("Grafica del bid de LTC/USDT "))

    return fig.show()


# In[10]:


def grafica_eosb(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Midprice",color="Exchange",title=("Grafica del bid de XRP/USDT "))

    return fig.show()


# # Spread

# In[11]:


def grafica_btcs(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Spread",color="Exchange",title=("Grafica del spread de BTC/USDT"))

    return fig.show()


# In[12]:


def grafica_ltcs(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Spread",color="Exchange",title=("Grafica del spread de LTC/USDT "))

    return fig.show()


# In[13]:


def grafica_eoss(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Spread",color="Exchange",title=("Grafica del spread de XRP/USDT "))

    return fig.show()


# # Vwap Ask

# In[14]:


def grafica_btcv(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="BTC/USDT"]
    fig=px.line(df2, x="Index", y="Vwap Ask",color="Exchange",title=("Grafica del VWAP de BTC/USDT"))

    return fig.show()


# In[15]:


def grafica_ltcv(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="LTC/USDT"]
    fig=px.line(df2, x="Index", y="Vwap Ask",color="Exchange",title=("Grafica del VWAP de LTC/USDT "))

    return fig.show()


# In[16]:


def grafica_eosV(dataframe): 
    df2= dataframe[dataframe["Ticker"]=="XRP/USDT"]
    fig=px.line(df2, x="Index", y="Vwap Ask",color="Exchange",title=("Grafica del VWAP de XRP/USDT "))

    return fig.show()


# In[ ]:




