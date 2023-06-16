def even_num(n1):
    if n1%2==0:
        return True
    else:
        return False
s=int(input("Enter integer:"))
s2=even_num(s)
print(s2)