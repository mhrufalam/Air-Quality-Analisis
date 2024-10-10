# Import semua library yang digunakan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV dari database Github
df5 = pd.read_csv('https://raw.githubusercontent.com/mhrufalam/Database_Dicoding_Projek/refs/heads/main/data_polutan_df5.csv')
data_korelasi = pd.read_csv('https://raw.githubusercontent.com/mhrufalam/Database_Dicoding_Projek/refs/heads/main/correlation_TEMP_O3.csv')

# Membuat kolom baru berisi lokasi
df5['lokasi'] = 'Guanyuan'

# Mengganti format tahun agar menjadi DateTime
df5['year'] = df5['year'].astype(str)
df5['datetime'] = pd.to_datetime(df5['year']) 

# Jenis Analisis
jenis_analisis_list = ['Tren Polutan', 'Korelasi']


# Title aplikasi
st.title("Analisis Data Kualitas Udara")

# Sidebar untuk memilih jenis analisis
jenis_analisis = st.sidebar.selectbox("Pilih Jenis Analisis", jenis_analisis_list)

# Jika user memilih Tren Polutan
if jenis_analisis == 'Tren Polutan':
    st.write(f"Data Tren Polutan untuk Guanyuan. Pengguna dapat memilih zat polutan yang ingin ditampilkan")
    
    # Pilih parameter polutan
    parameter = st.selectbox("Pilih Parameter:", ["NO2", "PM10", "PM2.5", "SO2", "CO"])
    
    # Menampilkan tren polutan per tahun
    st.subheader(f"Tren {parameter} Per Tahun")
    plt.figure(figsize=(10, 5))
    plt.plot(df5['year'], df5[parameter], marker='o')
    plt.title(f'Tren {parameter} Per Tahun di Guanyuan')
    plt.xlabel('Tahun')
    plt.ylabel(f'Konsentrasi {parameter}')
    st.pyplot(plt)

    # Hasil Analisis
    st.write(f'Kadar rata-rata polutan di daerah Guanyuan mengalami peningkatan dari tahun 2013 - 2014. Lalu kadarnya turun hingga 2016. Setelah tahun 2016, kadar polutan kembali naik dengan sangat curam. Hal ini menyebabkan kadar polutan lain yang memiliki tren yang sama. Curah hujan yang menurun pada waktu 2016 - 2017 menjadi salah satu alasan mengapa kadar polutan meningkat di waktu tersebut.')

    # Menampilkan tren RAIN per tahun
    st.subheader(f"Tren RAIN Per Tahun")
    plt.figure(figsize=(10, 5))
    plt.plot(df5['year'], df5['RAIN'], marker='o')
    plt.title(f'Tren RAIN Per Tahun di Guanyuan')
    plt.xlabel('Tahun')
    plt.ylabel(f'Tingkat RAIN')
    st.pyplot(plt)

# Jika user memilih Korelasi
elif jenis_analisis == 'Korelasi':
    st.write(f"Korelasi TEMP dan O3. Digunakan untuk melihat keterkaitan antara TEMP dan O3.")
    
    # Menampilkan korelasi
    plt.figure(figsize=(10, 5))
    plt.bar(x=data_korelasi["DataFrame"], height=data_korelasi["Korelasi"])
    plt.title("Korelasi Temperatur dan Kadar O3", loc="center", fontsize=20)
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Hasil Analisis
    st.write(f"TEMP dan O3 memiliki korelasi karena nilai korelasi positif sehingga memiliki keterkaitan antara satu sama lain. Hal ini dikarenakan ketika suhu menurun, terutama saat musim dingin, produksi ozon akan berkurang karena kurangnya sinar UV. Melalui contoh data yang diambil dari daerah Changping, ketika suhu meningkat maka kadar O3 juga akan meningkat, sedangkan ketika suhu menurun kadar O3 juga ikut menurun. Sehingga terlihat korelasi antara TEMP dan O3.")