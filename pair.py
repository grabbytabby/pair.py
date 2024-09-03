import streamlit as st
import time

# List of cryptocurrency exchanges
exchanges = [
    "Gatecoin", "Gemini", "HitBTC", "Huobi", "itBit", "Kraken", "LakeBTC", 
    "LocalBitcoins", "MonetaGo", "OKCoin", "Poloniex", "Yacuna", "Yunbi", "Yobit", 
    "Korbit", "BitBay", "BTCMarkets", "QuadrigaCX", "CoinCheck", "BitSquare", 
    "Vaultoro", "MercadoBitcoin", "Unocoin", "Bitso", "BTCXIndia", "Paymium", 
    "TheRockTrading", "bitFlyer", "Quoine", "Luno", "EtherDelta", "Liqui", 
    "bitFlyerFX", "BitMarket", "LiveCoin", "Coinone", "Tidex", "Bleutrade", 
    "EthexIndia"
]

# List of artists for pairing
artists = [
    "Threat", "Tlee Batez", "King Tee", "Alkaholiks", "Dogg Pound", "Outlawz", "IInd 2 None", 
    "Sickwidit", "Chilly Chill", "The Lynch Mob", "Geto Boys", "Pharcyde", "Wu-Tang Clan", 
    "Nas", "AZ", "Goodie Mob", "Boss", "MC Hammer", "Spice 1", "Oaktown 357", "Money B", 
    "Digital Underground", "Battle Cat", "Eastsiders", "Kokane", "Above the Law", "Suga Free", 
    "Juvenile", "BG", "Mannie Fresh", "Bone Thugs-N-Harmony"
]

# Set up the Streamlit app title and description
st.title("Cryptocurrency Exchange Ticker and Artist Pairing")
st.markdown("Monitor cryptocurrency exchanges and set up future pairings with artists.")

# Container for the ticker
ticker_container = st.empty()

# Slider to control the speed of the ticker
speed = st.slider("Speed of Ticker", min_value=0.1, max_value=1.0, value=0.2, step=0.1)

# Sidebar for artist selection
st.sidebar.header("Select Artist for Pairing")
selected_artist = st.sidebar.selectbox("Choose an Artist:", artists)
st.sidebar.write(f"Selected Artist: **{selected_artist}**")

st.sidebar.markdown("### Future Pairings")
st.sidebar.write("Cryptocurrency exchanges will be paired with the selected artist.")

# Display selected artist pairing
pairing_container = st.sidebar.empty()
pairing_container.write(f"Pairing: **{selected_artist}** with exchanges")

# Continuous loop for ticker display
while True:
    for exchange in exchanges:
        # Update the ticker display
        ticker_container.markdown(f"<h2 style='color: green;'>{exchange}</h2>", unsafe_allow_html=True)
        time.sleep(speed)
        # Update pairing display
        pairing_container.write(f"Pairing: **{selected_artist}** with {exchange}")
