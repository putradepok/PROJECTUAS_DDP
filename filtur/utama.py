import streamlit as st

def show_utama():
    st.header("Selamat Datang di Kota Depok")

    # Menampilkan gambar Kota Depok (pastikan Anda memiliki gambar ini di direktori yang benar)
    st.image("depok.jpg", caption="Kota Depok", use_container_width=True)

    # Penjelasan tentang Kota Depok
    st.subheader("Tentang Kota Depok")
    st.write("""
        Kota Depok adalah salah satu kota yang terletak di Provinsi Jawa Barat, Indonesia. 
        Kota ini memiliki populasi yang terus berkembang dan dikenal sebagai pusat pendidikan dan teknologi, 
        dengan beberapa universitas terkemuka seperti Universitas Indonesia (UI) yang berlokasi di daerah Depok.

        Kota Depok memiliki berbagai fasilitas umum, seperti pusat perbelanjaan, rumah sakit, dan tempat hiburan,
        serta kaya akan budaya dan sejarah yang mencerminkan tradisi Jawa Barat dan modernitas perkotaan.

        Beberapa tempat menarik di Depok antara lain:
        - **Taman Wisata Alam Angke**: Tempat yang tepat untuk menikmati alam dan keindahan hutan mangrove.
        - **Universitas Indonesia (UI)**: Kampus besar yang menjadi pusat pendidikan di Depok.
        - **Margo City**: Salah satu pusat perbelanjaan besar di Depok.

        Kota Depok juga dikenal dengan kemajuan infrastrukturnya dan kontribusinya terhadap perekonomian Indonesia, 
        menjadikannya sebagai kota yang layak huni dan terus berkembang.
    """)

    # Jika Anda ingin menonjolkan bagian tertentu dalam teks, gunakan tanda kuning (highlight)
    st.markdown("""
        **Kota Depok** adalah kota yang sangat berkembang di Jawa Barat, dengan pusat pendidikan, teknologi, 
        dan hiburan. Salah satu highlight besar di kota ini adalah **Universitas Indonesia (UI)** yang terkenal.
    """, unsafe_allow_html=True)
