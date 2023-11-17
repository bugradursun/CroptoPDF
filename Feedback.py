from PyPDF2 import PdfReader
import re
from datetime import datetime
from coordinatedene import extract_text_from_coordinates

##BURADA KELİMELERİ İSTENİLEN FORMATA CEVİRİP,BİR DICTIONARYDE TUTUYORUM.SONRASINDA HTML'DEKİ OBJELERE YERLESTİRİYORUM.
##PYPDF => EXTRACT TEXTS => STORE THEM IN AN ARRAY => SPLIT THE ARRAY(ALREADY ONE ITEM ARRAY CONSISTS ALL WORDS) => DO SPLIT OPERATIONS AND STORE THEM


reader = PdfReader("Fatura.pdf")
page = reader.pages[0]
kelimeler_array = []
kelimeler = page.extract_text()
#print(kelimeler)
kelimeler_encoded = kelimeler.encode("utf-8","ignore")
kelimeler_decoded = kelimeler_encoded.decode("utf-8", "ignore")
kelimeler_array.append(kelimeler_decoded)
words = kelimeler_array[0].split()
print(words)

##for i in range (125,150) : 
##  print(words[i])
##


alici_adi = words[1:5]
alici_adi = ' '.join(alici_adi)
alici_adres = words[5:8]
alici_adres = ' '.join(alici_adres)
alici_adres1 = words[8:12]
alici_adres1=''.join(alici_adres1)
alici_adres1 = alici_adres1.replace('/','/')
alici_adres1=alici_adres1.replace('BÜYÜKDERE', ' BÜYÜKDERE ')
alici_adres2= words[12:14]
alici_adres2 = ''.join(alici_adres2)
alici_vergi_daire = words[16:19]
alici_vergi_daire = ' '.join(alici_vergi_daire)
alici_vkn_no = words[20]
alici_vkn_no = alici_vkn_no[0:10]
alici_fatura_no = words[30]
alici_ozellestirme_no = words[22]
alici_fatura_tarihi = words[33] #FATURA TARİHİ ALANI BU
teslim_yeri = words[51]
teslim_yeri_depo = words[57:60]
teslim_yeri_depo = ' '.join(teslim_yeri_depo)
satici_adi = words[63:67]
satici_adi = ' '.join(word for word in satici_adi if not word.startswith('TL.'))
satici_adres = words[67:81]
satici_adres = ' '.join(satici_adres)
lines = satici_adres.split()
line1 = " ".join(lines[:5])
line2 = " ".join(lines[5:12])
line3 = " ".join(lines[12:])
line4=" ".join(lines[14:])
##satici_adres1= words[75:81]
##satici_adres1 = ''.join(satici_adres1)
##print("ilkcumle:",satici_adres)
##print("ikinci cumle:",satici_adres1)
satici_vergi_daire = words[94:98]
satici_vergi_daire = ' '.join(satici_vergi_daire)
satici_vkn_no = words[99]
urun_kodu_grup = words[119]
mal_hizmet_tutari=words[129]
islem_tutari = words[155]
urun_turu = words[120]
urun_turu = urun_turu[0:6]
urun_cins = words[120]
urun_cins = urun_cins[6:] ##BUĞDAYİTHAL => İTHAL
urun_miktar = words[122]
hesaplanan_kdv = words[127]
urun_birim_fiyat = words[124]
depo_semt = words[51]
islem_no_counter=1
counter=1
urun_no=""
##URUN KODU + B + {countre} + {urun_miktar}
urun_kodu = {
    "BUĞDAY":"W",
    "ARPA":"B",
    "MİSİR":"C",
    "FİNDİK":"F"
}
kod_gonder=""
if(urun_turu=="BUĞDAY") :
    kod_gonder = urun_kodu["BUĞDAY"]
elif(urun_turu=="ARPA"):
    kod_gonder = urun_kodu["ARPA"]
elif (urun_turu=="MİSİR") :
    kod_gonder=urun_kodu["MİSİR"]
elif(urun_turu=="FİNDİK"):
    kod_gonder=urun_kodu["FİNDİK"]
else :
    print("GECERSİZ KOD")

urun_no = kod_gonder +"-" +  "B" + "-" +  str(counter) +"-" +str(urun_miktar)

today_date = datetime.today().strftime("%d %b, %Y") ##ikinci tarih kismi icin kullanilabilir!
today_month = datetime.today().strftime("%B")


extractVeriler = {
  "alici_adi": alici_adi,
  "alici_adres": alici_adres,
  "alici_vergi_daire": alici_vergi_daire,
  "alici_vkn_no": alici_vkn_no,
  "alici_fatura_no": alici_fatura_no,
  "line1":line1,
  "line2":line2,
  "line3":line3,
  "line4":line4,
  "alici_ozellestirme_no": alici_ozellestirme_no,
  "alici_fatura_tarihi": alici_fatura_tarihi,
  "teslim_yeri": teslim_yeri,
  "teslim_yeri_depo": teslim_yeri_depo,
  "satici_adi": satici_adi,
  "satici_adres": satici_adres,
  "satici_vergi_daire": satici_vergi_daire,
  "satici_vkn_no": satici_vkn_no,
  "urun_no" : urun_no,
  "urun_kodu_grup": urun_kodu_grup,
  "mal_hizmet_tutari":mal_hizmet_tutari,
  "urun_cins": urun_cins,
  "urun_miktar": urun_miktar,
  "urun_birim_fiyat": urun_birim_fiyat,
  "duzenleme_tarihi" : today_date,
  "islem_tutari" : islem_tutari,
  "hesaplanan_kdv" : hesaplanan_kdv,
  "islem_no_counter" : islem_no_counter,
  "counter" : counter,
  "depo_semt" : depo_semt,
  "urun_turu" : urun_turu
}



