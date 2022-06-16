import pytz
import requests
import pycountry_convert as pc
import datetime
import json

chave = "5c288fa48dc401eec6d410c5f84f333c"
cidade = "Sapucaí-Mirim"

api_link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}"

r = requests.get(api_link)

dados = r.json()

print(dados)

# país

paises = dados["sys"]["country"]

pais = pytz.country_names[paises]


def continentes(i):
    pais_aplha = pc.country_name_to_country_alpha2(i)
    continente_codigo = pc.country_alpha2_to_continent_code(pais_aplha)
    continente_name = pc.convert_continent_code_to_continent_name(continente_codigo)

    return continente_name


continente = continentes(pais)

# temperatura

temperatura = dados["main"]["temp"]

temp_graus = temperatura - 273.15

print(f"País: {pais}")
print(f"Continente: {continente}")
print(f"Temperatura: {str(temp_graus).split('.')[0]}°C")