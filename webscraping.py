# F. Javier Morales
# 26/04/2023
# Python 3.11.3
# Windows 10
# Atom Editor 1.55.0

from bs4 import BeautifulSoup as bs
import requests
import json

# Asiganmos la url del sitio
url = 'https://super.walmart.com.mx/all-departments'

# Agregamos la información adicional de headers para obtener acceso al sitio
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'}

# Hacemos la petición
response = requests.get(url, headers=headers)

# Obtenemos el contenido html
soup = bs(response.text, 'html.parser')

# Se identificaron los elementos y clases que contienen la información pertinente
divs = soup.find_all('div', {'class': 'flex flex-column'})

# Diccionario para almacenar la información
result = dict()

for div in divs:
    h2 = div.find('h2', {'class': 'ma0'}).text.strip()
    ul = div.find('ul', {'class': 'pt2 pl0 list'})
    lis = ul.find_all('li', {'class': 'pv1 pv0-m'})
    lis_text = [li.text.strip() for li in lis]
    result[h2] = lis_text

print(result)

# Generación de archivo JSON
with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
