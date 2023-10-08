import math

class Node():
    def __init__(self, a=None, b=None, x='', p=None):
        self.x = x
        self.p = p
        self.children = [a, b]
        self.n = None

def sort(a):
    if a[0].p < a[1].p:
        b, c = 0, 1
    else:
        b, c = 1, 0
    for i in range(2, len(a)):
        if a[i].p < a[c].p:
            if a[i].p < a[b].p:
                c, b = b, i
            else:
                c = i
    return b, c

P = [0.2, 0.2, 0.4, 0.15, 0.05]
X = ['x1', 'x2', 'x3', 'x4', 'x5']
a = [Node(None, None, X[i], P[i]) for i in range(len(X))]

while len(a) != 1:  #building a tree
    b, c = sort(a)
    a[b].n = 0
    a[c].n = 1
    x = a[b].x + a[c].x
    p = a[b].p + a[c].p
    d = Node(a[b], a[c], x, p)
    if b < c:
        a.pop(c)
        a.pop(b)
    if c < b:
        a.pop(b)
        a.pop(c)
    a.append(d)

Tree = a[0]

def find_code(name):  #find code to each letter using tree
    t = Tree
    code = ''
    while len(t.x) != 2:
        if t.children[0] != None and name in t.children[0].x:
            code = code + str(t.children[0].n)
            t = t.children[0]
        else:
            code = code + str(t.children[1].n)
            t = t.children[1]
    return code

C = []
for i in X:
    code = find_code(i)
    C.append(code)
    print(i, ' = ', code)

H = 0
R = 0
for i in range(len(P)):
    H += P[i] * math.log(P[i], 2) * (-1)
    R += len(C[i]) * P[i]

print('H = ', H)
print('R = ', R)
print('ефективність = ', H/R)
