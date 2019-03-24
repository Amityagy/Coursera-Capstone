# mergesort
x=[5,2,9,6,21,4,30,4,1,56,34,25,37,11]
n=len(x)
y=x[:n//2]
z=x[n//2:]
def sort_1():
    for i in (0,n//2):
        if y(i)>y(i+1):
            A(i)=y(i+1)
        else:
            A(i)=y(i)