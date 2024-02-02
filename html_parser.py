import mammoth

custom_styles = "b => i" 

with open("PriceList.docx", 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles) 

html = result.value

print(html)


with open('output.txt', 'w') as html_file:
    html_file.write(html)