from pathlib import Path
import json

#将数据转换为字符串读取并转换为pyhon对象
path = Path('eq/eq_data/eq_data_1_day_m1.geojson')
contents=path.read_text()
all_eq_data=json.loads(contents)

#查看数据集中的所有地震
all_eq_dicts=all_eq_data['features']
#print(len(all_eq_dicts))

mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

#将数据文件转换为更易于阅读的版本
path = Path('eq/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data,indent=4)
path.write_text(readable_contents)