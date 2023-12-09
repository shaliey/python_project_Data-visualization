import pytest
import sys
sys.path.append('D:/python/python_project_Data visualization')

from die.die import Die

import plotly.express as px
from io import StringIO
import sys

def test_two_dice_plot():
    die_1 = Die()
    die_2 = Die()

    # 重定向标准输出以捕获绘图
    captured_output = StringIO()
    sys.stdout = captured_output

    # 创建图表并显示
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    poss_results = range(2, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    title = "Result of Rolling Two D6 Dice 1,000 Times "
    labels = {'x': 'Result', 'y': 'Frequency of Result'}
    fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
    fig.update_layout(xaxis_dtick=1)
    fig.show()

    # 恢复标准输出
    sys.stdout = sys.__stdout__

    # 检查是否有异常
    assert captured_output.getvalue() == ""

if __name__ == '__main__':
    pytest.main()
