print("=== APLIKASI HITUNG HPP & SARAN JUALAN ===")

# 1. user input
modal = int(input("Masukkan total modal (Rp): "))
hpp_satuan = int(input("Masukkan HPP/biaya per 1 produk (Rp): "))
margin_persen = float(input("Masukkan target keuntungan (%): "))

# 2. Proses dengan Operator Aritmatika
jumlah_produk = modal // hpp_satuan #pembagian bulat (mencari jumlah unit)
sisa_modal = modal % hpp_satuan # Modulus (sisa uang modal yang tidak cukup beli 1 unit utuh)
tambahan_profit = hpp_satuan * (margin_persen / 100) # Perkalian & pembagian persentase
saran_harga_jual = hpp_satuan + tambahan_profit # Penjumlahan untuk harga jual

potensi_pendapatan = jumlah_produk * saran_harga_jual # Total kira kira omset

if margin_persen < 10:
    sistem = "Margin Kamu Terlalu Tipis , Awas Boncos Lhoo"
elif margin_persen <= 30:
    sistem = "Margin Lumayan Kalau Targetnya Pelajar"
else:
    sistem = "UNTUNG BESAR WAKK"

# 3. Output nya dari semua yang udah di masukin
print("\n" + "="*30)
print("HASIL REKOMENDASI SISTEM:")
print(f"• Maksimal produk yang bisa dibuat: {jumlah_produk} pcs")
print(f"• Sisa modal (Modulus): Rp {sisa_modal}")
print(f"• Saran harga jual per unit: Rp {saran_harga_jual:.0f}")
print(f"• Potensi total pendapatan: Rp {potensi_pendapatan:.0f}")
print(f"• Analisis Pasar: {sistem}")
print("="*30)
