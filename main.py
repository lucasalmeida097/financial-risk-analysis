import os
from src.fetch_data import fecth_daily_data
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    symbol = "BBDC3.SA"
    try:
        df = fecth_daily_data(symbol)        
        output_path = f"data/{symbol.replace('.', '_')}.csv"
        os.makedirs("data", exist_ok=True)
        df.to_csv(output_path)
        logging.info(f"Data saved to {output_path}")
        
    except Exception as e:
        logging.exception(f"An error occurred: {e}")