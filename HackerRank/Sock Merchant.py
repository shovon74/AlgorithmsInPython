def sock_marchant(n,ar):
    count = 0
    ar.sort()
    i = 0
    while i < n-1:
        if ar[i] == ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count




ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
n = 9
print(sock_marchant(n, ar))

