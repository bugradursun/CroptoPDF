import pdfplumber

def extract_text_from_coordinates(pdf_file, coordinates):
    with pdfplumber.open(pdf_file) as pdf:
        page = pdf.pages[0]  # Assuming you want to extract text from the first page

        text_within_coordinates = ""
        for obj in page.extract_words():
            x, y = obj['x0'], obj['top']
            if (
                coordinates["left"] <= x <= coordinates["right"]
                and coordinates["top"] <= y <= coordinates["bottom"]
            ):
                # Check if the word is a valid number before attempting conversion
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
satici_adres = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":40,"right":150,"bottom":70})
satici_vkn_no = extract_text_from_coordinates(pdf_file_path,{"left":20,"top":120,"right":150,"bottom":130})
satici_vergi_daire = extract_text_from_coordinates(pdf_file_path,{"left":50,"top":110,"right":150,"bottom":120})
alici_adi = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":230,"right":150,"bottom":240})
alici_adres = extract_text_from_coordinates(pdf_file_path,{"left":0,"top":240,"right":150,"bottom":280})
alici_vkn_no = extract_text_from_coordinates(pdf_file_path,{"left":20,"top":290,"right":150,"bottom":300})
alici_vergi_daire = extract_text_from_coordinates(pdf_file_path,{"left":50,"top":280,"right":150,"bottom":290})
fatura_tarihi =  extract_text_from_coordinates(pdf_file_path,{"left":430,"top":290,"right":500,"bottom":300})
urun_cinsi = extract_text_from_coordinates(pdf_file_path,{"left":110,"top":350,"right":200,"bottom":400}) #BUĞDAY
urun_tipi = extract_text_from_coordinates(pdf_file_path,{"left":70,"top":350,"right":100,"bottom":400})   #İTHAL
urun_miktar =  extract_text_from_coordinates(pdf_file_path,{"left":200,"top":350,"right":250,"bottom":400})
urun_fiyat = extract_text_from_coordinates(pdf_file_path,{"left":250,"top":350,"right":300,"bottom":400})
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
counter=1
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

urun_no = kod_gonder + "-" + "B" + "-" + str(counter) + "-" + str(urun_miktar)

veriler1= {
    "satici_adi":satici_adi,"satici_adres":satici_adres,"satici_vkn_no":satici_vkn_no,"satici_vergi_daire":satici_vergi_daire,"odenecek_tutar":odenecek_tutar,
    "alici_adi":alici_adi,"alici_adres":alici_adres,"alici_vkn_no":alici_vkn_no,"alici_vergi_daire":alici_vergi_daire,"fatura_tarihi":fatura_tarihi,
    "urun_cinsi":urun_cinsi,"urun_tipi":urun_tipi,"urun_miktar":urun_miktar,"urun_fiyat":urun_fiyat,"islem_tutari":islem_tutari,"islem_tutari":odenecek_tutar,
    "hesaplanan_kdv":hesaplanan_kdv,"depo_semt":depo_semt,"teslim_yeri_depo":teslim_yeri_depo,"counter":counter,"urun_no":urun_no,"islem_tutar1":islem_tutar1
}