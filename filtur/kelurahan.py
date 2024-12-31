import streamlit as st
import pandas as pd

# Simulasi data penduduk
penduduk_data = []

def show_kelurahan():
    st.header("Data kelurahan")

    menu_kelurahan = ['Input Data Penduduk', 'Pencarian Data Penduduk', 'Rekapan Data Penduduk', 'Penduduk Bansos']
    choice = st.selectbox('Pilih Fitur', menu_kelurahan)

    if choice == 'Input Data Penduduk':
        input_data_penduduk()
    elif choice == 'Pencarian Data Penduduk':
        cari_data_penduduk()
    elif choice == 'Rekapan Data Penduduk':
        rekapan_data_penduduk()
    elif choice == 'Penduduk Bansos':
        penduduk_bansos()



# fitur input
def input_data_penduduk():
    st.subheader("Input Data Penduduk")
    
    nama = st.text_input("Nama")
    nik = st.text_input("NIK")
    rt = st.text_input("RT")
    rw = st.text_input("RW")
    
    if st.button('Simpan'):
        penduduk_data.append({'Nama': nama, 'NIK': nik, 'RT': rt, 'RW': rw})
        st.success("Data berhasil disimpan")



# fitur pencarian
def cari_data_penduduk():
    st.subheader("Pencarian Data Penduduk")
    search_name = st.text_input("Masukkan nama lengkap untuk pencarian")
    
    if st.button('Cari'):
        # Mengubah nama yang dicari menjadi format huruf kecil agar pencarian tidak case-sensitive
        search_name_lower = search_name.lower()
        
        # Mencari penduduk yang namanya mengandung kata kunci pencarian
        found = [p for p in penduduk_data if search_name_lower in p['Nama'].lower()]
        
        if found:
            # Mengubah hasil menjadi DataFrame
            found_df = pd.DataFrame(found)
            
            # Mengatur index agar dimulai dari 1
            found_df.index = range(1, len(found_df) + 1)
            
            # Tampilkan tabel
            st.table(found_df)
        else:
            st.write("Data tidak ditemukan.")



# Fitur Rekapan
def rekapan_data_penduduk():
    st.subheader("Rekapan Data Penduduk")
    
    st.write("Jumlah Penduduk:", len(penduduk_data))
    if len(penduduk_data) > 0:
        # Menampilkan tabel data penduduk
        st.dataframe(penduduk_data)
# Menjalankan fungsi rekapan data penduduk
rekapan_data_penduduk()



# Fitur Bansos
def penduduk_bansos():
    st.subheader("Penduduk yang Mendapat Bansos")
    # Menampilkan dropdown untuk memilih RW
    rw_terpilih = st.selectbox("Pilih RW", options=["Semua RW", "1", "2", "3"])
    
    # Filter data berdasarkan pilihan RW
    if rw_terpilih == "Semua RW":
        data_yang_ditampilkan = penduduk_data
    else:
        data_yang_ditampilkan = [data for data in penduduk_data if data["RW"] == rw_terpilih]
    
    # Menampilkan jumlah penduduk yang dipilih
    st.write("Jumlah Penduduk:", len(data_yang_ditampilkan))
    
    # Jika ada data, tampilkan dalam tabel yang bisa diedit
    if len(data_yang_ditampilkan) > 0:
        # Menampilkan data dalam bentuk editor interaktif
        edited_data = st.data_editor(data_yang_ditampilkan, num_rows="dynamic", use_container_width=True)
        
        # Cek jika ada perubahan data
        if edited_data != data_yang_ditampilkan:
            st.write("Data berhasil diperbarui!")
            # Jika diperlukan, Anda bisa menambahkan kode untuk menyimpan data yang sudah diperbarui
    else:
        st.write("Tidak ada data penduduk untuk RW yang dipilih.")
    # Menganggap semua penduduk berhak mendapat bansos
    

