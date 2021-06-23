import matplotlib.pyplot as plt
import csv
import datetime
date = []
temprature = []
humidity = []
with open('data.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        date_string = row[0]
        date_object = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')

        date.append((date_object))
        temprature.append(round(float((row[1])), 4))
        humidity.append(round(float((row[2])), 4))

plt.plot(date, humidity, label='Humidity')
plt.plot(date, temprature, label = "Temprature")
plt.xlabel('Date/Time')
plt.ylabel('Humidity (%)')
plt.title('Humidity of the International Space Station \n From 18:00 to 21:00 on April 18, 2021')
plt.legend()
plt.show()
