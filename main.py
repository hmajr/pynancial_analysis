if __name__ == "__main__":
    ##
    # IMPORTA BIBLIOTECAS
    ##
    print("CARREGANDO BIBLIOTECA...", end = " ")
    from pandas_datareader import data, wb
    import pandas as pd
    import numpy as np
    from datetime import datetime
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Optional Plotly Method Imports
    import plotly.plotly
    import cufflinks as cf
    cf.go_offline()
    print(" DONE!!!\n")
    

    ##
    # VARIABLES
    ##

    # Set search datetime
    start_time = datetime(2010, 1, 4)
    end_time = datetime(2019, 1, 1)
    pinrt(" == DATA UTILIZADAS ==")
    print("Data inicio: {} \n Data fim: {}".format(start_time, end_time))

    ## SERVIDOR
    SERVER = 'stooq' #stock data source server
    
    ## STOCKS CODES
    bank_dict = {"BAC": "Bank of America", "C": "City Group", "GS": "Goldman Sachs", 
                 "JPM": "JP Morgan Chase", "MS": "Morgan Stanley", "WFC": "Wells Fargo"}
    tickers = list(bank_dict.keys())
    
    df_bank = {}

    ##
    # DATA
    ##
    print("\nCarregando dados...")
    for bank in bank_dict:
        # FETCH - Bank
        print("{}...".format(bank_dict[bank]), end=" ")
        temp = data.DataReader(bank, SERVER, start=start_time, end=end_time)
        df_bank[bank] = temp
        print("OK!")
    print("IMPORT DONE!!!")

    ##
    # DATA FRAME TREATMENT
    ##

    #Concat bank stock data frame
    bank_stocks = pd.concat(df_bank, axis=1)

    #Set column name level 0
    bank_stocks.columns.names = ['Bank Ticker', 'Stock Info']

    #Check data frame
    print(bank_stocks.head())

    ##
    # EDA
    ##

    #Max close
    print("\n== Max close price ==\n")
    print(bank_stocks.xs(key="Close", axis=1, level="Stock Info").max())

    #Percent return
    print("\n == Bank price returns ==\n")
    returns = pd.DataFrame()
    bank_stocks_pct = bank_stocks

    for ticker in tickers:
        bank_stocks_pct[ticker, "Return"] = bank_stocks[ticker].xs(
            key="Close", axis=1).pct_change()
    banks_returns = bank_stocks_pct.xs(key="Return", axis=1, level=1)
    print(banks_returns.head())

    sns.pairplot(data=banks_returns[1:])
    plt.show()

    