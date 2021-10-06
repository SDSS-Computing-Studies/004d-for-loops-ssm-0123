#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""

n = input("int number that is smaller than 10")

n = int(n)
resultf=0
for i in range(1,n+1):
    result = str(1)*i
    resultf = int(result) + int(resultf)


print("the sum of the series is",str(resultf))

