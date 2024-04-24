def iterative_levenshtein(s, t):
    """ 
    bibliography: https://www.python-course.eu/levenshtein_distance.php
    """

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range(cols)] for x in range(rows)]
    for i in range(1, rows):
        dist[i][0] = i

    for i in range(1, cols):
        dist[0][i] = i
        
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row-1][col] + 1, dist[row][col-1] + 1, dist[row-1][col-1] + cost)
   
 
    return dist[row][col]

def onTheSameRow(p,q):
    return abs(p[0]-q[0])<=25 and abs(p[1]-q[1])>=20

def onTheSameColumn(p,q):
    return abs(p[1]-q[1])<=25 and abs(p[0]-q[0])>=20

def canBeARectangle(A,B,C,D):
    return onTheSameRow(A,B) and onTheSameRow(C,D) and onTheSameColumn(A,C) and onTheSameColumn(B,D) and !onTheSameRow(A,C) and !onTheSameRow(B,D) and !onTheSameColumn(A,C) and !onTheSameColumn(B,D) and ( A[1]<B[1] and D[1]<C[1] and A[0]<D[0] and B[0]<C[0])

def howManySpaces(myString):
    ans = 0
    for character in myString:
        if character == " ":
            ans+=1
    return ans

def canBeAName(myString):
    spaces = 0
    dot = 0
    hyphen = 0 
    for character in myString:
        if character==" ":
            spaces+=1
        if character==".":
            dot+=1
        if character=="-":
            hyphen+=1
    if (spaces==2 or spaces==3) and (dot==1) and (hyphen<=1):
        return True
    else:
        return False

