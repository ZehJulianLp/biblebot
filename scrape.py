import requests
from bs4 import BeautifulSoup

url = 'https://www.bibel-gratis.de/bestellen/'  # Ersetzen Sie "https://example.com/formular" durch die tatsächliche URL der Webseite mit dem Formular
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("Fehler beim Herunterladen der Webseite.")

    # Finden Sie das Formularelement anhand seiner Attribute
form_element = soup.find('form', {'class': 'relative max-w-screen-md mx-auto -my-24 bg-white px-5 py-5 border border-gray-100 rounded-lg shadow-lg z-10 md:px-8'})

# Suchen Sie nach den Feldern innerhalb des Formulars
fields = form_element.find_all('input') + form_element.find_all('textarea') + form_element.find_all('select')

# Durchlaufen Sie die Felder und extrahieren Sie die Namen und anderen Attribute
for field in fields:
    field_name = field.get('id') or field.get('name')  # Der Name des Feldes kann in der id- oder name-Attribut gefunden werden
    field_type = field.get('type')
    print(f"Feldname: {field_name}, Feldtyp: {field_type}")