import pytest
import sys
sys.path.append('D:/python/python_project_Data visualization')

from Plotly.die import Die
import plotly.express as px
from io import StringIO
import sys

def test_die_plot():
    die = Die()

    # 重定向标准输出以捕获绘图
    captured_output = StringIO()
    sys.stdout = captured_output

    # 创建图表并显示
    results = []
    for roll_num in range(1000):
        result = die.roll()
        results.append(result)

    frequencies = []
    poss_results = range(1, die.num_sides + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    title = "Result of Rolling One D6 1,000 Times "
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    fig.show()

    # 恢复标准输出
    sys.stdout = sys.__stdout__

    # 检查是否有异常
    assert captured_output.getvalue() == ""

if __name__ == '__main__':
    pytest.main()
