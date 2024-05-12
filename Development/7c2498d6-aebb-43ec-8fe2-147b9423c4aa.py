class StockDataDisplayer:
    def __init__(self, stock_data):
        self.stock_data = stock_data

    def display_data(self):
        st.write(self.stock_data)

class StockPage:
    def __init__(self):
        self.symbol = st.text_input("Enter stock symbol", value='SNOW')
        self.start_date = st.date_input("Start date", value=(datetime.now() - timedelta(days=35)))
        self.end_date = st.date_input("End date", value=datetime.now())

    def display(self):
        if st.button("Fetch Data"):
            fetcher = StockDataFetcher(self.symbol, self.start_date, self.end_date)
            stock_data = fetcher.fetch_data()
            if not stock_data.empty:
                displayer = StockDataDisplayer(stock_data)
                displayer.display_data()
            else:
                st.write("No data available for the selected dates.")

