import jinja2
import pdfkit
import PyPDF2
from datetime import datetime
import re #regular expressions 
import extractText
today_date = datetime.today().strftime("%d %b, %Y")
today_month = datetime.today().strftime("%B")
#
#
#
#islem_tarihi = today_date
#duzenleme_tarihi =today_month
#belge_no = "234"
#islem_counter = "324"
#satici_ad ="dsfasd"
#satici_tckn = "sdfsdf"
#satici_adres = "acarlra sites"
#satici_vergi_dairesi ="atasehir vergi"
#islem_counter_alici = "3"
#alici_ad="ahmet"
#alici_tckn="3452345"
#alici_adres="kadikoy caddebostan"
#alici_vergi_dairesi ="Caddebostan"
#isin_serino ="43"
#urun_sinifi="bugday"
#urun_turu ="ekmeklik"
#urun_grubu="un urunleri"
#urun_tipi="2. sinif"
#urun_altgrup = "hamur"
#hasat_yili = "2022"
#urun_depolama_yeri="sorgun yozgat"
#lisansli_depo="yozgat sorgun depolar"
#islem_miktari="10"
#birim_fiyat="10"
#islem_tutari="100"
#tescil_ucreti="20"
#tazmin_fonu="41"
#depo_ucreti="15"
#
#
#
#context = {'islem_tarihi':islem_tarihi,'duzenleme_tarihi':duzenleme_tarihi,'belge_no' : belge_no,'islem_counter': islem_counter,'satici_ad' : satici_ad,
#           'satici_tckn':satici_tckn,'satici_adres' :satici_adres,'satici_vergi_dairesi':satici_vergi_dairesi,'islem_counter_alici' : islem_counter_alici,
#            'alici_ad':alici_ad,'alici_tckn' : alici_tckn,'alici_adres' : alici_adres,'alici_vergi_dairesi' : alici_vergi_dairesi,'isin_serino' : isin_serino,
#            'urun_sinifi' : urun_sinifi,'urun_turu' : urun_turu,'urun_grubu':urun_grubu,'urun_tipi' : urun_tipi, 'urun_altgrup' : urun_altgrup, 'hasat_yili' : hasat_yili,
#            'urun_depolama_yeri':urun_depolama_yeri,'lisansli_depo':lisansli_depo,'islem_miktari' : islem_miktari,'birim_fiyat' : birim_fiyat,'islem_tutari' : islem_tutari,
#            'tescil_ucreti': tescil_ucreti,'tazmin_fonu':tazmin_fonu,'depo_ucreti' : depo_ucreti}
# 

source_pdf_file = open('RezervForm.pdf','rb')
pdf_reader = PyPDF2.PdfReader(source_pdf_file)
extracted_text = pdf_reader.pages[0].extract_text() #will define patterns to extract exact words from here
##print(extracted_text)
print(extractText.alici_adres)
date_pattern = r'\d{2}/\d{2}/\d{4}' #XX/XX/XXXX
number_pattern = r'\d+' #numbers 
text_pattern = r'[^0-9]+' #non-numeric texts

matches = re.findall(rf'{date_pattern}|{number_pattern}|{text_pattern}', extracted_text)
data = []
current_data = []
for match in matches :
    if(re.match(date_pattern,match)) :
        if current_data:
            data.append(current_data)
        current_data = [match]
    else : 
        current_data.append(match)

if current_data :
    data.append(current_data)

for item in data:
    if len(item) == 2:
        print(f"Number: {item[0]}")
        print(f"Text: {item[1]}")
    elif len(item) == 3:
        print(f"Date: {item[0]}")
        print(f"Number: {item[1]}")
        print(f"Text: {item[2]}")


##date1, number1, date2, text1, number2, text2, text3, number3, text4, text5, number4, text6, text7, text8, text9, text10, text11 = matches[:17]
##print("---------------------OUTPUT-------------------")
##print("Date 1:", date1)
##print("Number 1:", number1)
##print("Date 2:", date2)
##print("Text 1:", text1)
##print("Number 2:", number2)
##print("Text 2:", text2)
##print("Text 3:", text3)
##print("Number 3:", number3)
##print("Text 4:", text4)
##print("Text 5:", text5)
##print("Number 4:", number4)
##print("Text 6:", text6)
##print("Text 7:", text7)
##print("Text 8:", text8)
##print("Text 9:", text9)
##print("Text 10:", text10)
##print("Text 11:", text11)





