fib_arr = int(input("Enter the number of array: "))

n1 = 1
n2 = 1
arr = {}
if fib_arr <= 0:
    print("The number of terms should be positive")
elif fib_arr == 1:
    print("Fibonacci sequence for", fib_arr, "is:")
    print(n1)
else:
    print("Fibonacci sequence for", fib_arr, "is:")
    for count in range(fib_arr):
        # print(n1)
        arr[count] = n1
        print(arr[count])
        nth = n1 + n2
        n1 = n2
        n2 = nth
print("Element [", fib_arr, "] of Fibonacci array number series = ", arr[count])
