import data
import math
'''
Headnote:
This assignment turned out really great for me, I got a lot of quality practice solving solutions using Python. I will 
note however that everytime I run my tests for hw1, it initializes all my variables including the ones within the 
functions which can be annoying when running the test cases
I have come to find that it is totally irrelevant what you put in for those values which are initalized,
however it is annoying that they prompt you anyways. Hopefully all is legible and you can follow my thought process
as I am positive that all of my solutions created a result which was asked of the instructions. Thanks!
'''


# problem 1 - vowel count
# this function will check to see if the user input has any vowels in it, and if it does, adds 1 to the vowel count
# which will be returned as a str
print("PROBLEM 1 VOWEL COUNT")


def vowel_count(sent: str) -> str:
    count = 0
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for l in sent:
        if l in vowels:
            count += 1
    return count



sentence = input("Write a sentence to see how many vowels: ")
print("there are: ", vowel_count(sentence), " vowels.")


# Problem 2 - Short lists
# This takes a nested list of integers as the input and returns a new list of only the nested lists of len = 2
print("PROBLEM 2 SHORT LISTS")


def short_lists(lis: list(list[int])) -> list[int]:
    new = []
    for k in lis:
        if len(k) == 2:
            new.append(k)
    return new


lis_example = [[1, 4], [1, 6, 5], [6, 1], [5]]
print(short_lists(lis_example))


# problem 3: Ascending_pairs
# This takes an input of a nested list of in integers and if a nested list is of len 2, it sorts the int values in that
# list and returns the original list with the sorted nested list
print("PROBLEM 3 ASCENDING PAIRS")


def ascending_pairs(li: list[list[int]]) -> list:
    new = []
    for k in range(len(li)):
        if len(li[k]) == 2:
            li[k].sort()
            new.append(li[k])
        else:
            new.append(li[k])
    return new


list3 = [[2, 55], [2, 0], [22], [20, 30, 2]]

print(ascending_pairs(list3))


# problem 4: add_prices
# this will take 2 inputs of type data.Price and combine the values to get one price
print("PROBLEM 4 ADD PRICES")


def add_prices(P1: data.Price, P2: data.Price):
    totcent = P1.cents + P2.cents
    total = P1.dollars + P2.dollars
    decimal = totcent / 100
    total = total + decimal
    return total


pri1 = data.Price(2, 2)
pri2 = data.Price(4, 6)
print("the prices combined are", add_prices(pri1, pri2))


# Problem 5: rectangle_area
# this takes one input of type data.Rectangle which will compute the area of the rectangle when given 2 data.Point's
print("PROBLEM 5 RECTANGLE AREA")


def rectangle_area(rect: data.Rectangle):
    xval = rect.top_left.x - rect.bottom_right.x
    yval = rect.top_left.y - rect.bottom_right.y
    return abs(xval * yval)


def rectangle_generator():
    a = int(input("what is top_left x val?: "))
    b = int(input("what is top_left y val?: "))
    c = int(input("what is bottom_right x val?: "))
    d = int(input("what is bottom_right y val?: "))

    pt1 = data.Point(a, b)
    pt2 = data.Point(c, d)
    rec = data.Rectangle(pt1, pt2)
    return rec


print("area = ", rectangle_area(rectangle_generator()))

# Problem 6: books_by_author
# this takes the input of a string and a list of type data.Book which will basically determine which books are written
# by the author in the first input and return the list of books written by them
print("PROBLEM 6 BOOKS BY AUTHOR")

the_fairy = data.Book('Sydney', "a fairy")
the_dog = data.Book('Tiger', "a dog")
the_hag = data.Book('Jack', "a hag")
the_dragon = data.Book('Ben', "a dragon")
booklist = [the_dragon, the_fairy, the_hag, the_dog]


def books_by_author(authname: str, books: list[data.Book]):
    realbooks = []
    for b in range(len(books)):
        if books[b].authors == authname:  # or authname != books[b].authors:
            realbooks.append(books[b])
    return realbooks


bookies = books_by_author(input("who is your favorite author: Jack, Ben, Tiger, or Sydney?: "), booklist)
print(bookies)


# Problem 7: circle_bound
# This problem takes in a rectangle and gives you the center point of a circle bounding the
# corners of the rectangle + a radius
print("PROBLEM 7 CIRCLE BOUND")


def circle_bound(rect: data.Rectangle):
    xvalrecpre = abs(rect.bottom_right.x - rect.top_left.x) / 2
    yvalrecpre = abs(rect.bottom_right.y - rect.top_left.y) / 2
    center = data.Point(xvalrecpre + rect.top_left.x, yvalrecpre + rect.top_left.y)
    preradius = (xvalrecpre ** 2) + (yvalrecpre ** 2)
    radius = math.sqrt(preradius)
    circ = data.Circle(center, radius)
    return circ


print(circle_bound(rectangle_generator()))

# Problem 8: below_pay_average
# this problem takes in a list of type data.Employee and returns a list of type str. It will compute the average pay of
# the workers and when your return it, it will be a list of employees that are paid below the average.
print("PROBLEM 8 BELOW PAY AVERAGE")
Jack = data.Employee("Jack", 25)
Ben = data.Employee("Ben", 79)
Tiger = data.Employee("Tiger", 45)
Sydney = data.Employee("Sydney", 16)
Papi = data.Employee("Papi", 22)
Mom = data.Employee("Mom", 46)
emplis1 = [Jack, Ben, Tiger, Sydney, Papi, Mom]
emplis2 = []


def below_pay_average(emplis: list[data.Employee]) -> list[str]:
    total = 0
    underpaid = []
    for p in range(len(emplis)):
        total += emplis[p].pay_rate
    if len(emplis) != 0:
        avg_pay = total / len(emplis)
        for p in range(len(emplis)):
            if emplis[p].pay_rate < avg_pay:
                underpaid.append(emplis[p].name)
        return underpaid
    else:
        return print("no data")
    return underpaid


print(below_pay_average(emplis1))

