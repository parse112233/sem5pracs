import string
def rem_j():
    pool = list(string.ascii_lowercase)
    for i in range(len(pool)):
        if pool[i] == "j":
            pool.pop(i)
            break
    return pool

# def matrix(key):
key = "playfair"
keymat = []
cols = []
keys = []
pool = rem_j()
#Chars of key in unique chars list i.e keys
for i in key:
    if i not in keys:
        keys.append(i)
#Chars of pool in unique chars list i.e keys
for j in pool:
    if j not in keys:
        keys.append(j)

#Creation of 5x5 matrix
for i in range(0, len(keys), 5):
    keymat.append(keys[i:i+5])

print(keymat)
# print(keys)