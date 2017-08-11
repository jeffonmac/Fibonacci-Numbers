# Fonction fibonacci Sequence with loop "recursive" :

mem = {}


def fib(number):
    # print("fib" + str(number))
    if number < 1:
        return 0
    if number < 3:
        return 1
    if number not in mem:
        mem[number] = fib(number - 1) + fib(number - 2)
    return mem[number]


# With loop "for" :
def fib2():
    list = [0, 1]
    for i in range(2, 25):
        new_value = list[i - 1] + list[i - 2]
        list.append(new_value)
    return list


# With loop "while" :
def fib3():
    i = 0
    list = [0, 1]
    f = 25
    while len(list) < f:
        new_value = list[i - 1] + list[i - 2]
        list.append(new_value)
        # i = i + 1
        i = len(list)
    return list


# Fonction dichotomous research
def search_dic(numb, short_list):
    start = 0
    end = len(short_list) - 1
    middle = (start + end) // 2
    while start < end:
        if short_list[middle] == numb:
            return middle
        elif short_list[middle] > numb:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
    return start


# Loop with Fibonacci Sequence and
# adding in the list "fibonacciList" :
fibonacciList = []
for number in range(25):
    a = fib(number)
    fibonacciList.append(a)

# Fibonacci List with loop "for" :
fibonacciList2 = fib2()

# Fibonacci List with loop "while" :
fibonacciList3 = fib3()

# Displaying the top 25 values :
print("List of 25 first Fibonacci Number with recursive :")
print(fibonacciList)
print("List of 25 first Fibonacci Number with loop for :")
print(fibonacciList2)
print("List of 25 first Fibonacci Number with loop while :")
print(fibonacciList3)

# Displaying the index of the number 17711 :
index = search_dic(17711, fibonacciList)
print("Index of 17711 Number fonction (- Recursive - list):", (index + 1))

# Displaying the index of the number 17711 :
index = search_dic(17711, fibonacciList2)
print("Index of 17711 Number fonction  ( - For - list):", (index + 1))

# Displaying the index of the number 17711 :
index = search_dic(17711, fibonacciList3)
print("Index of 17711 Number fonction ( - While - list):", (index + 1))
