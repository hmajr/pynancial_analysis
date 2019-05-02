if __name__ == "__main__":
    ## IMPORTA BIBLIOTECAS
    ##
    print("CARREGANDO BIBLIOTECA...", end = " ")
    from pandas_datareader import data, wb
    import pandas as pd
    import numpy as np
    from datetime import datetime
    print(" DONE!!!")
    
    # SEta tempo de busca
    start_time = datetime(2014, 1, 1)
    end_time = datetime(2019, 1, 1)

    print("\nCarregando dados...")
    # FETCH - Bank of America
    print("Bank of America...", end=" ")
    BNK_AMR = data.DataReader("BAC", 'iex',start=start_time, end=end_time)        
    print("OK!")
 
    # # FETCH - CitiGroup
    # print("City Group...", end=" ")
    # CTY_GRP = data.DataReader("C", 'iex',start=start_time, end=end_time)
    # print("OK!")

    # # FETCH - Goldman Sachs
    # print("Goldman Sachs...", end=" ")
    # GLD_SCH = data.DataReader("GD=F", 'iex',start=start_time, end=end_time)
    # print("OK!")

    # # FETCH - JPMorgan Chase
    # print("JP Morgan Chase...", end=" ")
    # JPM_CHS = data.DataReader("JPM", 'iex',start=start_time, end=end_time)
    # print("OK!")

    # # FETCH - Morgan Stanley
    # print("Morgan Stanley...", end=" ")
    # MRG_STL = data.DataReader("MS", 'iex',start=start_time, end=end_time)
    # print("OK!")

    # # FETCH - Wells Fargo
    # print("WFC...", end=" ")
    # WLL_FRG = data.DataReader("BACWLL_FRG", 'iex',start=start_time, end=end_time)
    # print("OK!")

    print("DONE!!!")
