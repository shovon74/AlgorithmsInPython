
def unique_vaalue(L):
    NL = []
    for i in L:
        if i not in NL:
            NL.append(i)
    return NL







L = [10, 20, 30, 10, 20]
print(unique_vaalue(L))


