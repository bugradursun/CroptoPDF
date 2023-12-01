import jinja2
import pdfkit
import PyPDF2
from datetime import datetime
import re 
from extractText import extract_data_from_pdf
from extractLayout import veriler1

##DICTIONARYDEN ALDIGIM KEY VE VALUELAR ZATEN DİREKT HTML'E GORE OLDUGU İCİN CONTEXT İLE RENDERLİYORUM.

#data = extract_data_from_pdf("Fatura.pdf")
data1=veriler1
context = data1

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader = template_loader)

html_template = '26kasimdene.html' #reserveFinalLastday.html #en gunceli yenihtmldevamet.html KULLAN !!
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf = "C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")
pdfkit.from_string(output_text,'26KasimDeneme11.pdf',configuration=config,css="style1.css",options={"enable-local-file-access": ""})
