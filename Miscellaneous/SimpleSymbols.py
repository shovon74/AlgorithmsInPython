def SimpleSymbols(str):
    str = '=' + str + '='
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(str)):
        if str[i] in alpha:
            if str[i-1] != '+' or str[i+1] != '+':
                return 'false'

    return 'true'
    # code goes here
    #return str

print(SimpleSymbols(input()))