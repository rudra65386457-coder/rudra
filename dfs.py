import sys
from collections import defaultdict

d=defaultdict(list)
sys.stdout.write(f"Enter the edges: \nEnter edge(-,-) to indicate exit input:\n")
sys.stdout.flush()

while True:
    edge=sys.stdin.readline().strip()
    if "," not in edge:
        continue
    x, y = edge.split(",")
    x, y = x.strip(), y.strip()
    if x=="-" and y=="-":
        break
    d[x].append(y)
    d[y].append(x)

sys.stdout.write(f"\nEnter the start node: ")
sys.stdout.flush()
start=sys.stdin.readline().strip()
sys.stdout.write(f"Enter the goal node: ")
sys.stdout.flush()
goal=sys.stdin.readline().strip()

sys.stdout.write(str(d))
sys.stdout.write(f"\nStart node: {start}\nGoal node: {goal}\n")

def head(l):
    return l[0] if l else None

def tail(l):
    return l[1:]

def goaltest(m):
    return m==goal

def cons(e,l):
    return [e]+l

def MoveGen(m):
    l=list()
    for i in d.get(m, []):
        l.append(i)
    return l

def RemoveSeen(c,a,b):
    l=[]
    for i in a:
        l.append(head(i))
    for i in b: #what's the error here
        l.append(head(i))
    return [x for x in c if x not in l]

def AddParent(l,m):
    l1=[]
    for i in l:
        l1.append([i,m])
    return l1

def Append(n,l):
    return n+l

def ReconstructPath(n,l):
    p=[]
    p.append(n[0])
    p.append(n[1])
    for i in l:
        if p[-1]==i[0]:
            p.append(i[1])
    p.reverse()
    return p
def dfs():
    OPEN=[[start,"Nil"]]
    CLOSED=[]

    i=0
    while OPEN:
        i+=1
        sys.stdout.write(f"\nIteration {i}:\n")
        sys.stdout.write(f"OPEN: {OPEN}\n")
        sys.stdout.write(f"CLOSED: {CLOSED}\n")

        nodepair=head(OPEN)
        m=head(nodepair)
        if goaltest(m):
            sys.stdout.write(f"\nThere exists a path from {start} to {goal}.\n")
            sys.stdout.write(f"There exists a solution for this problem.\n")
            path=ReconstructPath(nodepair,CLOSED)
            sys.stdout.write(f"Path: {start}")
            for i in path[2:]:
                sys.stdout.write(f" -> {i}")
            return
        else:
            CLOSED=cons(nodepair,CLOSED)
            children=MoveGen(m)
            NoRepeat=RemoveSeen(children,OPEN,CLOSED)
            Newlist=AddParent(NoRepeat,m)
            OPEN=Append(Newlist,tail(OPEN))
    sys.stdout.write(f"\nThere doesn't exists a path from {start} to {goal}.\n")
    sys.stdout.write(f"There doesn't exists a solution for this problem.\n")

dfs()