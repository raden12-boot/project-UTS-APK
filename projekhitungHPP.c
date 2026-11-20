#include <stdio.h>

int main() {

    int modal;
    int hpp;
    float margin;

    printf("=== Selamat Datang Di Sistem Saran Jual ===");
    printf("\nMasukan Modal Yang Kamu Punyai Sekarang = ");
    scanf ("%d", &modal);

    printf("Masukkan HPP/biaya per 1 produk (Rp): ");
    scanf ("%d", &hpp);    
    
    printf("Masukkan target keuntungan (%): ");
    scanf ("%f", &margin);

    int jumlah_produk = modal / hpp;
    int sisa_modal = modal % hpp;
    float profit = hpp * (margin / 100);
    float rekomendasi_harga = hpp + profit;
    float potensi_pendapatan = jumlah_produk * rekomendasi_harga;


    printf("==============================\n");
    printf("HASIL REKOMENDASI\n");
    printf("Maksimal Produk Yang Bisa Di Produksi = %d\n" , jumlah_produk);
    printf("Sisa Modal = %d\n" , sisa_modal);
    printf("Saran Harga Jual Per 1 Pcs = %.0f\n" , rekomendasi_harga);
    printf("Potensi Pendapatan = %.0f\n" , potensi_pendapatan);

    if (margin <= 10){
        printf("SISTEM ALERT : Margin nya terlalu tipis, awas boncos\n");
    } else if (margin <= 15){
        printf("SISTEM ALERT : Margin nya lumayan kalau targetnya pelajar\n");
    } else{
        printf("SISTEM INFO : GOKIL\n");
    }

    printf("==============================");

  
    return 0;
}