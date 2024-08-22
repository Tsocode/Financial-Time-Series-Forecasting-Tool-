from flask import Flask, render_template
import yfinance as yf
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Function to fetch financial data from Yahoo Finance
def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")
    return hist

# Define the route for the homepage/dashboard
@app.route('/')
def dashboard():
    # Get data for a particular stock, e.g., Apple Inc.
    ticker = "AAPL"
    stock_data = get_stock_data(ticker)

    # Example: Calculate the latest closing price, year high, and low
    latest_close = stock_data['Close'].iloc[-1]
    year_high = stock_data['Close'].max()
    year_low = stock_data['Close'].min()

    # Example: Mockup data (you can replace this with actual calculations)
    financial_data = {
        'ticker': ticker,
        'latest_close': round(latest_close, 2),
        'year_high': round(year_high, 2),
        'year_low': round(year_low, 2),
        'forecast': 'Moderate growth expected based on current trends'
    }

    # Render the dashboard template with the financial data
    return render_template('dashboard.html', data=financial_data)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
