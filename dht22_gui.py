import Adafruit_DHT
import time
import tkinter as tk
from datetime import datetime

def read_sensor_data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)
    if humidity is not None and temperature is not None:
        current_time = datetime.now().strftime("%H:%M:%S")
        data = "Letzte Daten: {}\nTemperatur={:.1f}°C, Luftfeuchtigkeit={:.1f}%".format(current_time, temperature, humidity)
        result_label.config(text=data)
    else:
        result_label.config(text="Sensor nicht erkannt. Überprüfe die Verbindungen")
    root.after(60000, read_sensor_data)  

root = tk.Tk()
root.title("DHT22-GUI")

sensor = Adafruit_DHT.DHT22 
sensor_pin = 4

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

update_button = tk.Button(root, text="Daten Manuell Abrufen", command=read_sensor_data)
update_button.pack()

quit_button = tk.Button(root, text="Beenden", command=root.quit)
quit_button.pack()

root.geometry("400x200")

read_sensor_data()

root.mainloop()
