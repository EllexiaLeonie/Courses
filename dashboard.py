import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Muat data
hourly_data = pd.read_csv("data/hour.csv")
daily_data = pd.read_csv("data/day.csv")

# Judul
st.title('Dashboard Analisis Sewa Sepeda')

# Pertanyaan 2
st.header('Tren Jumlah Sewa Sepeda dari 2011 ke 2012')
# Hitung jumlah sewa sepeda per tahun
yearly_rentals = hourly_data.groupby('yr')['cnt'].sum()
# Membuat plot
fig, ax = plt.subplots()
ax.bar(yearly_rentals.index, yearly_rentals.values)
ax.set_xlabel('Year')
ax.set_ylabel('Total Rentals')
ax.set_title('Total Rentals per Year')
ax.set_xticks(yearly_rentals.index)
ax.set_xticklabels(['2011', '2012'])
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Pertanyaan 3
st.header('Jumlah Rata-Rata Penyewa Sepeda berdasarkan Musim')
# Hitung rata-rata penyewaan sepeda berdasarkan musim
seasonal_rentals = hourly_data.groupby('season')['cnt'].mean()
# Membuat plot
fig, ax = plt.subplots()
seasonal_rentals.plot(kind='bar', ax=ax, xlabel='Season', ylabel='Average Rentals', title='Average Rentals by Season')
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'], rotation=0)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Pertanyaan 4
st.header('Perbedaan Jumlah Rata-Rata Penyewa antara Akhir Pekan/ Hari Libur dan Hari Kerja')
# Plot jumlah sewa sepeda berdasarkan hari kerja
workday_rentals = hourly_data.groupby('workingday')['cnt'].mean()
# Membuat plot
fig, ax = plt.subplots()
workday_rentals.plot(kind='bar', ax=ax)
ax.set_xlabel('Working Day')
ax.set_ylabel('Average Rentals')
ax.set_title('Average Rentals by Working Day')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Weekend/Holiday', 'Workday'], rotation=0)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Pertanyaan 5
st.header('Distribusi Pola Penggunaan Sepeda Berdasarkan Bulan')
monthly_rentals = hourly_data.groupby('mnth')['cnt'].mean()
# Membuat plot
fig, ax = plt.subplots()
monthly_rentals.plot(kind='line', ax=ax, xlabel='Month', ylabel='Average Rentals', title='Average Rentals by Month', marker='o')
ax.set_xticks(range(1, 13))
ax.grid(True)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Pertanyaan 6
st.header('Distribusi Rata-Rata Penyewa berdasarkan Jam per Hari')
hourly_rentals = hourly_data.groupby('hr')['cnt'].mean()
# Membuat plot
fig, ax = plt.subplots()
hourly_rentals.plot(kind='line', ax=ax, xlabel='Hour', ylabel='Average Rentals', title='Average Rentals by Hour', marker='o')
ax.set_xticks(range(24))
ax.grid(True)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)

# Pertanyaan 7
st.header('Perbedaan Jumlah Rata-Rata Penyewa antara Hari Libur dan Hari Kerja')
# Plot jumlah sewa sepeda berdasarkan hari libur atau hari kerja
holiday_rentals = hourly_data.groupby('holiday')['cnt'].mean()
# Membuat plot
fig, ax = plt.subplots()
holiday_rentals.plot(kind='bar', ax=ax, xlabel='Holiday', ylabel='Average Rentals', title='Average Rentals by Holiday')
ax.set_xticks([0, 1])
ax.set_xticklabels(['Non-Holiday', 'Holiday'], rotation=0)
# Menampilkan plot menggunakan Streamlit
st.pyplot(fig)