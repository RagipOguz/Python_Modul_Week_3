gorevler = []
sira_sayaci = 1

# Görev Ekleme İşlevi
def gorev_ekle(gorev_adi):
    global sira_sayaci
    gorev = {
        'Sira Numarasi': sira_sayaci,
        'Görev Adi': gorev_adi,
        'Durum': 'Bekliyor'
    }
    gorevler.append(gorev)
    print(f"Görev eklendi: {gorev_adi}")
    sira_sayaci += 1

# Görev Tamamlama İşlevi
def gorev_tamamla(sira_numarasi):
    for gorev in gorevler:
        if gorev['Sira Numarasi'] == sira_numarasi:
            gorev['Durum'] = 'Tamamlandi'
            print(f"Görev tamamlandi: {gorev['Görev Adi']}")
            return
    print("Geçersiz sira numarasi")

# Görev Silme İşlevi
def gorev_sil(sira_numarasi):
    global gorevler
    yeni_gorevler = [gorev for gorev in gorevler if gorev['Sira Numarasi'] != sira_numarasi]
    if len(yeni_gorevler) < len(gorevler):
        gorevler = yeni_gorevler
        print(f"Görev silindi: {sira_numarasi}")
    else:
        print("Geçersiz sira numarasi.")

# Tamamlanan Görevleri Listeleme
def tamamlanan_gorevleri_listele():
    print("Tamamlanan Görevler:")
    for gorev in gorevler:
        if gorev['Durum'] == 'Tamamlandi':
            print(f"{gorev['Sira Numarasi']}: {gorev['Görev Adi']}")

# Tüm Görevleri Listeleme
def tum_gorevleri_listele():
    print("Tüm Görevler:")
    for gorev in gorevler:
        print(f"{gorev['Sira Numarasi']}: {gorev['Görev Adi']} - Durum: {gorev['Durum']}")

# Ana Döngü
def ana_menu():
    while True:
        print("\nGörev Yöneticisi Uygulamasi")
        print("1. Yeni Görev Ekle")
        print("2. Görevi Tamamla")
        print("3. Görevi Sil")
        print("4. Tamamlanan Görevleri Listele")
        print("5. Tüm Görevleri Listele")
        print("6. Cikis")
        secim = input("Seçiminizi yapin: ")

        if secim == '1':
            gorev_adi = input("Görev adini girin: ")
            gorev_ekle(gorev_adi)
        elif secim == '2':
            try:
                sira_numarasi = int(input("Tamamlanacak görevin sira numarasini girin: "))
                gorev_tamamla(sira_numarasi)
            except ValueError:
                print("Lütfen geçerli bir sayi girin.")
        elif secim == '3':
            try:
                sira_numarasi = int(input("Silinecek görevin sira numarasini girin: "))
                gorev_sil(sira_numarasi)
            except ValueError:
                print("Lütfen geçerli bir sayi girin.")
        elif secim == '4':
            tamamlanan_gorevleri_listele()
        elif secim == '5':
            tum_gorevleri_listele()
        elif secim == '6':
            print("Cikis yapiliyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

ana_menu()
