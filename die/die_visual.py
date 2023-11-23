import plotly.express as px
from die import Die

#创建一个D6
die = Die()

#掷几次骰子并将结果储存在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# fig=px.bar(x=poss_results,y=frequencies)    
# fig.show()

#定制绘图
title = "Result of Rolling One D6 1,000 Times "
labels={'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)
fig.show()


