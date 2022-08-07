import time
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from selenium import webdriver
from ticker_reader import get_all_tickers, get_all_names
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

today = date.today()

BASE_URL = 'https://finance.yahoo.com'
my_url = 'https://finance.yahoo.com/topic/stock-market-news/'
YAHOO_NEWS_URL = BASE_URL+'/topic/stock-market-news/'

all_tickers = get_all_tickers()
all_names = get_all_names()

def get_page(url):
    """Download a webpage and return a beautiful soup doc"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path=r'C:\Users\richard\Documents\Projects\Scraper\Sentiment Analyzers\Yahoo Finance\v1\chromedriver_win32\chromedriver.exe', options=options)

    driver.get(url)
    SCROLL_PAUSE_TIME = 1

    for i in range(0, 15):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

    doc = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    return doc

def get_news_tags(doc):
    """Get the list of tags containing news information"""
    news_class = "Ov(h) Pend(44px) Pstart(25px)" ## class name of div tag
    news_list  = doc.find_all('div', {'class': news_class})
    return news_list

def parse_news(news_tag):
    """Get the news data point and return dictionary"""
    news_source = news_tag.find('div').text #source
    news_headline = news_tag.find('a').text #heading
    news_url = news_tag.find('a')['href'] #link
    news_content = news_tag.find('p').text #content
    return { 'source' : news_source,
            'headline' : news_headline,
            'url' : BASE_URL + news_url,
            'content' : news_content,
           }

def scrape_yahoo_news():
    doc = get_page(YAHOO_NEWS_URL)

    news_list = get_news_tags(doc)

    news_data = [parse_news(news_tag) for news_tag in news_list]
    news_df = pd.DataFrame(news_data)

    #This return statement is optional, we are doing this just analyze the final output
    return news_df

def analyze_tickers_yahoo(df):
    tickers = {}

    for headline in df.headline:
        for ticker in all_tickers:
            if ticker in headline:
                tickers[ticker] = sid.polarity_scores(headline)['compound']

    return tickers

def generate_report():
    df = scrape_yahoo_news()
    analysis_dict = analyze_tickers_yahoo(df)

    return(analysis_dict)

def print_report():
    dict = generate_report()

    for i, j in dict.items():
        if (j != 0):
            print(i, j)

print_report()
