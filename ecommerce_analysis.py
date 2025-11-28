# Import Libraries & Setup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Mengatur gaya visualisasi
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Data Loading
spreadsheet_url = "https://docs.google.com/spreadsheets/d/1dDczkp5SRp6IMNpKxiak_4q0S5qrOSILIyKzp-2I9ZE/export?format=csv&gid=1307725687"
df = pd.read_csv(spreadsheet_url)

# Data Cleaning
df["event_timestamp"] = pd.to_datetime(df["event_timestamp"]) # Mengubah string ke datetime
df["date"] = df["event_timestamp"].dt.date # Membuat kolom Tanggal
df['month_name'] = df['event_timestamp'].dt.month_name() # Membuat kolom Bulan
df['hour'] = df['event_timestamp'].dt.hour # Membuat kolom Jam
df['day_of_week'] = df['event_timestamp'].dt.day_name() # Membuat kolom Hari
df["channel"] = df["channel"].fillna("organic") # Mengisi channel kosong dengan 'organic' (Asumsi direct traffic)

# ANALISIS


# OBJECTIVE 1: FOKUS PASAR (User Aktif per Negara di Q2 2025)

q2_months = ['April', 'May', 'June'] # Filter Data khusus Q2 (April, Mei, Juni)
df_q2 = df[df['month_name'].isin(q2_months)]

top_country = df_q2.groupby('country')['user_id'].nunique().sort_values(ascending=False) # Menghitung Unique User per Negara & Urutkan

# Visualisasi 1 (Bar Chart)
plt.figure(figsize=(10, 6))
ax = sns.barplot(x=top_country.index, y=top_country.values, color='#4c72b0')

for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}',
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 9),
                textcoords='offset points') # Menambahkan Label

plt.title('Active Users per Country (Q2 2025)', fontsize=14)
plt.xlabel('Country')
plt.ylabel('Unique Users')
sns.despine() # Menghilangkan border atas/kanan agar bersih
plt.tight_layout()
plt.show()


# OBJECTIVE 2: TREN PERTUMBUHAN (User Aktif Bulanan per Channel)

# Pivot Table untuk mengubah data menjadi format Time-Series
channel_trend = df.pivot_table(
    index='month_name',
    columns='channel',
    values='user_id',
    aggfunc='nunique' # Menghitung user unik
)

months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']
channel_trend = channel_trend.reindex(months_order).dropna(how='all') # Mengurutkan bulan secara kronologis (bukan alfabetis)

# Visualisasi 2 (Line Chart)
plt.figure(figsize=(14, 7))
sns.lineplot(data=channel_trend, marker='o', dashes=False, linewidth=2.5)

plt.title('Monthly User Trend by Channel', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Unique Users')
plt.legend(title='Channel', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y', linestyle='--', alpha=0.7) # Grid hanya horizontal
plt.tight_layout()
plt.show()

# OBJECTIVE 3: PREFERENSI PERANGKAT (Mobile vs Desktop)

users_per_device = df.groupby('device')['user_id'].nunique().sort_values(ascending=False) # Menghitung Unique User per Device

# Visualisasi 3 (Horizontal Bar Chart)
plt.figure(figsize=(10, 6))
ax_device = sns.barplot(x=users_per_device.values, y=users_per_device.index, color='#3274A1')

for p in ax_device.patches:
    width = p.get_width()
    ax_device.annotate(f'{int(width)}',
                       (width, p.get_y() + p.get_height() / 2),
                       ha='left', va='center', xytext=(8, 0),
                       textcoords='offset points', fontsize=11) # Menambahkan Label Angka

plt.title('Device Usage Overview (User Preference)', fontsize=14)
plt.xlabel('Number of Users')
plt.ylabel('Device')
sns.despine()
plt.tight_layout()
plt.show()


# OBJECTIVE 4: AKTIVITAS PUNCAK (Heatmap Hari & Jam)

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True) # Mengatur urutan hari (Senin -> Minggu)
activity_matrix = df.groupby(['day_of_week', 'hour'])['user_id'].nunique().unstack(fill_value=0) # Mengubah bentuk data (Baris=Hari, Kolom=Jam)

# Visualisasi 4 (Heatmap)
plt.figure(figsize=(12, 6))
sns.heatmap(activity_matrix, cmap='Blues', fmt='d', linewidths=.5, cbar_kws={'label': 'Unique Users'})

plt.title('User Activity Heatmap: Days vs Hours', fontsize=14)
plt.xlabel('Hour of Day (0-23)')
plt.ylabel('Day of Week')
plt.tight_layout()
plt.show()


# OBJECTIVE 5: EFEKTIVITAS FITUR (Konversi Search ke Add-to-Cart)

search_data = df[df['event_type'] == 'search'][['user_id', 'date']].drop_duplicates() # Isolasi User yang melakukan SEARCH
atc_data = df[df['event_type'] == 'add_to_cart'][['user_id', 'date']].drop_duplicates() # Isolasi User yang melakukan ADD TO CART
converted_data = pd.merge(search_data, atc_data, on=['user_id', 'date'], how='inner') # Terapkan Logika "Hari yang Sama"

# Perhitungan Persentase Konversi
total_searchers = len(search_data)
total_converted = len(converted_data)
conversion_rate = (total_converted / total_searchers) * 100

print(f"Total User yang Search: {total_searchers}")
print(f"Total User Konversi (Hari Sama): {total_converted}")
print(f"Conversion Rate: {conversion_rate:.2f}%")
