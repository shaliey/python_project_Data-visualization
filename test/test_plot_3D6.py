import pytest
import sys
sys.path.append('D:/python/python_project_Data visualization')
from Plotly.die import Die
import plotly.express as px
from io import StringIO
import sys

def test_three_dice_experiment():
    die_1 = Die()
    die_2 = Die()
    die_3 = Die()

    # 重定向标准输出以捕获绘图
    captured_output = StringIO()
    sys.stdout = captured_output

    # 创建图表并显示
    results = []
    for roll_num in range(1000):
        result = die_1.roll() + die_2.roll() + die_3.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
    poss_results = range(3, max_result + 1)
    for value in poss_results:
        frequency = results.count(value)
        frequencies.append(frequency)

    title = "Result of Rolling Three D6 Dice 1,000 Times "
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