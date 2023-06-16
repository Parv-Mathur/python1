d1={}
def dict_func():
    print("1: add new pair, 2:Remove pair, 3:update value, 4:Check key-value pair, 5:print all, 6:exit")
    n1=int(input("Enter your choice:"))
    if n1==1:
        a=int(input("Enter key: "))
        b=int(input("Enter value: "))
        d1[a]=b
        print(list(d1.keys()))
        dict_func()
    elif n1==2:
        print(d1)
        c=int(input("Enter key to delete: "))
        del d1[c]
        print(d1)
        dict_func()
    elif n1==3:
        d2={}
        print(d1)
        d=int(input("Enter key to update: "))
        e=int(input("Enter updated value: "))
        d2[d]=e
        d1.update(d2)
        print(d1)
        dict_func()
    elif n1==4:
        f=list(d1.keys())
        g=int(input("Enter key to search: "))
        for i in f:
            if(g==i):
                print("key found")
            else:
                print("Not found")
        dict_func()
    elif n1==5:
        h=list(d1.keys())
        print(h)
        dict_func()
    elif n1==6:
        exit
dict_func()
    
            
        
        
        
