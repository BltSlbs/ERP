class ERPSistem:

    def __init__(self):
        self.gorevler = []

    def gorevlerim(self):
        while True:
            print("\n*** Görevlerim Modülü ***")
            print("1. Hızlı Görev Ekleme")
            print("2. Haber Akışı")
            print("3. Genel Görevler")
            print("4. Görev Yönetimi")
            print("5. Ajandam")
            print("6. Bakım Ve Yardım Masası Görevleri")
            print("7. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-7): ")
            break

    def musteri_iliskileri(self):
        while True:
            print("\n*** Müşteri İlişkileri Modülü ***")
            print("1. Yeni Fırsat Tanımlama")
            print("2. Yeni İhale")
            print("3. Potansiyel Müşteriler")
            print("4. Müşteri Listesi")
            print("5. Kontaklar")
            print("6. Fırsat Yönetimi")
            print("7. İhale/Özel Teklif Yönetimi")
            print("8. Fuar ve Kampanyalar")
            print("9. İş Ortakları")
            print("10. Sözleşmeler")
            print("11. Müşteri İstek ve Şikayetleri")
            print("12. Raporlama Aracı")
            print("13. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-13): ")
            break

    def satislar(self):
        while True:
            print("\n*** Satışlar Modülü ***")
            print("1. Yeni Teklif Oluşturma")
            print("2. Yeni Sipariş Oluşturma")
            print("3. Müşteri Listesi")
            print("4. Teklif Yönetimi")
            print("5. Sipariş Yönetimi")
            print("6. İhracat Beyannameleri")
            print("7. Raporlama Aracı")
            print("8. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-8): ")
            break

    def projeler(self):
        while True:
            print("\n*** Projeler Modülü ***")
            print("1. Aktif Proje Listesi")
            print("2. Tüm Projeler Listesi")
            print("3. Harcamalar")
            print("4. Puantaj Listesi")
            print("5. Risk Yönetimi")
            print("6. Proje Havuzu")
            print("7. Kurum İçi İyileştirme Projeleri")
            print("8. Tamamlanmış Kurum İçi İyileştirmeler")
            print("9. Raporlama Aracı")
            print("10. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-10): ")
            break

    def yardim_masasi(self):
        while True:
            print("\n*** Yardım Masası Modülü ***")
            print("1. Aylık Envanter Kontrolü")
            print("2. Müşteri Envanter Listesi")
            print("3. Aktif Servis Planı")
            print("4. Kapanmış Servis Planı")
            print("5. Servis Ekibi")
            print("6. Problemler ve Çözümleri")
            print("7. Müşteri İstek ve Şikayetleri")
            print("8. Raporlama Aracı")
            print("9. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-9): ")
            break

    def satin_alma(self):
        while True:
            print("\n*** Satın Alma Modülü ***")
            print("1. Yeni Talep Oluştur")
            print("2. Yeni Sipariş Oluşturma")
            print("3. Talep Yönetimi")
            print("4. Teklif Yönetimi")
            print("5. Sipariş Yönetimi")
            print("6. Tedarikçi Listesi")
            print("7. Tedarikçi Değerlendirme")
            print("8. İthalat İşlemleri")
            print("9. Satın Alma Sözleşmeleri")
            print("10. Teslimat Yönetimi")
            print("11. Envanter Yönetimi")
            print("12. Kategori Yönetimi")
            print("13. Raporlama Aracı")
            print("14. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-14): ")
            break

    def stoklar(self):
        while True:
            print("\n*** Stoklar Modülü ***")
            print("1. Eldeki Stok")
            print("2. Stok Malzemeleri")
            print("3. Kategori Yönetimi")
            print("4. Ürün Listesi")
            print("5. Stok Barkodu Oluşturma")
            print("6. Stok Hareketleri")
            print("7. Malzeme İhtiyaç Planları")
            print("8. Malzeme İstek Fişleri")
            print("9. Müşteri Malzeme Teslim Alma Listesi")
            print("10. Taşeron Malzeme Teslim Listesi")
            print("11. Sipariş Listesi")
            print("12. Paket Listesi")
            print("13. Sarf Malzeme Listesi")
            print("14. Stok Transferi")
            print("15. Raporlama Aracı")
            print("16. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-16): ")
            break

    def uretim(self):
        while True:
            print("\n*** Üretim Modülü ***")
            print("1. Yeni Üretim Planı Oluştur")
            print("2. Ürün Ağaçları")
            print("3. Ürün Konfigürasyonu")
            print("4. Onaylanmış Sipariş Listesi")
            print("5. Üretim Planları")
            print("6. İş Emirleri")
            print("7. Kesim İş Emirleri")
            print("8. Proses İş Emirleri")
            print("9. Malzeme İhtiyaç Planları")
            print("10. Fason Yönetimi")
            print("11. İş Gücü Planlama")
            print("12. MİP Ayarları")
            print("13. Ürün Üretim Talimatları")
            print("14. Toplam Ekipman Etkinliği (OEE)")
            print("15. Raporlama Aracı")
            print("16. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-16): ")
            break

    def lojistik(self):
        while True:
            print("\n*** Lojistik Modülü ***")
            print("1. Sevkiyat Yönetimi")
            print("2. Sevkiyat Takvimi")
            print("3. Aktif Servis / Sevkiyat Planı")
            print("4. Kapanmış Servis / Sevkiyat Planı")
            print("5. Servis Ekibi")
            print("6. Raporlama Aracı")
            print("7. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-7): ")
            break

    def finans(self):
        while True:
            print("\n*** Finans Modülü ***")
            print("1. Yeni Tahsilat")
            print("2. Yeni Ödeme")
            print("3. Cari Hesaplar")
            print("4. Alacaklar Hesabı")
            print("5. Borçlar Hesabı")
            print("6. Muhasebe Defter ve Fişleri")
            print("7. Banka İşlemleri")
            print("8. Demirbaş Yönetimi")
            print("9. Raporlama Aracı")
            print("10. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-10): ")
            break

    def insan_kaynaklari(self):
        while True:
            print("\n*** İnsan Kaynakları Modülü ***")
            print("1. Yeni Personel Tanımlama")
            print("2. Personel Listesi")
            print("3. Yetki Listesi")
            print("4. Organizasyon Listesi")
            print("5. Raporlama Aracı")
            print("6. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-6): ")
            break

    def ic_iletisim(self):
        while True:
            print("\n*** İç İletişim Modülü ***")
            print("1. Beni Arayanlar")
            print("2. Tüm Aramalar")
            print("3. Ziyaretçilerim")
            print("4. Ziyaretçi Kayıt")
            print("5. Toplantı Tutanağı")
            print("6. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-6): ")
            break

    def bakim(self):
        while True:
            print("\n*** Bakım Modülü ***")
            print("1. Yıllık Bakım Planı")
            print("2. Aktif Arıza Kayıtları")
            print("3. Pasif Arıza Kayıtları")
            print("4. Makine / Teçhizat Listesi")
            print("5. Ölçme ve İzleme Cihazları Listesi")
            print("6. Departman İstek ve Şikayetleri")
            print("7. Raporlama Aracı")
            print("8. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-8): ")
            break

    def sistem_ayarlari(self):
        while True:
            print("\n*** Sistem Ayarları Modülü ***")
            print("1. Kurum Ayarları")
            print("2. Finans Ayarları")
            print("3. Doküman Yönetimi Ayarları")
            print("4. İç İletişim Ayarları")
            print("5. Müşteri İlişkileri Ayarları")
            print("6. Satış Yönetimi Ayarları")
            print("7. Proje Yönetimi Ayarları")
            print("8. Satın Alma Yönetimi Ayarları")
            print("9. Stok Yönetimi Ayarları")
            print("10. Üretim Yönetimi Ayarları")
            print("11. İnsan Kaynakları Yönetimi Ayarları")
            print("12. Pdks Ayarları")
            print("13. Ana Menüye Dön")

            secim = input("Bir seçenek belirtin (1-13): ")
            break

    def raporlama_araci(self):
        print("Raporlama Aracı Modülü")
        print("Bir rapor oluşturuluyor...")
        

    def baslat(self):
        while True:
            print("\n*** ERP Sistemi ***")
            print("1. Görevlerim")
            print("2. Müşteri İlişkileri")
            print("3. Satışlar")
            print("4. Projeler")
            print("5. Yardım Masası")
            print("6. Satın Alma")
            print("7. Stoklar")
            print("8. Üretim")
            print("9. Lojistik")
            print("10. Finans")
            print("11. İnsan Kaynakları")
            print("12. İç İletişim")
            print("13. Bakım")
            print("14. Sistem Ayarları")
            print("15. Raporlama Aracı")
            print("16. Çıkış")

            secim = input("Bir seçenek belirtin (1-16): ")

            if secim == '1':
                self.gorevlerim()
            elif secim == '2':
                self.musteri_iliskileri()
            elif secim == '3':
                self.satislar()
            elif secim == '4':
                self.projeler()
            elif secim == '5':
                self.yardim_masasi()
            elif secim == '6':
                self.satin_alma()
            elif secim == '7':
                self.stoklar()
            elif secim == '8':
                self.uretim()
            elif secim == '9':
                self.lojistik()
            elif secim == '10':
                self.finans()
            elif secim == '11':
                self.insan_kaynaklari()
            elif secim == '12':
                self.ic_iletisim()
            elif secim == '13':
                self.bakim()
            elif secim == '14':
                self.sistem_ayarlari()
            elif secim == '15':
                self.raporlama_araci()
            elif secim == '16':
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ERPSistem().baslat()