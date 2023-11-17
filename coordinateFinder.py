pixels_to_points = 72 / 96

gimp_width = 951
gimp_height = 582

pdfplumber_width = gimp_width * pixels_to_points
pdfplumber_height = gimp_height * pixels_to_points

coordinates = {
    "left":300,
    "top" :300,
    "right" : pdfplumber_width,
    "bottom" : pdfplumber_height,
}
print(coordinates)