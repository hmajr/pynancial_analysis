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
    plotly.tools.set_credentials_file(username="hmajr", api_key="H9q8iDo6taiqDURM445u")
    import cufflinks as cf
    cf.go_offline()
    print(" DONE!!!\n")
    

    ##
    # VARIABLES
    ##

    # Set search datetime
    start_time = datetime(2010, 1, 4)
    end_time = datetime(2019, 1, 1)
    print(" == DATA UTILIZADAS ==")
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

    #Max return date
    print("\n == Best return date ==\n")
    print(banks_returns.idxmax())

    print("\n == Worst return date ==\n")
    print(banks_returns.idxmin())

    print("\n == Deviation return ==\n")
    print(banks_returns.std())

    ## Distribuicao normal Morgan Stanley
    print("\n == Distribuicao normal Morgan Stanley ==\n")
    sns.set(style="whitegrid")
    sns.distplot(banks_returns["2015-01-01":"2015-12-31"]["MS"],
                 bins=100, color="green")
    plt.show()

    ## Distribuicao normal City Bank
    print("\n == Distribuicao normal City Bank ==\n")
    sns.distplot(banks_returns["2011-01-01":"2011-12-31"]["C"],
                 color="red", bins=100)
    plt.show()

    ## Plot stock close prices
    print("\n == Grafico Preco Fechamento ==\n")
    sns.set(style="whitegrid", rc={'figure.figsize': (13, 7)})
    for ticker in tickers:
        bank_stocks[ticker]["Close"].plot(
            kind="line", figsize=(12, 6), label=ticker)
    plt.legend()
    plt.show()

    ## Interative close price stocks
    print("\n == Grafico Interativo Preco Fechamento ==\n")
    bank_stocks.xs(key="Close", axis=1, level=1).iplot()

    ## interative MMA plot
    print("\n == Grafico Interativo Media Movel ==\n")
    sns.set(style="whitegrid")
    bank_stocks["BAC"]["Close"].loc["2011-01-01":"2011-12-31"].rolling(
        window=30).mean().plot(label="MMA 30")
    bank_stocks["BAC"]["Close"].loc["2011-01-01":"2011-12-31"].plot(
        label="BAC CLOSE", color="green")
    plt.legend()
    plt.show()

    ## Heatmap stock correlation
    print("\n == Grafico Heatmap Correlacao Preco Fechamento ==\n")
    sns.heatmap(bank_stocks.xs(key="Close", axis=1, level=1).corr(),
                annot=True, cmap="rocket_r")
    plt.legend()
    plt.show()

    ## Cluster stock correlation
    print("\n == Grafico Cluster Correlacao Preco Fechamento ==\n")
    sns.clustermap(bank_stocks.xs(key="Close", axis=1,
                                  level=1).corr(), annot=True, cmap="rocket_r")
    plt.legend()
    plt.show()

    ## Interative Heatmap stock correlation
    print("\n == Grafico Heatmap interativo ==\n")
    bank_stocks.xs(key="Close", axis=1, level=1).corr().iplot(
        kind="heatmap", colorscale='rdylbu')
    plt.show()

    ## Interative Candle graph
    print("\n == Grafico Candlestick ==\n")
    bank_stocks["BAC"].loc["2015-01-01":"2016-01-01"].iplot(kind="candle")
    plt.show()

    ## Interactive MMA graph plot
    print("\n == Grafico Media Movel Interativo ==\n")
    bank_stocks["MS"]["Close"].loc["2015-01-01":
                                   "2015-12-31"].ta_plot(study="sma")
    plt.show()

    ## Interactive Bollinger`s Band graph
    print("\n == Grafico Banda Bollinger Interativo ==\n")
    bank_stocks["BAC"]["Close"].loc["2015-01-01":
                                    "2015-12-31"].ta_plot(study="boll", color="red")
    plt.show()
