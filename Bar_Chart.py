#by @BirsuY
import matplotlib.pyplot as plt

graph_name = input("Please enter the name of the bar chart: ")
num = int(input("Please enter the number of bars you would like for the chart: "))
x = []
y = []
labels = []
colors = []
for i in range(num):
    x_el = int(input("\nPlease enter the placement of the bar: "))
    y_el = int(input("Please enter the height of the bar: "))
    label = input("Please enter the label of the bar: ")
    colr = input("Please enter the hex code of the bar's color(with #): ")
    x.append(x_el)
    y.append(y_el)
    labels.append(label)
    colors.append(colr)
    
wdth = float(input("\nPlease enter a number for the witdh of the bars: "))

plt.bar(x, y, tick_label=labels, width=wdth, color = colors)
x_axis =input("Please enter a general name for the labels on x axis: ") 
y_axis =input("Please enter a general name for the datas on y axis: ") 
plt.xlabel(x_axis)
plt.ylabel(y_axis)
    
plt.title(graph_name)

plt.show()
#by @BirsuY