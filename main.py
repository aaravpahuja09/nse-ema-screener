import yfinance as yf
def ema_9():

    stocks = [
"360ONE.NS","ABB.NS","APLAPOLLO.NS","AUBANK.NS","ADANIENSOL.NS","ADANIENT.NS","ADANIGREEN.NS","ADANIPORTS.NS","ADANIPOWER.NS",
"ABCAPITAL.NS","ALKEM.NS","AMBER.NS","AMBUJACEM.NS","ANGELONE.NS","APOLLOHOSP.NS","ASHOKLEY.NS","ASIANPAINT.NS","ASTRAL.NS",
"AUROPHARMA.NS","DMART.NS","AXISBANK.NS","BSE.NS","BAJAJ-AUTO.NS","BAJFINANCE.NS","BAJAJFINSV.NS","BAJAJHLDNG.NS","BANDHANBNK.NS",
"BANKBARODA.NS","BANKINDIA.NS","BDL.NS","BEL.NS","BHARATFORG.NS","BHEL.NS","BPCL.NS","BHARTIARTL.NS","BIOCON.NS","BLUESTARCO.NS",
"BOSCHLTD.NS","BRITANNIA.NS","CGPOWER.NS","CANBK.NS","CDSL.NS","CHOLAFIN.NS","CIPLA.NS","COALINDIA.NS","COCHINSHIP.NS","COFORGE.NS",
"COLPAL.NS","CAMS.NS","CONCOR.NS","CROMPTON.NS","CUMMINSIND.NS","DLF.NS","DABUR.NS","DALBHARAT.NS","DELHIVERY.NS","DIVISLAB.NS",
"DIXON.NS","DRREDDY.NS","EICHERMOT.NS","ESCORTS.NS","FEDERALBNK.NS","GAIL.NS","GLENMARK.NS","GMRINFRA.NS","GODREJCP.NS","GODREJPROP.NS",
"GRASIM.NS","GUJGASLTD.NS","HAVELLS.NS","HCLTECH.NS","HDFCAMC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEROMOTOCO.NS","HINDALCO.NS","HINDPETRO.NS",
"HINDUNILVR.NS","ICICIBANK.NS","ICICIGI.NS","ICICIPRULI.NS","IDFCFIRSTB.NS","INDHOTEL.NS","INDIGO.NS","INDUSINDBK.NS","INDUSTOWER.NS","INFY.NS",
"IRCTC.NS","ITC.NS","JINDALSTEL.NS","JSWSTEEL.NS","JUBLFOOD.NS","KOTAKBANK.NS","LT.NS","LTF.NS","LICHSGFIN.NS","LODHA.NS","LUPIN.NS",
"MANAPPURAM.NS","MARICO.NS","MARUTI.NS","MCDOWELL-N.NS","MCX.NS","METROPOLIS.NS","MGL.NS","MOTHERSON.NS","MPHASIS.NS","MRF.NS","MUTHOOTFIN.NS",
"NATIONALUM.NS","NAVINFLUOR.NS","NMDC.NS","NTPC.NS","OBEROIRLTY.NS","ONGC.NS","PAGEIND.NS","PATANJALI.NS","PEL.NS","PERSISTENT.NS","PETRONET.NS",
"PIDILITIND.NS","PIIND.NS","PNB.NS","POLYCAB.NS","POWERGRID.NS","PVRINOX.NS","RAMCOCEM.NS","RECLTD.NS","RELIANCE.NS","SAIL.NS","SBICARD.NS",
"SBILIFE.NS","SBIN.NS","SHREECEM.NS","SIEMENS.NS","SRF.NS","SUNPHARMA.NS","SUNTV.NS","SUZLON.NS","SYRMA.NS","TATACHEM.NS","TATACOMM.NS",
"TATACONSUM.NS","TATAELXSI.NS","TATAMOTORS.NS","TATAPOWER.NS","TATASTEEL.NS","TECHM.NS","TIMKEN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TRENT.NS",
"TVSMOTOR.NS","UBL.NS","ULTRACEMCO.NS","UNIONBANK.NS","UPL.NS","VEDL.NS","VOLTAS.NS","WIPRO.NS","YESBANK.NS","ZEEL.NS","ZYDUSLIFE.NS"
]

    for ticker in stocks:
        print(f"\nAnalyzing {ticker}...")
        stock_data = yf.Ticker(ticker)
        history = stock_data.history(period="1y")  # more data for stability
        close_prices = history['Close'].tolist()

        if len(close_prices) < 9:
            print(f"Not enough data for {ticker}")
            continue
        l1=[]
        l2=[]

        # Step A: SMA for first 9 days
        sma_9 = sum(close_prices[:9]) / 9

        # Step B: Multiplier
        multiplier = 2 / (9 + 1)

        # Step C: EMA calculation
        ema_values = []
        current_ema = sma_9
        for price in close_prices[9:]:
            current_ema = (price * multiplier) + (current_ema * (1 - multiplier))
            ema_values.append(current_ema)

        latest_close = close_prices[-1]
        latest_ema = ema_values[-1]

        print(f"Latest Close Price: Rs. {latest_close:.2f}")
        print(f"9 Day EMA Line:     Rs. {latest_ema:.2f}")

        if latest_close > latest_ema:
            print("Result: BULLISH SIGN (above 9 EMA)")
        else:
            print("Result: BEARISH SIGN (below 9 EMA)")
            l2.append(ticker)
def stock_filteration():


        stocks = [
    "360ONE.NS","ABB.NS","APLAPOLLO.NS","AUBANK.NS","ADANIENSOL.NS","ADANIENT.NS","ADANIGREEN.NS","ADANIPORTS.NS","ADANIPOWER.NS",
    "ABCAPITAL.NS","ALKEM.NS","AMBER.NS","AMBUJACEM.NS","ANGELONE.NS","APOLLOHOSP.NS","ASHOKLEY.NS","ASIANPAINT.NS","ASTRAL.NS",
    "AUROPHARMA.NS","DMART.NS","AXISBANK.NS","BSE.NS","BAJAJ-AUTO.NS","BAJFINANCE.NS","BAJAJFINSV.NS","BAJAJHLDNG.NS","BANDHANBNK.NS",
    "BANKBARODA.NS","BANKINDIA.NS","BDL.NS","BEL.NS","BHARATFORG.NS","BHEL.NS","BPCL.NS","BHARTIARTL.NS","BIOCON.NS","BLUESTARCO.NS",
    "BOSCHLTD.NS","BRITANNIA.NS","CGPOWER.NS","CANBK.NS","CDSL.NS","CHOLAFIN.NS","CIPLA.NS","COALINDIA.NS","COCHINSHIP.NS","COFORGE.NS",
    "COLPAL.NS","CAMS.NS","CONCOR.NS","CROMPTON.NS","CUMMINSIND.NS","DLF.NS","DABUR.NS","DALBHARAT.NS","DELHIVERY.NS","DIVISLAB.NS",
    "DIXON.NS","DRREDDY.NS","EICHERMOT.NS","ESCORTS.NS","FEDERALBNK.NS","GAIL.NS","GLENMARK.NS","GODREJCP.NS","GODREJPROP.NS",
    "GRASIM.NS","GUJGASLTD.NS","HAVELLS.NS","HCLTECH.NS","HDFCAMC.NS","HDFCBANK.NS","HDFCLIFE.NS","HEROMOTOCO.NS","HINDALCO.NS","HINDPETRO.NS",
    "HINDUNILVR.NS","ICICIBANK.NS","ICICIGI.NS","ICICIPRULI.NS","IDFCFIRSTB.NS","INDHOTEL.NS","INDIGO.NS","INDUSINDBK.NS","INDUSTOWER.NS","INFY.NS",
    "IRCTC.NS","ITC.NS","JINDALSTEL.NS","JSWSTEEL.NS","JUBLFOOD.NS","KOTAKBANK.NS","LT.NS","LTF.NS","LTIM.NS","LICHSGFIN.NS","LODHA.NS","LUPIN.NS",
    "MANAPPURAM.NS","MARICO.NS","MARUTI.NS","MCDOWELL-N.NS","MCX.NS","METROPOLIS.NS","MGL.NS","MOTHERSON.NS","MPHASIS.NS","MRF.NS","MUTHOOTFIN.NS",
    "NATIONALUM.NS","NAVINFLUOR.NS","NMDC.NS","NTPC.NS","OBEROIRLTY.NS","ONGC.NS","PAGEIND.NS","PATANJALI.NS","PEL.NS","PERSISTENT.NS","PETRONET.NS",
    "PIDILITIND.NS","PIIND.NS","PNB.NS","POLYCAB.NS","POWERGRID.NS","PVRINOX.NS","RAMCOCEM.NS","RECLTD.NS","RELIANCE.NS","SAIL.NS","SBICARD.NS",
    "SBILIFE.NS","SBIN.NS","SHREECEM.NS","SIEMENS.NS","SRF.NS","SUNPHARMA.NS","SUNTV.NS","SUZLON.NS","SYRMA.NS","TATACHEM.NS","TATACOMM.NS",
    "TATACONSUM.NS","TATAELXSI.NS","TATAMOTORS.NS","TATAPOWER.NS","TATASTEEL.NS","TECHM.NS","TIMKEN.NS","TORNTPHARM.NS","TORNTPOWER.NS","TRENT.NS",
    "TVSMOTOR.NS","UBL.NS","ULTRACEMCO.NS","UNIONBANK.NS","UPL.NS","VEDL.NS","VOLTAS.NS","WIPRO.NS","YESBANK.NS","ZEEL.NS","ZYDUSLIFE.NS"
]


        list1, list2, list3, list4, list5 = [], [], [], [], []

        for ticker in stocks:
            stock_data = yf.Ticker(ticker)
            history = stock_data.history(period="6mo")  # more data for stability
            close_prices = history['Close'].tolist()

            if len(close_prices) < 9:
                continue

            # Step A: SMA for first 9 days
            sma_9 = sum(close_prices[:9]) / 9
            multiplier = 2 / (9 + 1)

            # Step B: EMA calculation
            ema_values = []
            current_ema = sma_9
            for price in close_prices[9:]:
                current_ema = (price * multiplier) + (current_ema * (1 - multiplier))
                ema_values.append(current_ema)

            closes = close_prices[9:]

            latest_close = closes[-1]
            latest_ema = ema_values[-1]

            # Bearish check first
            if latest_close < latest_ema:
                list4.append(ticker)
                continue  # skip other lists if bearish

            # Bullish stocks only go into Lists 1–3–5
            if closes[-2] > ema_values[-2] and closes[-3] <= ema_values[-3]:
                list1.append(ticker)  # crossed yesterday
            elif closes[-3] > ema_values[-3] and closes[-4] <= ema_values[-4]:
                list2.append(ticker)  # crossed 2 days ago
            elif closes[-4] > ema_values[-4] and closes[-5] <= ema_values[-5]:
                list3.append(ticker)  # crossed 3 days ago
            else:
                # Check if last crossover was more than 3 days ago
                for i in range(len(closes) - 4):
                    if closes[i+1] > ema_values[i+1] and closes[i] <= ema_values[i]:
                        if i < len(closes) - 4:  # older than 3 days
                            list5.append(ticker)
                        break

        print("\nCrossed 1 day ago + currently bullish:", list1)
        print("\n\n\nCrossed 2 days ago + currently bullish:", list2)
        print("\n\n\nCrossed 3 days ago + currently bullish:", list3)
        print("\n\n\nCrossed >3 days ago + currently bullish):", list5)
        print("\n\n\nCurrently bearish moves:", list4)
        
print('''prompt 1 for checking the list of bullish and bearish stocks
prompt 2 for filteration of stocks on the basis of day of crossing 9ema line''')
while True:
    ch=int(input("Enter prompt: "))
    if ch==1:
        ema_9()
    if ch==2:
        stock_filteration()
    a=input("continue?(y/n)")
    if a in "yY":
        continue
    else:
        break



