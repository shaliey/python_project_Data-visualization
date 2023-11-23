from pathlib import Path
import pytest
import sys
sys.path.append('D:/python/python_project_Data visualization')
from eq.eq_world30_map import create_earthquake_plot

def test_create_earthquake_plot():
    path = Path('eq/eq_data/eq_data_30_day_m1.geojson')

    fig = create_earthquake_plot(path)

    fig.write_html('test_earthquake_plot.html')

    assert fig is not None

# 使用 pytest 运行测试
if __name__ == '__main__':
    pytest.main()
