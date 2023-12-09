from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('D:\\python\\python_project_Data visualization\\【立方数据学社】 2001-2022年逐年平均气温（分市）\\【立方数据学社】 2001-2022年逐年平均气温（分市）\\【立方数据学社】_咸宁市_2001-2022年逐年平均气温.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)

for index,column_header in enumerate(header_row):
    print(index,column_header)

dates,highs = [],[],
for row in reader:
    current_date=datetime.strptime(row[1],'%Y')
    high = float(row[6])
    dates.append(current_date)
    highs.append(high)
    
print(highs)

plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red')

#设置绘图的格式
ax.set_title("Average Temperatures,2001-2022",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
