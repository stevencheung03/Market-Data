import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import csv

def get_individual_market_data(ticker: str, v_start: str, v_end: str, v_period: str, v_interval: str):
    """Fetches market data for a given stock ticker within a specified time range and saves it as a CSV file.

    Args:
        ticker (str): The stock ticker symbol.
        v_start (str): The start date for the data retrieval in 'YYYY-MM-DD' format.
        v_end (str): The end date for the data retrieval in 'YYYY-MM-DD' format.
        v_period (str): The data period (e.g., "1d", "5d", "1mo", "3mo", "1y").
        v_interval (str): The interval between data points (e.g., "1m", "5m", "1d", "1wk").

    Returns:
        _type_: A DataFrame containing the fetched market data.
    """
    data = yf.download(ticker, start=v_start, end=v_end, period=v_period, interval=v_interval)
    with open(f'Market-Data/DataSets/{v_start}_{v_end}_{ticker}".csv', "w") as f:
        for i in data.to_csv():
            f.write(i)
    return data

print(get_individual_market_data("AAPL", "2024-01-01", "2025-01-01", "1d", "1d").to_csv())
