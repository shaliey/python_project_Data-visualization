import plotly.express as px
from die import Die

#创建两个D6
die_1 = Die()
die_2 = Die(10)

#掷骰子多次，并将结果储存在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result=die_1.num_sides+die_2.num_sides
poss_results = range(2,max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# fig=px.bar(x=poss_results,y=frequencies)    
# fig.show()

#定制绘图
title = "Result of Rolling a D6 and a D10 50,000 Times "
labels={'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
#进一步定制图形
fig.update_layout(xaxis_dtick=1)
fig.show()
