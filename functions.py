#!/usr/bin/env python
# coding: utf-8

# In[16]:


import ccxt
from datetime import datetime
import pandas as pd
from sympy import Limit
import numpy as np
import time


# ## Fetch Ohlcv

# In[17]:


def fetchData(exchange, symbol, timeframe, since="26-04-2022", limit=100):
    exchange_list = [
        'aax', 
        'ascendex', 
        'bequant', 
        'bibox',
        'bigone',
        'binance',
        'binancecoinm',
        'binanceus',
        'binanceusdm', 
        'bit2c', 
        'bitbank',
        'bitbay',
        'bitbns',
        'bitcoincom', 
        'bitfinex',
        'bitfinex2',
        'bitflyer', 
        'bitforex', 
        'bitget', 
        'bithumb', 
        'bitmart',
        'bitmex',
        'bitopro',
        'bitpanda', 
        'bitrue', 
        'bitso',
        'bitstamp', 
        'bitstamp1', 'bittrex', 'bitvavo', 'bkex', 'bl3p', 'blockchaincom', 'btcalpha', 'btcbox', 'btcmarkets', 'btctradeua', 'btcturk', 'buda', 'bw', 'bybit', 'bytetrade', 'cdax', 'cex', 'coinbase', 'coinbaseprime', 'coinbasepro', 'coincheck', 'coinex', 'coinfalcon', 'coinmate', 'coinone', 'coinspot', 'crex24', 'cryptocom', 'currencycom', 'delta', 'deribit', 'digifinex', 'eqonex', 'exmo', 'flowbtc', 'fmfwio', 'ftx', 'ftxus', 'gateio', 'gemini', 'hitbtc', 'hitbtc3', 'hollaex', 'huobi', 'huobijp', 'huobipro', 'idex', 'independentreserve', 'indodax', 'itbit', 'kraken', 'kucoin', 'kucoinfutures', 'kuna', 'latoken', 'lbank', 'liquid', 'luno', 'lykke', 'mercado', 'mexc', 'ndax', 'novadax', 'oceanex', 'okcoin', 'okex', 'okex5', 'okx', 'paymium', 'phemex', 'poloniex', 'probit', 'qtrade', 'ripio', 'stex', 'therock', 'tidebit', 'tidex', 'timex', 'upbit', 'vcc', 'wavesexchange', 'wazirx', 'whitebit', 'woo', 'xena', 'yobit', 'zaif', 'zb', 'zipmex', 'zonda']
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
    header = ["Timestamp", "Open", "High", "Low", "Close", "Volume"]
    df = pd.DataFrame(data, columns=header)

    df.Timestamp = (
        df.Timestamp / 1000
    ) 
    df["Timestamp"] = pd.to_datetime(df.Timestamp, unit="s")

    df = df[["Timestamp", "Open", "High", "Low", "Close", "Volume"]]

    df["Open"] = pd.to_numeric(df["Open"])
    df["High"] = pd.to_numeric(df["High"])
    df["Low"] = pd.to_numeric(df["Low"])
    df["Close"] = pd.to_numeric(df["Close"])
    df["Volume"] = pd.to_numeric(df["Volume"])

    return df


# ## Funciones-Fecthc Order Book para los distintos apis

# In[18]:


def tim():
    t=time.localtime(time.time())
    return str(t[0])+"-"+str(t[1])+"-"+str(t[2])
tim()


# In[22]:


def fetch_order_book_bitso(symbol,limit):
    exchange = ccxt.bitso()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk['Index'] = dfk.index 
    dfk["Exchange"]=exchange
    dfk["Ticker"]=symbol
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    SA=(-(((dfk.Bid+dfk.Ask)/2)/2)**2)
    dfk["Roll Spread"]=(np.sqrt(-SA))*2
    
                       
    return dfk


# In[20]:


def fetch_order_book_ascendex(symbol,limit):
    exchange = ccxt.ascendex()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk['Index'] = dfk.index 
    dfk["Exchange"]=exchange
    dfk["Ticker"]=symbol
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    SA=(-(((dfk.Bid+dfk.Ask)/2)/2)**2)
    dfk["Roll Spread"]=(np.sqrt(-SA))*2
                      
    return dfk


# In[21]:


def fetch_order_book_bitbay(symbol,limit):
    exchange = ccxt.bitbay()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk['Index'] = dfk.index 
    dfk["Exchange"]=exchange
    dfk["Ticker"]=symbol
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    SA=(-(((dfk.Bid+dfk.Ask)/2)/2)**2)
    dfk["Roll Spread"]=(np.sqrt(-SA))*2
    
                       
    return dfk


# In[13]:


def fetch_order_book_bitbns(symbol,limit):
    exchange = ccxt.bitbns()
    bi_btc_ob = exchange.fetch_order_book(symbol,limit=limit)
    bi_btc_ob_time=bi_btc_ob["datetime"]
    bi_btc_ob_ask=pd.DataFrame(bi_btc_ob["asks"],columns=["Ask","AVolume"])
    bi_btc_ob_bid=pd.DataFrame(bi_btc_ob["bids"],columns=["Bid","BVolume"])
    dfk = pd.concat([bi_btc_ob_ask,  bi_btc_ob_bid],axis=1)
    dfk['Index'] = dfk.index 
    dfk["Exchange"]=exchange
    dfk["Ticker"]=symbol
    dfk["Timestamp"]=bi_btc_ob_time
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Total Volume"]=(dfk.AVolume + dfk.BVolume)
    dfk["Midprice"]=((dfk.Ask + dfk.Bid)/2)
    dfk['Vwap Ask'] =(np.cumsum(dfk.Ask*dfk.AVolume) / np.cumsum(dfk.AVolume))
    dfk['Vwap Bid'] =(np.cumsum(dfk.Bid*dfk.BVolume) / np.cumsum(dfk.BVolume))
    dfk["Spread"]=(dfk.Bid - dfk.Ask)
    SA=(-(((dfk.Bid+dfk.Ask)/2)/2)**2)
    dfk["Roll Spread"]=(np.sqrt(-SA))*2
    
    return dfk


# In[ ]:




