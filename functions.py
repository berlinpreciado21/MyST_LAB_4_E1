#!/usr/bin/env python
# coding: utf-8

# In[270]:


import ccxt
from datetime import datetime
import pandas as pd
from sympy import Limit
import numpy as np


# ## Fetch Ohlcv

# In[281]:




def fetchData(exchange, symbol, timeframe, since="26-04-2022", limit=30):
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
    df["date"] = pd.to_datetime(df.Timestamp, unit="s")

    df = df[["date", "open", "high", "low", "close", "volume"]]

    df["open"] = pd.to_numeric(df["open"])
    df["high"] = pd.to_numeric(df["high"])
    df["low"] = pd.to_numeric(df["low"])
    df["close"] = pd.to_numeric(df["close"])
    df["volume"] = pd.to_numeric(df["volume"])

    return df


# In[282]:


print(fetchData("kraken",'BTC/USDT',"1m",30))


# ## Funciones-Fecthc Order Book para los distintos apis

# In[261]:


def fetch_order_book_kraken(symbol,limit):
    exchange = ccxt.kraken()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    
                       
    return dfk


# In[ ]:


def fetch_order_book_ftx(symbol,limit):
    exchange = ccxt.ftx()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dff = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dff['Vwap Ask'] =(np.cumsum(dff.Ask*dff.AVolume) / np.cumsum(dff.AVolume))
    dff['Vwap Bid'] =(np.cumsum(dff.Bid*dff.BVolume) / np.cumsum(dff.BVolume))
    dff["Total Volume"]=(dff.AVolume + dff.BVolume)
    dff["Midprice"]=((dff.Ask + dff.Bid)/2)
    dff['Vwap Ask'] =(np.cumsum(dff.Ask*df.AVolume) / np.cumsum(dff.AVolume))
    dff['Vwap Bid'] =(np.cumsum(dff.Bid*df.BVolume) / np.cumsum(dff.BVolume))
    
                       
    return dff


# In[262]:


def fetch_order_book_currencycom(symbol,limit):
    exchange = ccxt.currencycom()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfc = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfc['Vwap Ask'] =(np.cumsum(dfc.Ask*dfc.AVolume) / np.cumsum(dfc.AVolume))
    dfc['Vwap Bid'] =(np.cumsum(dfc.Bid*dfc.BVolume) / np.cumsum(dfc.BVolume))
    dfc["Total Volume"]=(dfc.AVolume + dfc.BVolume)
    dfc["Midprice"]=((dfc.Ask + dfc.Bid)/2)
    dfc['Vwap Ask'] =(np.cumsum(dfc.Ask*dfc.AVolume) / np.cumsum(dfc.AVolume))
    dfc['Vwap Bid'] =(np.cumsum(dfc.Bid*dfc.BVolume) / np.cumsum(dfc.BVolume))
    
                       
    return dfc


# In[ ]:


def fetch_order_book_coinmate(symbol,limit):
    exchange = ccxt.coinmate()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfcm = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfcm['Vwap Ask'] =(np.cumsum(dfcm.Ask*dfcm.AVolume) / np.cumsum(dfcm.AVolume))
    dfcm['Vwap Bid'] =(np.cumsum(dfcm.Bid*dfcm.BVolume) / np.cumsum(dfcm.BVolume))
    dfcm["Total Volume"]=(dfcm.AVolume + dfcm.BVolume)
    dfcm["Midprice"]=((dfcm.Ask + dfcm.Bid)/2)
    dfcm['Vwap Ask'] =(np.cumsum(dfcm.Ask*dfcm.AVolume) / np.cumsum(dfcm.AVolume))
    dfcm['Vwap Bid'] =(np.cumsum(dfcm.Bid*dfcm.BVolume) / np.cumsum(dfcm.BVolume))
    
                       
    return dfcm

