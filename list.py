def concat_list():
    try:
        l1=[]
        while True:
            l1.append(int(input()))
    except:
        print(l1)
    try:
        l2=[]
        while True:
            l2.append(int(input()))
    except:
        print(l2)
    return l1+l2
s=concat_list()
print(s)
