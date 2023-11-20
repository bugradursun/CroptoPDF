import jinja2
import pdfkit
from datetime import datetime

today_date = datetime.today().strftime("%d %b, %Y")
today_month = datetime.today().strftime("%B")
//extraction
islem_tarihi = today_date
duzenleme_tarihi =today_month
belge_no = "234"
islem_counter = "324"
satici_ad ="dsfasd"
satici_tckn = "sdfsdf"
satici_adres = "acarlra sites"
satici_vergi_dairesi ="atasehir vergi"
islem_counter_alici = "3"
alici_ad="ahmet"
alici_tckn="3452345"
alici_adres="kadikoy caddebostan"
alici_vergi_dairesi ="Caddebostan"
isin_serino ="43"
urun_sinifi="bugday"
urun_turu ="ekmeklik"
urun_grubu="un urunleri"
urun_tipi="2. sinif"
urun_altgrup = "hamur"
hasat_yili = "2022"
urun_depolama_yeri="sorgun yozgat"
lisansli_depo="yozgat sorgun depolar"
islem_miktari="10"
birim_fiyat="10"
islem_tutari="100"
tescil_ucreti="20"
tazmin_fonu="41"
depo_ucreti="15"



context = {'islem_tarihi':islem_tarihi,'duzenleme_tarihi':duzenleme_tarihi,'belge_no' : belge_no,'islem_counter': islem_counter,'satici_ad' : satici_ad,
           'satici_tckn':satici_tckn,'satici_adres' :satici_adres,'satici_vergi_dairesi':satici_vergi_dairesi,'islem_counter_alici' : islem_counter_alici,
            'alici_ad':alici_ad,'alici_tckn' : alici_tckn,'alici_adres' : alici_adres,'alici_vergi_dairesi' : alici_vergi_dairesi,'isin_serino' : isin_serino,
            'urun_sinifi' : urun_sinifi,'urun_turu' : urun_turu,'urun_grubu':urun_grubu,'urun_tipi' : urun_tipi, 'urun_altgrup' : urun_altgrup, 'hasat_yili' : hasat_yili,
            'urun_depolama_yeri':urun_depolama_yeri,'lisansli_depo':lisansli_depo,'islem_miktari' : islem_miktari,'birim_fiyat' : birim_fiyat,'islem_tutari' : islem_tutari,
            'tescil_ucreti': tescil_ucreti,'tazmin_fonu':tazmin_fonu,'depo_ucreti' : depo_ucreti}
 
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'reserveFinal.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_string(output_text,'reserveFormTest6.pdf',configuration=config,css = "reserve.css")
