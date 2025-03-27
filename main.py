import yfinance as yf
import matplotlib.pyplot as plt
import json

def get_individual_market_data(ticker: str, v_start: str, v_end: str, v_period: str, v_interval: str):
    return yf.download(ticker, start=v_start, end=v_end, period=v_period, interval=v_interval)