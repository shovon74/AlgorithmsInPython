
def is_anagram(str1,str2):
    n1 = len(str1)
    n2 = len(str2)

    if n1 != n2:
        return 0
    else:
        sorted1 = sorted(str1)
        sorted2 = sorted(str2)

        for i in range(0, n1):
            if sorted1[i] != sorted2[i]:

                return 0
    return 1


str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"

result = is_anagram(str1,str2)

if result:
    print("is anagram")
else:
    print("Not Anagram")
