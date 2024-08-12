import yfinance as yf # type: ignore

def download_data():
    # Download historical data for Bitcoin
    btc_data = yf.download('BTC-USD', start='2020-01-01', end='2024-01-01', interval='1d')
    btc_data.to_csv('E://download//elevate//BITCOIN PRICE PREDICTION//bitcoin_data.csv')

if __name__ == "__main__":
    download_data()
