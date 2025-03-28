import streamlit as st
import json

with open("quran.json", "r", encoding="utf-8") as file:
    quran_data = json.load(file)

st.markdown("""
    <style>
        .main {background-color: #3D3B40; color: #E0AFA0;}
        h1 {text-align: center; color: #D8C3A5;}
    </style>
""", unsafe_allow_html=True)

st.title("The Majestic Quran")

for surah in quran_data:
    for ayah in surah['verses']:
        st.write(ayah['text'])
