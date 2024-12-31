import streamlit as st

def show_rt():
    st.header("Data RT")

    rt_data = [{'Nama': 'John Doe', 'NIK': '123456789', 'Mushola': 'Mushola Al-Falah'}, 
               {'Nama': 'Jane Smith', 'NIK': '987654321', 'Mushola': 'Mushola An-Nur'}]

    st.write(rt_data)
