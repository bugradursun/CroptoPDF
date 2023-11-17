import pdfkit

pdf_file = open('DepoRezervİstenilenForm.pdf','rb')
html_file = pdfkit.from_pdf(pdf_file,"deneme1.html")
pdf_file.close()
                            


