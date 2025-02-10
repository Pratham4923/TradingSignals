import streamlit as st
import yfinance as yf
import pandas as pd
import logging
from functools import lru_cache

# Set up logging
logging.basicConfig(level=logging.INFO)

# Predefined list of popular Indian stocks (you can expand this list)
indian_stocks = [
    "ABB.NS"
    ,"ACC.NS"
    ,"APLAPOLLO.NS"
    ,"AUBANK.NS"
    ,"AARTIIND.NS"
    ,"ABBOTINDIA.NS"
    ,"ADANIENSOL.NS"
    ,"ADANIENT.NS"
    ,"ADANIGREEN.NS"
    ,"ADANIPORTS.NS"
    ,"ATGL.NS"
    ,"ABCAPITAL.NS"
    ,"ABFRL.NS"
    ,"ALKEM.NS"
    ,"AMBUJACEM.NS"
    ,"ANGELONE.NS"
    ,"APOLLOHOSP.NS"
    ,"APOLLOTYRE.NS"
    ,"ASHOKLEY.NS"
    ,"ASIANPAINT.NS"
    ,"ASTRAL.NS"
    ,"ATUL.NS"
    ,"AUROPHARMA.NS"
    ,"DMART.NS"
    ,"AXISBANK.NS"
    ,"BSOFT.NS"
    ,"BSE.NS"
    ,"BAJAJ-AUTO.NS"
    ,"BAJFINANCE.NS"
    ,"BAJAJFINSV.NS"
    ,"BALKRISIND.NS"
    ,"BANDHANBNK.NS"
    ,"BANKBARODA.NS"
    ,"BANKINDIA.NS"
    ,"BATAINDIA.NS"
    ,"BERGEPAINT.NS"
    ,"BEL.NS"
    ,"BHARATFORG.NS"
    ,"BHEL.NS"
    ,"BPCL.NS"
    ,"BHARTIARTL.NS"
    ,"BIOCON.NS"
    ,"BOSCHLTD.NS"
    ,"BRITANNIA.NS"
    ,"CESC.NS"
    ,"CGPOWER.NS"
    ,"CANFINHOME.NS"
    ,"CANBK.NS"
    ,"CDSL.NS"
    ,"CHAMBLFERT.NS"
    ,"CHOLAFIN.NS"
    ,"CIPLA.NS"
    ,"CUB.NS"
    ,"COALINDIA.NS"
    ,"COFORGE.NS"
    ,"COLPAL.NS"
    ,"CAMS.NS"
    ,"CONCOR.NS"
    ,"COROMANDEL.NS"
    ,"CROMPTON.NS"
    ,"CUMMINSIND.NS"
    ,"CYIENT.NS"
    ,"DLF.NS"
    ,"DABUR.NS"
    ,"DALBHARAT.NS"
    ,"DEEPAKNTR.NS"
    ,"DELHIVERY.NS"
    ,"DIVISLAB.NS"
    ,"DIXON.NS"
    ,"LALPATHLAB.NS"
    ,"DRREDDY.NS"
    ,"EICHERMOT.NS"
    ,"ESCORTS.NS"
    ,"EXIDEIND.NS"
    ,"NYKAA.NS"
    ,"GAIL.NS"
    ,"GMRAIRPORT.NS"
    ,"GLENMARK.NS"
    ,"GODREJCP.NS"
    ,"GODREJPROP.NS"
    ,"GRANULES.NS"
    ,"GRASIM.NS"
    ,"GUJGASLTD.NS"
    ,"GNFC.NS"
    ,"HCLTECH.NS"
    ,"HDFCAMC.NS"
    ,"HDFCBANK.NS"
    ,"HDFCLIFE.NS"
    ,"HFCL.NS"
    ,"HAVELLS.NS"
    ,"HEROMOTOCO.NS"
    ,"HINDALCO.NS"
    ,"HAL.NS"
    ,"HINDCOPPER.NS"
    ,"HINDPETRO.NS"
    ,"HINDUNILVR.NS"
    ,"HUDCO.NS"
    ,"ICICIBANK.NS"
    ,"ICICIGI.NS"
    ,"ICICIPRULI.NS"
    ,"IDFCFIRSTB.NS"
    ,"IPCALAB.NS"
    ,"IRB.NS"
    ,"ITC.NS"
    ,"INDIAMART.NS"
    ,"INDIANB.NS"
    ,"IEX.NS"
    ,"IOC.NS"
    ,"IRCTC.NS"
    ,"IRFC.NS"
    ,"IGL.NS"
    ,"INDUSTOWER.NS"
    ,"INDUSINDBK.NS"
    ,"NAUKRI.NS"
    ,"INFY.NS"
    ,"INDIGO.NS"
    ,"JKCEMENT.NS"
    ,"JSWENERGY.NS"
    ,"JSWSTEEL.NS"
    ,"JSL.NS"
    ,"JINDALSTEL.NS"
    ,"JIOFIN.NS"
    ,"JUBLFOOD.NS"
    ,"KEI.NS"
    ,"KPITTECH.NS"
    ,"KALYANKJIL.NS"
    ,"KOTAKBANK.NS"
    ,"LTF.NS"
    ,"LTTS.NS"
    ,"LICHSGFIN.NS"
    ,"LTIM.NS"
    ,"LT.NS"
    ,"LAURUSLABS.NS"
    ,"LICI.NS"
    ,"LUPIN.NS"
    ,"MRF.NS"
    ,"LODHA.NS"
    ,"MGL.NS"
    ,"M&MFIN.NS"
    ,"M&M.NS"
    ,"MANAPPURAM.NS"
    ,"MARICO.NS"
    ,"MARUTI.NS"
    ,"MFSL.NS"
    ,"MAXHEALTH.NS"
    ,"METROPOLIS.NS"
    ,"MPHASIS.NS"
    ,"MCX.NS"
    ,"MUTHOOTFIN.NS"
    ,"NBCC.NS"
    ,"NCC.NS"
    ,"NHPC.NS"
    ,"NMDC.NS"
    ,"NTPC.NS"
    ,"NATIONALUM.NS"
    ,"NAVINFLUOR.NS"
    ,"NESTLEIND.NS"
    ,"OBEROIRLTY.NS"
    ,"ONGC.NS"
    ,"OIL.NS"
    ,"PAYTM.NS"
    ,"OFSS.NS"
    ,"POLICYBZR.NS"
    ,"PIIND.NS"
    ,"PVRINOX.NS"
    ,"PAGEIND.NS"
    ,"PERSISTENT.NS"
    ,"PETRONET.NS"
    ,"PIDILITIND.NS"
    ,"PEL.NS"
    ,"POLYCAB.NS"
    ,"POONAWALLA.NS"
    ,"PFC.NS"
    ,"POWERGRID.NS"
    ,"PRESTIGE.NS"
    ,"PNB.NS"
    ,"RBLBANK.NS"
    ,"RECLTD.NS"
    ,"RELIANCE.NS"
    ,"SBICARD.NS"
    ,"SBILIFE.NS"
    ,"SHREECEM.NS"
    ,"SJVN.NS"
    ,"SRF.NS"
    ,"MOTHERSON.NS"
    ,"SHRIRAMFIN.NS"
    ,"SIEMENS.NS"
    ,"SOLARINDS.NS"
    ,"SONACOMS.NS"
    ,"SBIN.NS"
    ,"SAIL.NS"
    ,"SUNPHARMA.NS"
    ,"SUNTV.NS"
    ,"SUPREMEIND.NS"
    ,"SYNGENE.NS"
    ,"TATACONSUM.NS"
    ,"TVSMOTOR.NS"
    ,"TATACHEM.NS"
    ,"TATACOMM.NS"
    ,"TCS.NS"
    ,"TATAELXSI.NS"
    ,"TATAMOTORS.NS"
    ,"TATAPOWER.NS"
    ,"TATASTEEL.NS"
    ,"TECHM.NS"
    ,"FEDERALBNK.NS"
    ,"INDHOTEL.NS"
    ,"PHOENIXLTD.NS"
    ,"RAMCOCEM.NS"
    ,"TITAN.NS"
    ,"TORNTPHARM.NS"
    ,"TORNTPOWER.NS"
    ,"TRENT.NS"
    ,"TIINDIA.NS"
    ,"UPL.NS"
    ,"ULTRACEMCO.NS"
    ,"UNIONBANK.NS"
    ,"UBL.NS"
    ,"UNITDSPR.NS"
    ,"VBL.NS"
    ,"VEDL.NS"
    ,"IDEA.NS"
    ,"VOLTAS.NS"
    ,"WIPRO.NS"
    ,"YESBANK.NS"
    ,"ZOMATO.NS"
    ,"ZYDUSLIFE.NS"
]


@lru_cache(maxsize=128)
def fetch_data(pair, period="1d", interval="5m"):
    """Fetch stock data from Yahoo Finance"""
    try:
        data = yf.download(pair, period=period, interval=interval)
        if data.empty:
            raise ValueError("No data returned for the given pair.")
        return data
    except Exception as e:
        logging.error(f"Error fetching data for {pair}: {e}")
        return None


def calculate_atr(data, window=14):
    """Calculate the Average True Range (ATR) for volatility measurement"""
    data['High-Low'] = data['High'] - data['Low']
    data['High-ClosePrev'] = abs(data['High'] - data['Close'].shift(1))
    data['Low-ClosePrev'] = abs(data['Low'] - data['Close'].shift(1))
    tr = data[['High-Low', 'High-ClosePrev', 'Low-ClosePrev']].max(axis=1)
    data['ATR'] = tr.rolling(window).mean()
    return data


def price_action_strategy(data, pair, atr_multiplier=1.5):
    """Identify trade entry points using price action strategy"""
    entries = []

    # Check if data is empty
    if data.empty:
        logging.warning("Data is empty. No signals can be generated.")
        return entries

    for i in range(1, len(data)):
        current = data.iloc[i]
        previous = data.iloc[i - 1]

        # Debugging statements
        logging.debug(f"Current row: {current}")
        logging.debug(f"Previous row: {previous}")

        # Ensure that 'Close', 'High', and 'Open' are present in the current and previous rows
        if all(col in current.index for col in ['Close', 'Open']) and 'High' in previous.index:
            atr = data['ATR'].iloc[i]

            # Compare scalar values
            if current['Close'].item() > previous['High'].item() and current['Open'].item() > previous['High'].item():
                entry_price = current['Open'].item()
                stop_loss = entry_price - atr * atr_multiplier
                take_profit = entry_price + atr * atr_multiplier * 2
                entries.append({
                    'pair': pair, 'date': current.name.strftime('%Y-%m-%d %H:%M:%S'),
                    'type': 'BUY', 'entry': entry_price, 'stop': stop_loss, 'tp': take_profit
                })
            elif current['Close'].item() < previous['Low'].item() and current['Open'].item() < previous['Low'].item():
                entry_price = current['Open'].item()
                stop_loss = entry_price + atr * atr_multiplier
                take_profit = entry_price - atr * atr_multiplier * 2
                entries.append({
                    'pair': pair, 'date': current.name.strftime('%Y-%m-%d %H:%M:%S'),
                    'type': 'SELL', 'entry': entry_price, 'stop': stop_loss, 'tp': take_profit
                })
        else:
            logging.warning("Current or previous row does not contain required columns.")

    return entries


# Streamlit UI
st.title("Indian Stock Trading Signals")

# Dropdown for selecting stocks
currency_pair = st.selectbox("Select Stock", indian_stocks)

if st.button("Get Signals"):
    data = fetch_data(currency_pair)
    if data is None:
        st.error(f"Error fetching data for {currency_pair}.")
    else:
        data = calculate_atr(data)
        entries = price_action_strategy(data.dropna(), currency_pair)
        if entries:
            for signal in entries:
                st.write(
                    f"{signal['date']}: {signal['type']} {signal['pair']} at {signal['entry']} (Stop: {signal['stop']}, TP: {signal['tp']})")
        else:
            st.write("No trade signals generated.")
