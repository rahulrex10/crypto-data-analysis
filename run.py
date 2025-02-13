import requests
import pandas as pd
import time

def fetch_crypto_data():
    """
    Fetches live cryptocurrency data for the top 50 coins by market cap using CoinGecko API.
    Returns:
        data (list): List of dictionaries containing cryptocurrency details.
    """
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',         # Prices in USD
        'order': 'market_cap_desc',     # Order by market cap descending
        'per_page': 50,                 # Fetch top 50 cryptocurrencies
        'page': 1,
        'sparkline': 'false'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data:", response.status_code)
        return []

def analyze_data(data):
    """
    Analyzes the fetched data.
    - Identifies the top 5 cryptocurrencies by market cap.
    - Calculates the average price of the top 50 cryptocurrencies.
    - Finds the highest and lowest 24-hour percentage price changes.
    
    Args:
        data (list): List of cryptocurrency data dictionaries.
        
    Returns:
        top_5 (DataFrame): DataFrame of top 5 cryptocurrencies by market cap.
        avg_price (float): Average current price of the 50 cryptocurrencies.
        highest_change (float): Highest 24-hour percentage price change.
        lowest_change (float): Lowest 24-hour percentage price change.
        df (DataFrame): Full DataFrame for all 50 cryptocurrencies.
    """
    df = pd.DataFrame(data)
    
    # Ensure the necessary columns are present
    required_columns = [
        'name', 'symbol', 'current_price', 'market_cap',
        'total_volume', 'price_change_percentage_24h'
    ]
    if not all(col in df.columns for col in required_columns):
        raise ValueError("One or more required fields are missing from the API response.")

    # Analysis
    top_5 = df.nlargest(5, 'market_cap')  # Top 5 by market capitalization
    avg_price = df['current_price'].mean()  # Average price across 50 coins
    highest_change = df['price_change_percentage_24h'].max()  # Highest 24h % change
    lowest_change = df['price_change_percentage_24h'].min()   # Lowest 24h % change
    
    return top_5, avg_price, highest_change, lowest_change, df

def update_excel(df, filename="crypto_data.xlsx"):
    """
    Writes the DataFrame to an Excel file.
    
    Args:
        df (DataFrame): DataFrame containing cryptocurrency data.
        filename (str): Name of the Excel file to save.
    """
    try:
        df.to_excel(filename, index=False)
        print(f"Excel file '{filename}' updated successfully.")
    except Exception as e:
        print("Error updating Excel file:", e)

def main():
    """
    Main function to continuously fetch, analyze, and update the Excel file.
    It repeats every 5 minutes.
    """
    while True:
        print("Fetching live cryptocurrency data...")
        crypto_data = fetch_crypto_data()
        if not crypto_data:
            print("No data fetched. Retrying in 5 minutes...")
            time.sleep(300)
            continue
        
        # Perform analysis
        top_5, avg_price, highest_change, lowest_change, df = analyze_data(crypto_data)
        
        # Display analysis results
        print("\n--- Analysis Report ---")
        print("Top 5 Cryptocurrencies by Market Cap:")
        print(top_5[['name', 'symbol', 'market_cap']].to_string(index=False))
        print("\nAverage Price of Top 50 Cryptocurrencies: ${:.2f}".format(avg_price))
        print("Highest 24h Percentage Price Change: {:.2f}%".format(highest_change))
        print("Lowest 24h Percentage Price Change: {:.2f}%".format(lowest_change))
        print("-----------------------\n")
        
        # Update Excel sheet with the latest data
        update_excel(df)
        
        # Wait for 5 minutes (300 seconds) before the next update
        print("Waiting for 5 minutes before next update...\n")
        time.sleep(300)

if __name__ == '__main__':
    main()
