# Create a dictionary mapping page names to their respective functions
pages = {
    "Stock Data": StockPage
}
# Create a sidebar for navigation
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Execute the selected page function
pages[selection]().display()