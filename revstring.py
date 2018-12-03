def  rev_string(x):

    y=""
    l=len(x)
    while l>0:
        y+=x[l-1]
        l=l-1
    return y
x=input()
print(rev_string(x))
