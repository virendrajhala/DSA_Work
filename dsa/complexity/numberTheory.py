def sum(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10

    return sum

print(sum(452345))

#  above program has time complexity -> ) O(log(n) to base 10)
#  relation between a number(n) and the no. of digits(d) it contains ->  d = 1 + log(n) to base 10
#  above program gives sum of digits of a number

