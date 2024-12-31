import streamlit as st
from utama import show_utama
from kelurahan import show_kelurahan

st.sidebar.image("ijo.png", width=100, use_container_width=True)
st.markdown("""
    <style>
    .stApp {
        background-color: #fff;
        font-family: 'Arial', sans-serif;
    }
    
    [data-testid="stHeader"] {
        background-color: #fff;
    }

     [data-testid="stSidebar"] {
       background-color: #C2FFC7;
        color: black;
        padding: 20px;
    }

    /* Teks pada sidebar */
    [data-testid="stSidebar"] * {
        color: black !important;
        font-size: 16px;
        margin-bottom: 5px;
       
    }

    .stSelectbox>div>div {
        background-color: #D3F1DF;
        border-radius: 5px;
    }
    
    .st.sidebar.image{
       width: 20px;
       height: 20px     
     }
    </style>
    """, unsafe_allow_html=True)


def main():
    st.title('Aplikasi Kelurahan Pancoranmas Depok')

    menu = ['Halaman Utama', 'Data Kecamatan']
    choice = st.sidebar.selectbox('Pilih Halaman', menu)

    if choice == 'Halaman Utama':
        show_utama()
    elif choice == 'Data Kecamatan':
        show_kelurahan()

if __name__ == "__main__":
    main()


