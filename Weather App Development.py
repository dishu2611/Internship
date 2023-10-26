from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Weather
def getWeather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d2ea77aff0b8780d753050bc347f4f70"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']

        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")

        w.config(text=f"WIND: {humidity}")
        h.config(text=f"HUMIDITY: {humidity}")
        d.config(text=f"DESCRIPTION: {description}")
        p.config(text=f"PRESSURE: {pressure}")

    except Exception as e:
        messagebox.showerror("Weather App", "Invalid entry!!")

search_image = PhotoImage(file='C:\\Users\\Dikshitha d\\Desktop\\search.png.png')
myimage = Label(image=search_image)
myimage.place(x=20, y=20)

textfield = Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file='C:\\Users\\Dikshitha d\\Desktop\\sea.png.png')
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file='C:\\Users\\Dikshitha d\\Desktop\\logo.png.png')
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom box
Frame_image = PhotoImage(file='C:\\Users\\Dikshitha d\\Desktop\\box.png.png')
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label4.place(x=650, y=400)

t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 14, "bold"), bg="#1ab5ef")
w.place(x=100, y=430)
h = Label(text="...", font=("arial", 14, "bold"), bg="#1ab5ef")
h.place(x=230, y=430)
d = Label(text="...", font=("arial", 14, "bold"), bg="#1ab5ef")
d.place(x=390, y=430)
p = Label(text="...", font=("arial", 14, "bold"), bg="#1ab5ef")
p.place(x=638, y=430)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900 
window_height = 500  

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.mainloop()
