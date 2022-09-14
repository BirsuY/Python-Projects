#by @BirsuY
import matplotlib.pyplot as plt

graph_name = input("Please enter the name of the graph: ")
line_num = int(input("Please enter the number of lines you would like to enter for the graph: "))
num = int(input("Please enter the number of points you would like to enter in a line: "))
for l in range(line_num):
    print("\nPlease enter the data for the line {}\n".format((l+1)))
    x = []
    y = []
    for t in range(num):
        x_el = int(input(f"Please enter the x axis of the point {t+1}: "))
        y_el = int(input(f"Please enter the y axis of the point {t+1}: "))
        x.append(x_el)
        y.append(y_el)
        print("\n")
    optn = input("Would you like to personalize the line(Y/N): ")
    if(optn.upper() == 'Y'):
        print("You can enter the hex for the color. \nIf you would like to use a gray shade enter a float between 0-1")
        clr = input("Please enter the color of the line: ")
        print("The options for line style is: solid, dashed or dotted")
        styl = input("Please enter the line style: ")
        wdth = int(input("Please enter the line width for the line: "))
        opt = input("Would you like to personalize marker features too(Y/N): ")
        if(opt.upper() == 'Y'):
            print("YYou can enter the hex for the color.. \nIf you would like to use a gray shade enter a float between 0-1")
            marker_color = input("Please enter the marker face color: ")
            marker_sz = int(input("Please enter the marker size: "))
            plt.plot(x,y, label = f'Line {l}', color = clr, linestyle = styl, linewidth = wdth, marker = 'o', markerfacecolor = marker_color, markersize = marker_sz)
        else:
            plt.plot(x,y, label = f'Line {l}', color = clr, linestyle = styl, linewidth = wdth)
    else:    
        plt.plot(x,y, label = f'Line {l}')

    
option = input("Would you like to change the name of the x axis and y axis(Y/N): ")
if(option.upper() == 'Y'):
    x_axis = input("What would you like name the x axis: ")
    y_axis = input("What would you like name the y axis: ")
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
else:    
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    
plt.title(graph_name)

plt.show()
#by @BirsuY