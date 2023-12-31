import pdfplumber
from datetime import datetime
import re

def extract_text_from_coordinates(pdf_file, coordinates):
    with pdfplumber.open(pdf_file) as pdf:
        page = pdf.pages[0]  

        text_within_coordinates = ""
        for obj in page.extract_words():
            x, y = obj['x0'], obj['top']
            if (
                coordinates["left"] <= x <= coordinates["right"]
                and coordinates["top"] <= y <= coordinates["bottom"]
            ):
                ##checking if word is valid numbr
                try:
                    float_value = float(obj['text'])
                    text_within_coordinates += str(float_value) + ' '
                except ValueError:
                    text_within_coordinates += obj['text'] + ' '

    return text_within_coordinates.strip()

#left : X coordinate
#top  : Y coordinate
#right : width from GIMP
#bottom : height from
coordinates = {
    "left": 50,
    "top": 110,
    "right": 150,
    "bottom": 120,
}

pdf_file_path = "Fatura.pdf"

satici_adi = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":20,"right":150,"bottom":40})
split_index = satici_adi.rfind(" ")
satici_adi1 = satici_adi[:split_index]
satici_adi2 = satici_adi[split_index + 1:].split()
satici_adi2 = " ".join(satici_adi2)
satici_adres = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":40,"right":150,"bottom":70})
adress_parts = satici_adres.split(" ")
satici_adres1=" ".join(adress_parts[:4])
satici_adres2=" ".join(adress_parts[4:-3])
satici_adres3=" ".join(adress_parts[-3:])
satici_vkn_no = extract_text_from_coordinates(pdf_file_path,{"left":20,"top":120,"right":150,"bottom":130})
satici_vkn_no = int(float(satici_vkn_no))
satici_vergi_daire = extract_text_from_coordinates(pdf_file_path,{"left":50,"top":110,"right":150,"bottom":120})
alici_adi = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":230,"right":150,"bottom":240})
alici_adi1 = " ".join(alici_adi[:4])
alici_adi2 = " ".join(alici_adi[4:])
split_index1 = alici_adi.rfind(" ")
alici_adi11 = alici_adi[:split_index1]
alici_adi22 = alici_adi[split_index + 1:]
alici_adres = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":240,"right":150,"bottom":280})
adress_parts1=alici_adres.split(" ")
alici_adres1 = " ".join(adress_parts1[:2])
alici_adres2= " ".join(adress_parts1[2:5])
alici_adres3= " ".join(adress_parts1[5:])
alici_vkn_no = extract_text_from_coordinates(pdf_file_path,{"left":20,"top":290,"right":150,"bottom":300})
alici_vkn_no=int(float(alici_vkn_no))
alici_vergi_daire = extract_text_from_coordinates(pdf_file_path,{"left":50,"top":280,"right":150,"bottom":290})
fatura_tarihi =  extract_text_from_coordinates(pdf_file_path,{"left":430,"top":290,"right":500,"bottom":300})
fatura_tarihi_datetime = datetime.strptime(fatura_tarihi,"%d-%m-%Y")
formatted_fatura_tarihi = fatura_tarihi_datetime.strftime("%d/%m/%Y")
fatura_tarihi=formatted_fatura_tarihi
urun_cinsi = extract_text_from_coordinates(pdf_file_path,{"left":110,"top":350,"right":200,"bottom":400}) #BUĞDAY
urun_tipi = extract_text_from_coordinates(pdf_file_path,{"left":70,"top":350,"right":100,"bottom":400})   #İTHAL
urun_miktar =  extract_text_from_coordinates(pdf_file_path,{"left":200,"top":350,"right":260,"bottom":400})
urun_miktar= int(float(urun_miktar))
deneme1=extract_text_from_coordinates(pdf_file_path,{"left":300,"top":360,"right":320,"bottom":400})
parts=  deneme1.split('.')
result1 = parts[0] if len(parts) > 0 else deneme1
ettn_no=extract_text_from_coordinates(pdf_file_path,{"left":15,"top":300,"right":100,"bottom":340})
ettn_no_parts = ettn_no.split(":")
ettn_desired_part = ettn_no_parts[1].strip()
print(ettn_desired_part)
urun_fiyat = extract_text_from_coordinates(pdf_file_path,{"left":250,"top":350,"right":300,"bottom":400})
urun_fiyat1 = extract_text_from_coordinates(pdf_file_path,{"left":210,"top":350,"right":350,"bottom":400})
formatfiyat = urun_fiyat.split()
urun_fiyat = formatfiyat[1]
islem_tutari =  extract_text_from_coordinates(pdf_file_path,{"left":500,"top":350,"right":600,"bottom":400})
formattutari = islem_tutari.split()
islem_tutari = formattutari[1]
odenecek_tutar = extract_text_from_coordinates(pdf_file_path,{"left":500,"top":450,"right":600,"bottom":600})
formatodenecek = odenecek_tutar.split()
malhizmetdeneme=extract_text_from_coordinates(pdf_file_path,{"left":500,"top":400,"right":600,"bottom":600})
formatmalhizmetdeneme=malhizmetdeneme.split()
malhizmetdeneme=formatmalhizmetdeneme[2]
islem_tutar1=malhizmetdeneme
odenecek_tutar = formatodenecek[0]
hesaplanan_kdv = extract_text_from_coordinates(pdf_file_path,{"left":500,"top":300,"right":600,"bottom":700})
formathesaplanankdv = hesaplanan_kdv.split()
hesaplanan_kdv = formathesaplanankdv[11]
depo_semt = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":530,"right":600,"bottom":540})
formatdeposemt= depo_semt.split()
depo_semt = formatdeposemt[3]
teslim_yeri_depo_format1 =extract_text_from_coordinates(pdf_file_path,{"left":65,"top":540,"right":600,"bottom":550})
teslim_yeri_depo = teslim_yeri_depo_format1 +" " +depo_semt
counter="001"
urun_no=""
urun_kodu = {
    "BUĞDAY":"W","ARPA":"B","MISIR":"C","FINDIK":"F"
}
kod_gonder=""
if(urun_cinsi=="BUĞDAY") :
  kod_gonder = urun_kodu["BUĞDAY"]
elif(urun_cinsi=="ARPA"):
  kod_gonder = urun_kodu["ARPA"]
elif (urun_cinsi=="MİSİR") :
  kod_gonder=urun_kodu["MİSİR"]
elif(urun_cinsi=="FİNDİK"):
  kod_gonder=urun_kodu["FİNDİK"]
else :
  print("GECERSİZ KOD")
##test et
urun_no = kod_gonder + "-" + "B" + "-" + str(counter) + "-" + str(urun_miktar)

veriler1= {
    "satici_adi":satici_adi,"satici_adres":satici_adres,"satici_vkn_no":satici_vkn_no,"satici_vergi_daire":satici_vergi_daire,"odenecek_tutar":odenecek_tutar,
    "alici_adi":alici_adi,"alici_adres":alici_adres,"alici_vkn_no":alici_vkn_no,"alici_vergi_daire":alici_vergi_daire,"fatura_tarihi":fatura_tarihi,
    "urun_cinsi":urun_cinsi,"urun_tipi":urun_tipi,"urun_miktar":urun_miktar,"urun_fiyat":urun_fiyat,"islem_tutari":islem_tutari,"islem_tutari":odenecek_tutar,
    "hesaplanan_kdv":hesaplanan_kdv,"depo_semt":depo_semt,"teslim_yeri_depo":teslim_yeri_depo,"counter":counter,"urun_no":urun_no,"islem_tutar1":islem_tutar1,
    "satici_adi1":satici_adi1,"satici_adi2":satici_adi2,"satici_adres1":satici_adres1,"satici_adres2":satici_adres2,"satici_adres3":satici_adres3,"alici_adres1":alici_adres1,
    "alici_adres2":alici_adres2,"alici_adi1":alici_adi1,"alici_adi2":alici_adi2,"alici_adi11":alici_adi11,"alici_adi22":alici_adi22,"alici_adres3":alici_adres3,"result1":result1,"urun_fiyat1":urun_fiyat1,
    "ettn_no":ettn_desired_part,
}