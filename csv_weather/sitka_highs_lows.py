from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# path = Path('csv_weather/weather_data/sitka_weather_2021_simple.csv')
# lines = path.read_text().splitlines()

# reader = csv.reader(lines)
# header_row = next(reader)
# #print(header_row)

# for index,column_header in enumerate(header_row):
#     print(index,column_header)

# dates,highs,lows = [],[],[]
# for row in reader:
#     current_date=datetime.strptime(row[2],'%Y-%m-%d')
#     high = int(row[4])
#     low = int(row[5])
#     dates.append(current_date)
#     highs.append(high)
#     lows.append(low)
# print(highs)

# plt.style.use('seaborn')
# fig,ax = plt.subplots()
# ax.plot(dates,highs,color='red',alpha=0.5)
# ax.plot(dates,lows,color='blue',alpha=0.5)
# ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# #设置绘图的格式
# ax.set_title("Daily High and Low Temperatures,2021",fontsize=24)
# ax.set_xlabel('',fontsize=16)
# fig.autofmt_xdate()
# ax.set_ylabel("Temperature(F)",fontsize=16)
# ax.tick_params(labelsize=16)

# plt.show()

def plot_weather_data(file_path):
    lines = file_path.read_text().splitlines()

    reader = csv.reader(lines)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, color='red', alpha=0.5)
    ax.plot(dates, lows, color='blue', alpha=0.5)
    ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)", fontsize=16)
    ax.tick_params(labelsize=16)

    return fig, ax
