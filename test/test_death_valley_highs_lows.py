import pytest
from pathlib import Path
import matplotlib.pyplot as plt
import sys
sys.path.append('D:/python/python_project_Data visualization')

from csv_weather.death_valley_highs_lows import plot_weather_data  

def test_plot_weather_data():
    csv_path = Path('csv_weather/weather_data/death_valley_2021_simple.csv')
    fig, ax = plot_weather_data(csv_path)
    assert fig is not None  # 确保图形对象不为空


