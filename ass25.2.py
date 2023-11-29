# Write a program to find the password is valid or invalid.

k=input('Enter a Password:')
u=0
l=0
d=0
s=0
sp='@_$'
n=len(k)
for i in k:
    if i.islower():
        l=l+1
    elif i.isupper():
        u=u+1
    elif i.isdigit():
        d=d+1
    elif i in sp:
        s=s+1
if u>0 and l>0 and d>0 and s>0 and n>=8:
    print('Valid')
    print('Password is Strong')
elif u>0 and l>0 and s>0 and n>=8:
    print('Valid')
    print('Password is Medium')
elif u>0 or l>0 and d>0 and n>=8:
    print('Valid')
    print('Password is Weak')
else:
    print('Password is Invalid')
