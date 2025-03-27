import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import csv

def get_individual_market_data(ticker: str, v_start: str, v_end: str, v_period: str, v_interval: str):
    data = yf.download(ticker, start=v_start, end=v_end, period=v_period, interval=v_interval)
    with open("Market-Data/DataSets/"+v_start+"_"+v_end+"_"+ticker+".csv", "w") as f:
        for i in data.to_csv():
            f.write(i)
    return data

print(get_individual_market_data("AAPL", "2024-01-01", "2025-01-01", "1d", "1d").to_csv())
