import requests
from customtkinter import *
from PIL import Image,ImageTk
#1f6d62c66e04dde04590618e5d468d2a

def getweather(city):
    api_key = "4857715897114bb1cee58aa0f6cb2573"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={f_city}&appid={api_key}"
    res = requests.get(url)

    if res.status_code == 404:
        print("Error , city not found ")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url,temperature,description,city , country)


def search():
    global f_city
    f_city = e_city.get()
    print(f_city)
    result = getweather(f_city)
    if result is None:
        return

    icon_url , temperature , description,city,country = result
    print(f"text={city},{country}".encode('utf-8'))

    image = Image.open(requests.get(icon_url,stream=True).raw)
    ctk_image = CTkImage(light_image=image, size=(200, 200))
    icon = ctk_image
    icon_label.configure(image=icon)
    icon_label.image = icon

    city_label.configure(text=f"City: {f_city}")
    temperature_label.configure(text=f"Temperature: {temperature:.2f} °C")
    description_label.configure(text=f"Description: {description}")

root = CTk()
root.title("Weather App ")
root.geometry("550x550")
root._set_appearance_mode("dark")
root.configure(fg_color='#77B0AA')

font = CTkFont(family='Comic Sans MS', size=17, weight='bold')
font1 = CTkFont(family='Calibri', size=17, weight='bold')

enter_city = CTkLabel(root,text="City Name :",text_color="black",fg_color="#77B0AA",font=font)
enter_city.place(x=185,y=40)

e_city = StringVar()
city_entry = CTkEntry(root,textvariable=e_city,width=270)
city_entry.place(x=160,y=75)

search_button = CTkButton(root,text = "Search" ,command=search,fg_color="#135D66",font=font,hover_color="#153448")
search_button.place(x=220,y=120)


icon_label = CTkLabel(root,text="")
icon_label.place(x=190,y=180)

city_label = CTkLabel(root,text="",font=font1)
city_label.place(x=230,y=175)

temperature_label = CTkLabel(root,text="",font=font1)
temperature_label.place(x=210,y=350)

description_label = CTkLabel(root,text="",font=font1)
description_label.place(x=207,y=390)

root.mainloop()


