if __name__ == '__main__':
    s = input()
    ca=False
    cl=False
    cu=False
    cd=False
    cn=False
    for i in s:
        if i.isalnum():
            cn=True
        if i.isalpha():
            ca=True
        if i.islower():
            cl=True
        if i.isupper():
            cu=True
        if i.isdigit():
            cd=True
    print(cn)
    print(ca)
    print(cd)
    print(cl)
    print(cu)

u  = 1 1 1 1 1 1