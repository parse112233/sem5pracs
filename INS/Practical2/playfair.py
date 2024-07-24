import string
def matrix(key):
    keymat=[]
    key = "rose"
    keys= []
    pool = [char for char in string.ascii_lowercase if char != 'j']
    for i in key:
        if i not in keys:
            keys.append(i)
    for j in pool:
        if j not in keys:
            keys.append(j)

    for i in range(0, (len(keys)), 5):
        keymat.append(keys[i:i+5])

def diagraphs(pt):
    for i in range(len(pt)):
        if pt[i] == pt[(i+1) % (len(pt))]:
            pt.insert(i+1, 'x')
    if len(pt) & 1 == 1:
        pt.append('x')
    return pt

def locate_index(char, keymat):
    for i in range(len(keymat)):
        for j in range(len(keymat)):
            if keymat[i][j] == char:
                return i, j

def encrypt(key, pt):
    keymat = matrix(key.lower())
    plain = diagraphs(pt.lower().replace(" ", ""))
    ciphers = ""

    i=0
    while i<len(plain):
        c1 = locate_index(plain[i], keymat)
        c2 = locate_index(plain[i+1], keymat)

        if c1[0] == c2[0]:
            row1 = c1[0]
            col1 = (c2[1]+1) % 5
            row2 = c1[0]
            col2 = (c2[1]+1) % 5
        elif c1[1] == c2[1]:
            row1 = (c1[1]+1) % 5
            col1 = c2[0]
            row2 = (c2[1]+1) % 5
            col2 = c2[0]
        else:
            row1 = c1[0]
            col1 = c2[1]
            row2 = c1[0]
            col2 = c2[1]

        ciphers += keymat[row1][col1] +keymat[row2][col2]

        i += 2
    return ciphers
# "KCNVMP"
print(encrypt("hello world","playfair"))