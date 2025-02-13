# crypto-data-analysis
Below is an example of a comprehensive README file in Markdown format for your GitHub repository:

---

# Live Cryptocurrency Data Fetching and Analysis

This repository provides a Python-based solution to fetch, analyze, and visualize live cryptocurrency data. It targets the top 50 cryptocurrencies by market capitalization using the CoinGecko API and includes an automated Excel integration for continuous data updates.

## Overview

The project performs the following key tasks:

- **Live Data Fetching:** Retrieves real-time data for the top 50 cryptocurrencies, including key metrics such as current price, market capitalization, trading volume, and 24-hour price changes.
- **Data Analysis:** Identifies the top 5 cryptocurrencies by market cap, calculates the average price of all 50 coins, and determines the highest and lowest 24-hour percentage price changes.
- **Excel Integration:** Updates an Excel file (`crypto_data.xlsx`) every 5 minutes to reflect the latest data.
- **Alternative Setup:** Provides instructions for using Excel's Power Query to directly integrate live data from the API.

## Features

- **Automated Data Retrieval:** Uses the CoinGecko API to fetch live cryptocurrency data.
- **Real-time Analysis:** Processes data to extract critical market insights.
- **Scheduled Updates:** Automatically refreshes the data every 5 minutes.
- **Dual Integration Methods:** Supports both a Python-script-based approach and Excel Power Query for live data updates.

## Prerequisites

- **Python 3.6+**
- Required Python libraries:
  - `requests`
  - `pandas`
  - `openpyxl`

Install the dependencies using pip:

```bash
pip install requests pandas openpyxl
```

## Getting Started

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/crypto-data-fetcher.git
cd crypto-data-fetcher
```

### Running the Python Script

Execute the Python script to start fetching and analyzing the cryptocurrency data:

```bash
python crypto_data_fetcher.py
```

The script will:
- Fetch live data from the CoinGecko API.
- Analyze the data to determine key market insights.
- Update an Excel file (`crypto_data.xlsx`) with the latest data every 5 minutes.

### Setting Up Live Data in Excel Using Power Query

Alternatively, you can set up live data updates directly in Excel:

1. **Open Excel** and go to the **Data** tab.
2. Click on **Get Data > From Other Sources > From Web**.
3. Enter the following URL:
   ```
   https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false
   ```
4. In the Power Query Editor, select and format the following fields:
   - `name`
   - `symbol`
   - `current_price`
   - `market_cap`
   - `total_volume`
   - `price_change_percentage_24h`
5. Set the query refresh interval to **300 seconds (5 minutes)** in the Query Properties.

## Data Analysis Report

When the script is running, it prints key insights to the console:

- **Top 5 Cryptocurrencies by Market Cap:** Lists the names, symbols, and market capitalization of the leading cryptocurrencies.
- **Average Price Calculation:** Computes the average price across the top 50 cryptocurrencies.
- **Price Change Analysis:** Displays the highest and lowest 24-hour percentage price changes.

These insights can be compiled into a detailed report for further analysis.

## Future Enhancements

- **Improved Error Handling:** Enhance robustness and logging during data retrieval.
- **Expanded Metrics:** Include additional data points such as historical trends and technical indicators.
- **User Interface:** Develop a web-based dashboard for more interactive data visualization.
- **Multi-API Support:** Integrate with additional cryptocurrency data providers like CoinMarketCap or Binance.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with any improvements or bug fixes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any questions or feedback, please open an issue or contact the repository maintainer.

Happy coding!

---
