#!/usr/bin/env python
# coding: utf-8

# In[330]:


import ccxt
from datetime import datetime
import pandas as pd
from sympy import Limit
import numpy as np
import time


# ## Fetch Ohlcv

# In[442]:




def fetchData(exchange, symbol, timeframe, since="26-04-2022", limit=100):
    exchange_list = [
        "kraken",
        'ftx',
        'currencycom',
        'coinmate' ]
    try:
        exchange = getattr(ccxt, exchange)()
    except AttributeError:
        print("-" * 36, " ERROR ", "-" * 35)
        print(
            'Exchange "{}" not found. Please check the exchange is supported.'.format(
                exchange
            )
        )
        print("Supported exchanges are:")
        print(exchange_list)
        print("-" * 80)
        quit()

    data = exchange.fetch_ohlcv(symbol, timeframe, since, limit)
    header = ["Timestamp", "open", "high", "low", "close", "volume"]
    df = pd.DataFrame(data, columns=header)

    df.Timestamp = (
        df.Timestamp / 1000
    ) 
    df["timestamp"] = pd.to_datetime(df.Timestamp, unit="s")

    df = df[["timestamp", "open", "high", "low", "close", "volume"]]

    df["open"] = pd.to_numeric(df["open"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["close"] = pd.to_numeric(df["close"])
    df["volume"] = pd.to_numeric(df["volume"])

    return df


# ## Funciones-Fecthc Order Book para los distintos apis

# In[444]:


def tim():
    t=time.localtime(time.time())
    return str(t[0])+"-"+str(t[1])+"-"+str(t[2])
tim()


# In[445]:


def fetch_order_book_bitso(symbol,limit):
    exchange = ccxt.bitso()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    
    
                       
    return dfk


# In[446]:


def fetch_order_book_ascendex(symbol,limit):
    exchange = ccxt.ascendex()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    
    
                       
    return dfk


# In[447]:


def fetch_order_book_bitbay(symbol,limit):
    exchange = ccxt.bitbay()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    
    
                       
    return dfk


# In[448]:


def fetch_order_book_bitbns(symbol,limit):
    exchange = ccxt.bitbns()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    
    
                       
    return dfk


# In[ ]:




