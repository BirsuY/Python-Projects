#birsuyilmaz
def binary_search(arr, target):
    middle = 0
    start = 0
    end = len(arr)
    steps = 0
    
    while(start <= end):
        print("Step", steps, ":", arr[start:end])
        middle = (end - start) // 2
        if(arr[middle] > target):
            steps += 1
            end = middle + 1
        elif(arr[middle] < target):
            steps += 1
            start = middle - 1
        else:
            print(f"Index of {target} is {middle}")
            break

arr = [] 
num = int(input("Please enter the number of the elements: "))
print("Please enter the elements: ")
for i in range(0, num):
    elmt = int(input())
    
    arr.append(elmt)

target = int(input("Please enter the target you want to find the index of: "))
binary_search(arr, target)
#birsuyilmaz
