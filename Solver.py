import math

class Solver:
    def __init__(self):
        pass

    def demo(self,a,b,c):
        d=b**2-4*a*c
        if d>0:
            disc: float = math.sqrt(d)
            root1=(-b+disc)/(2*a)
            root2=(-b-disc)/(2*a)
            return root1, root2
        elif d==0:
            return -b/(2*a)
        else:
            return "This equation has no roots"
if __name__=='__main__':
    #print(demo(1,2,1))
    assert 1==1, "Checking whether the expression is TRUE"
    for i in range(10):
        print(i)
        if i == 2:
            break
    for j in range(10):
        print(j, end=" ")
    s = "Geeks"
    for i in s:
        print(i)


    def add():
        x = 15

        def change():
            global x
            x = 20

        print("Before making changing: ", x)
        print("Making change")
        change()
        print("After making change: ", x)


    add()
    print("value of x", x)
    string = 'GeeksforGeeks'

    # lambda returns a function object
    ans="ab"
    print(string)
    print(lambda string: string)
    ans=lambda string: string+"sss"
    print(ans)

    x = "GeeksforGeeks"

    # lambda gets pass to print
    (lambda x: print(x))(x)
    lambda x: print(x)