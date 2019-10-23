
def first_repeat(str):
    size = len(str)
    output = ''
    k = 0
    for i in range(size):
        k += 1
        for j in range(k, size):
            if str[i] == str[j]:
                output += str[i]
                return output

    return output


str = "abccd"

result = first_repeat(str)
print(result)

