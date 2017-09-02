import csv
import os.path
import datetime
from airpi import AirPi
import time
airpi = AirPi()

def write_to_file(time, temp, pressure, altitude, sealevelpressure, lightlevel, volume, humidity, carbonmonoxide):
    file_exists = os.path.isfile('data.csv')
    with open('data.csv', 'a') as csvfile:
        fieldnames = ['Time', 'Temp', 'Pressure', 'Altitude', 'Sealevel Pressure', 'Light Level', 'Volume', 'Humidity', 'Carbon monoxide']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
                        {
                        'Time': time,
                        'Temp': temp,
                        'Pressure': pressure,
                        'Altitude': altitude,
                        'Sealevel Pressure': sealevelpressure,
                        'Light Level': lightlevel,
                        'Volume': volume,
                        'Humidity': humidity,
                        'Carbon monoxide': carbonmonoxide
                        })



def take_note():
    write_to_file(
              datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
              airpi.bmp085.get_data()[0],
              airpi.bmp085.get_data()[1],
              airpi.bmp085.get_data()[2],
              airpi.bmp085.get_data()[3],
              airpi.ldr.get_data(),
              airpi.tgs2600.get_data(),
              airpi.dht22.get_data()[1],
              airpi.mics5524.get_data()
              )

def main():
    while True:
        take_note()
        time.sleep(60 * 60)

main()
