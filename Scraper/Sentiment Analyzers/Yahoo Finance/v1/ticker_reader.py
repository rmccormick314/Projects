import pandas as pd
import csv

def read_tickers_nyse(csv_file_path):
    tickers = []

    df = pd.read_csv(csv_file_path)

    for i in df['ACT Symbol']:
        tickers.append(i)

    return(tickers)

def read_tickers_nasdaq(csv_file_path):
    tickers = []

    df = pd.read_csv(csv_file_path)

    for i in df['Symbol']:
        tickers.append(i)

    return(tickers)

def read_names(csv_file_path):
    names = []

    df = pd.read_csv(csv_file_path)

    for i in df['Company Name']:
        names.append(i)

    return(names)

def combine_ticker_sets():
    final_set = list(set(
        read_tickers_nyse("tickers_nyse.csv") +
        read_tickers_nasdaq("tickers_nasdaq.csv")))

    return(final_set)

def combine_name_sets():
    final_set_names = list(set(
        read_names("tickers_nyse.csv") +
        read_names("tickers_nasdaq.csv")))

    return(final_set_names)

def get_all_tickers():
    return(combine_ticker_sets())

def get_all_names():
    return(combine_name_sets())
