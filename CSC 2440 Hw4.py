def input_array():
    arr = [10, 20, 30, 40, 50]
    return arr

def Reverse_array_using_Stack(arr):
    stack = []

    for i in arr:
        stack.append(i)
    reversed_array = []

    while stack:
        reversed_array.append(stack.pop())
    return reversed_array

#Driver Code
if __name__ == "__main__":
    arr = input_array()
    print("Original array:", arr)

    reversed_arr = Reverse_array_using_Stack(arr)
    print("Reversed array:", reversed_arr)