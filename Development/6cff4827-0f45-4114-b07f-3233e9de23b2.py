class StockDataFetcher:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.ticker = yfc.Ticker(self.symbol)

    def fetch_data(self):
        # Fetch historical stock data
        stock_data = self.ticker.history(start=self.start_date, end=self.end_date)
        stock_data.reset_index(inplace=True)
        stock_data['Date'] = stock_data['Date'].dt.date
        earning_dates = self.ticker.get_earnings_dates()
        earning_dates.reset_index(inplace=True)
        earning_dates['Earnings Date'] = pd.to_datetime(earning_dates['Earnings Date'])
        earning_dates['Earnings Date'] = earning_dates['Earnings Date'].dt.date

        # Drop duplicates from the index
        stock_data = stock_data.loc[~stock_data.index.duplicated(keep='first')]
        # Calculate %Change for Adj Close and Intraday Up and Down, based on Open price
        stock_data['%Change_1d'] = stock_data['Open'].pct_change()*100
        stock_data['%Change_1w'] = stock_data['Open'].pct_change(7)*100
        stock_data['%Change_1m'] = stock_data['Open'].pct_change(30)*100
        stock_data['%Intraday_up'] = (stock_data['High'] - stock_data['Open']) / stock_data['Open']*100
        stock_data['%Intraday_down'] = (stock_data['Open'] - stock_data['Low']) / stock_data['Open']*100

        stock_data = pd.merge(stock_data, earning_dates, left_on='Date', right_on='Earnings Date', how='left')        
        # Drop High and Low columns
        stock_data.drop(['High', 'Low','Close','Stock Splits'], axis=1, inplace=True)

        return stock_data
