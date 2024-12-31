import streamlit as st
import pandas as pd

def show_pendudukan():
    st.header("Data Penduduk")
   
    # Simulasi data penduduk
    penduduk = [{'No''Nama': 'John Doe', 'NIK': '123456789'}, {'No''Nama': 'Jane Smith', 'NIK': '987654321'}]
    
    st.write(penduduk)

