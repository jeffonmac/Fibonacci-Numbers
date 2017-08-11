# Fonction fibonacci Sequence with loop "recursive" :
def fib(valure):
        if valure < 1:
            return 0
        if valure < 3:
            return 1
        else:
            return fib(valure - 1) + fib(valure - 2)


# With loop "for" :
def fib2():
    liste = [0, 1]
    for i in range(2, 25):
        new_value = liste[i - 1] + liste[i - 2]
        liste.append(new_value)
    return liste


# With loop "while" :
def fib3():
    i = 0
    liste = [0, 1]
    f = 25
    while len(liste) < f:
        new_value = liste[i - 1] + liste[i - 2]
        liste.append(new_value)
        # i = i + 1
        i = len(liste)
    return liste

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