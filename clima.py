import tkinter
from datetime import *
from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
import pytz
import requests
import pycountry_convert as pc
import json

background_day = "#6cc4cc"
background_afternoon = "#bfb86d"
background_night = "#484f60"
background = background_day

janela = Tk()
janela.title("")
janela.geometry("360x350")
janela.configure(bg=background)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# create frames

frame_search = Frame(janela, width=370, height=50, bg="white", pady=0, padx=0)
frame_search.grid(row=0, column=0)

frame_result = Frame(janela, width=370, height=300, bg=background, pady=0, padx=0)
frame_result.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("clam")

# function that receives and sends information

global imagem


def info():
    # Base Api
    card = "5c288fa48dc401eec6d410c5f84f333c"
    cities = search.get()

    api_link = f"https://api.openweathermap.org/data/2.5/weather?q={cities}&appid={card}"

    r = requests.get(api_link)

    dice = r.json()

    print(dice)

    # weather characteristics
    temperatures = dice["main"]["temp"]
    temp_degrees = temperatures - 273.15

    humidity = dice["main"]["humidity"]
    speed = dice["wind"]["speed"]
    description = dice["weather"][0]["description"]

    # search country and continents

    countries = dice["sys"]["country"]

    country = pytz.country_names[countries]

    def continents(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        continent_code = pc.country_alpha2_to_continent_code(pais_alpha)
        continent_name = pc.convert_continent_code_to_continent_name(continent_code)

        return continent_name

    continent = continents(country)

    # timezone
    timezone = pytz.country_timezones[countries]
    zone = pytz.timezone(timezone[0])
    hours = datetime.now(zone)
    hours = hours.strftime("%d/%m/%Y | %H:%M:%S %p")

    print(hours)

    # passing information to labels

    city["text"] = cities + " - " + country + " / " + continent
    data["text"] = hours

    humidity_result["text"] = humidity
    humidity_percentage["text"] = "%"
    humidity_name["text"] = "Humidade"

    temperature["text"] = "Temperatura: " + str(temp_degrees).split('.')[0] + "°C"
    wind_speed["text"] = f"Velocidade do vento: {speed} Km/h"
    weather["text"] = description

    # changing background color

    period_day = datetime.now(zone)
    period_day = period_day.strftime("%H")

    global imagem

    period = int(period_day)

    if period <= 5:
        imagem = Image.open("image/lua.png")
        background_color = background_night

    elif period <= 11:
        imagem = Image.open("image/sol_dia.png")
        background_color = background_day

    elif period <= 17:
        imagem = Image.open("image/sol_tarde.png")
        background_color = background_afternoon

    if period <= 23:
        imagem = Image.open("image/lua.png")
        background_color = background_night

    else:
        pass

    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    time_schedule = Label(frame_result, image=imagem, bg=background_color)
    time_schedule.place(x=200, y=26)

    janela.configure(bg=background_color)
    frame_search.configure(bg=background_color)
    frame_result.configure(bg=background_color)

    city["bg"] = background_color
    data["bg"] = background_color
    humidity_result["bg"] = background_color
    humidity_percentage["bg"] = background_color
    humidity_name["bg"] = background_color
    temperature["bg"] = background_color
    wind_speed["bg"] = background_color
    weather["bg"] = background_color

# config frame_search


search = Entry(frame_search, width=23, justify="left", font=("", 14),
               highlightthickness=1, relief="solid")
search.place(x=15, y=12)

entry = Button(frame_search, command=info, text="Ver clima", font="Ivy 9 bold",
               relief="raised", overrelief=RIDGE, bg="#feffff", fg=background)
entry.place(x=285, y=12)

# config frame_result

city = Label(frame_result, text="", anchor=CENTER,
             bg=background, fg="white", font="Arial 14")
city.place(x=10, y=4)

data = Label(frame_result, text="", anchor=CENTER,
             bg=background, fg="white", font="Arial 10")
data.place(x=10, y=54)

humidity_result = Label(frame_result, text="", anchor=CENTER,
                        bg=background, fg="white", font="Arial 45")
humidity_result.place(x=10, y=100)

humidity_percentage = Label(frame_result, text="", anchor=CENTER,
                            bg=background, fg="white", font="Arial 15 bold")
humidity_percentage.place(x=85, y=110)

humidity_name = Label(frame_result, text="", anchor=CENTER,
                      bg=background, fg="white", font="Arial 10")
humidity_name.place(x=85, y=140)

temperature = Label(frame_result, text="", anchor=CENTER,
                    bg=background, fg="white", font="Arial 16")
temperature.place(x=10, y=184)

wind_speed = Label(frame_result, text="", anchor=CENTER,
                   bg=background, fg="white", font="Arial 14")
wind_speed.place(x=10, y=230)

weather = Label(frame_result, text="", anchor=CENTER,
                bg=background, fg="white", font="Arial 14")
weather.place(x=225, y=155)

janela.mainloop()
