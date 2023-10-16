class ERPSistem:

    def __init__(self):
        self.gorevler = []

    def musteri_iliskileri(self):
        print("Müşteri İlişkileri Modülü")

    def satislar(self):
        print("Satışlar Modülü")

    def projeler(self):
        print("Projeler Modülü")

    def yardim_masasi(self):
        print("Yardım Masası Modülü")

    def satin_alma(self):
        print("Satın Alma Modülü")

    def stoklar(self):
        print("Stoklar Modülü")

    def uretim(self):
        print("Üretim Modülü")

    def lojistik(self):
        print("Lojistik Modülü")

    def finans(self):
        print("Finans Modülü")

    def insan_kaynaklari(self):
        print("İnsan Kaynakları Modülü")

    def ic_iletisim(self):
        print("İç İletişim Modülü")

    def bakim(self):
        print("Bakım Modülü")

    def sistem_ayarlari(self):
        print("Sistem Ayarları Modülü")

    def raporlama_araci(self):
        print("Raporlama Aracı Modülü")

    def baslat(self):
        while True:
            print("\n*** ERP Sistemi ***")
            print("1. Müşteri İlişkileri")
            print("2. Satışlar")
            print("3. Projeler")
            print("4. Yardım Masası")
            print("5. Satın Alma")
            print("6. Stoklar")
            print("7. Üretim")
            print("8. Lojistik")
            print("9. Finans")
            print("10. İnsan Kaynakları")
            print("11. İç İletişim")
            print("12. Bakım")
            print("13. Sistem Ayarları")
            print("14. Raporlama Aracı")
            print("15. Çıkış")

            secim = input("Bir seçenek belirtin (1-15): ")

            if secim == '1':
                self.musteri_iliskileri()
            elif secim == '2':
                self.satislar()
            elif secim == '3':
                self.projeler()
            elif secim == '4':
                self.yardim_masasi()
            elif secim == '5':
                self.satin_alma()
            elif secim == '6':
                self.stoklar()
            elif secim == '7':
                self.uretim()
            elif secim == '8':
                self.lojistik()
            elif secim == '9':
                self.finans()
            elif secim == '10':
                self.insan_kaynaklari()
            elif secim == '11':
                self.ic_iletisim()
            elif secim == '12':
                self.bakim()
            elif secim == '13':
                self.sistem_ayarlari()
            elif secim == '14':
                self.raporlama_araci()
            elif secim == '15':
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ERPSistem().baslat()