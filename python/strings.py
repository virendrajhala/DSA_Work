def swapEvenOdd(str):
    length = len(str)
    output = ""
    if length == 0 or length == 1:
        return str
    tempStr = ""
    for index in range(length):
        if index % 2 == 0:
            tempStr += str[index]
            if index == length-1:
                output += str[index]
        else:
            tempStr += str[index]
            output += tempStr[::-1]
            tempStr = ""
    return output


def main():
    str = "abcdeghjgkjdhfjkdwfl"
    print(swapEvenOdd(str))

main()
