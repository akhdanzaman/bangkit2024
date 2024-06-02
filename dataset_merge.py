import pandas as pd

# Baca tiga sheet dari file Excel
excel_file = 'data\\input\\used_dataset\\merge.xlsx'  # Ganti dengan nama file Excel Anda
sheet1 = pd.read_excel(excel_file, sheet_name='anxiety')  # Ganti dengan nama sheet pertama
sheet2 = pd.read_excel(excel_file, sheet_name='depression')  # Ganti dengan nama sheet kedua
sheet3 = pd.read_excel(excel_file, sheet_name='lonely')  # Ganti dengan nama sheet ketiga

# Satukan tiga sheet menjadi satu DataFrame
combined_df = pd.concat([sheet1, sheet2, sheet3], ignore_index=True)

# Simpan DataFrame gabungan sebagai file CSV
combined_df.to_csv('merged_output.csv', index=False)
