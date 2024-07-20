import reqcduests
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Weather App")
window.geometry("300x250")
window.eval('tk::PlaceWindow . center')

# Create and configure labels and entry fields
city_label = tk.Label(window, text="Country/City:")
city_label.pack()
city_entry = tk.Entry(window)
city_entry.pack()

# Create a button to fetch weather data
fetch_button = tk.Button(window, text="Show Weather")
fetch_button.pack()

# Create a label to display weather information
weather_label = tk.Label(window, text="")
weather_label.pack()


# Define the function to fetch weather data
def fetch_weather():
    city = city_entry.get()
    #To create an OpenWeatherMap API, go to 'https://home.openweathermap.org/users/sign_up' and sign up.
    #Then enter the API you created api_key.
    api_key = "your_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            weather_label.config(text=f"Temperature: {temperature}°C\nWeather: {weather}")
        else:
            messagebox.showerror("Error", data.get("message", "Unable to fetch weather data"))
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


fetch_button.config(command=fetch_weather)

window.mainloop()