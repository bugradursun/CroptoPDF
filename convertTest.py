import jinja2
import pdfkit
from datetime import datetime
import aspose.words as aw


#PDF TO HTML => https://products.aspose.com/words/python-net/conversion/pdf-to-html/ !! also usable with import
#doc = aw.Document("RezervForm.pdf")
#doc.save("Output.html")
birim_fiyat = "7.5" #!
islem_miktari = "100.000" #!
birimfiyat1 = float(birim_fiyat)
islem_miktari1 = float(islem_miktari)
islem_tutari1 = birimfiyat1 * islem_miktari1
islemtutari_str = str(islem_tutari1)
today_date = datetime.today().strftime("%d %b, %Y") #!
fatura_tarihi =today_date #!

alici_teslimyeri="Yozgat Sorgun" #!



today_month = datetime.today().strftime("%B")
tutar_deneme = "123456X"

context = {'birim_fiyat' : birim_fiyat, 'islem_miktari' : islem_miktari, 'islemtutari_str' : islemtutari_str, 'fatura_tarihi' : fatura_tarihi,'alici_teslimyeri':alici_teslimyeri}
 
template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'test.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_string(output_text,'reserveForm7.pdf',configuration=config)