import pytest
from pathlib import Path
import sys
import matplotlib.pyplot as plt
sys.path.append('D:/python/python_project_Data visualization')

from csv_weather.sitka_highs_lows import plot_weather_data  # 请替换为你的实际模块名


def test_plot_weather_data():
    csv_path = Path('csv_weather/weather_data/sitka_weather_2021_simple.csv')
    fig, ax = plot_weather_data(csv_path)
    
    # 手动调用 plt.show() 来显示图像
    plt.show()

    assert fig is not None  # 确保图形对象不为空
