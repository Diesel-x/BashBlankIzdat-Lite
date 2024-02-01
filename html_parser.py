import mammoth

custom_styles = "b => i" 

# Открываем документ Word
with open("PriceList.docx", 'rb') as docx_file:
    result = mammoth.convert_to_html(docx_file, style_map = custom_styles) 

# Получаем HTML из результата
html = result.value

# Выводим HTML
print(html)


with open('output.txt', 'w') as html_file:
    html_file.write(html)