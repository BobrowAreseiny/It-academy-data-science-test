
def unique_even(numbers):
    unique_evens = []
    for n in numbers:
       if n % 2 == 0:
           already = False
           for exist in unique_evens:
               if exist == n:
                   already = True
           if not already:
               unique_evens.append(n)

    length = len(unique_evens)
    for i in range(length):
        for j in range(length - 1 - i):
            if unique_evens[j] < unique_evens[j + 1]:
                unique_evens[j], unique_evens[j + 1] = unique_evens[j + 1], unique_evens[j]
    return unique_evens


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [1,2,5,7,9,32,5,7,13,7,996,9]
    print(unique_even(numbers))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
