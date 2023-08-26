import streamlit as st
import pandas as pd
import seaborn as sns

CSS = """
h1 {
    color: #a54b49;
},
body {
    color: #1d4878;
}
.stApp {
    background-image: url(https://a-static.besthdwallpaper.com/simple-minimalism-white-color-wallpaper-2880x1800-82612_8.jpg);
    background-size: cover;
}
"""

if st.checkbox('Inject CSS'):
    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

st.markdown("# JP's Currency Plots")
st.markdown('Chart: Base Rate **Euro**')

data = pd.read_csv('https://gist.githubusercontent.com/janduplessis883/e7b834c8293745ddc92b7a1fc57af9c0/raw/477a4e030a07e10bf8a96e562ef590d17605d99a/currency_rates.csv')

option = st.slider('Display no of rows',1,30,1)
st.write(data.tail(option))