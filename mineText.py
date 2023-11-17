from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams,LTTextBox,LTTextLine

#extract text from a specified rectangular region in the pdf
def extract_text_from_coordinates(pdf_path,x0,y0,x1,y1):
    rect=(x0,y0,x1,y1)

    laparams = LAParams() ##create a layout analysis parameters object

    ##extract text in region 
    with open(pdf_path,'rb') as file :
        text=""
        for page in extract_text(file,laparams=laparams):
            for element in page:
                if isinstance(element,(LTTextBox,LTTextLine)):
                    bbox = element.bbox
                    if bbox[0] >= rect[0] and bbox[1] >= rect[1] and bbox[2] <= rect[2] and bbox[3] <= rect[3]:
                        text += element.get_text()
    return text
        

pdf_path='./Fatura.pdf'
x0,y0,x1,y1 = 20,100,300,400
region_text = extract_text_from_coordinates(pdf_path,x0,y0,x1,y1)

print(region_text)