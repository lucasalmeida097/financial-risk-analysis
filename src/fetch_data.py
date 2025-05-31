import yfinance as yf
import logging

logging.basicConfig(level=logging.INFO)

def fecth_daily_data(symbol: str, start: str = "2010-01-01", end: str = None):
    logging.info(f"Fetching data for symbol: {symbol}")
    df = yf.download(symbol, start=start,end=end)

    if df.empty :
        logging.error(f"No data found for symbol '{symbol}'")
        raise ValueError(f"No data found for symbol '{symbol}'")
    
    df = df[["Close"]].rename(columns={"Close": "adjusted_close"})
    logging.info(f"Data fetched successfully: {len(df)} rows")

    return df