
def gen_key_mat(msg: str, col):

    msg = list(msg.replace(" ", ""))
    row = math.ceil(len(msg) / col)
    empty_cells = row*col - len(msg)
    msg.extend('x'*empty_cells)

    mat= []
    for i in range(0, len(msg),col):
        mat.append(msg[i:i+col])

    return mat


def encrypt(msg: str, key: str):

    mat = gen_key_mat(msg, len(key))
    key = list(key)
    sorted_key = sorted(key)

    encrypted_text = ""
    k = 0

    for i in range(len(key)):
        col = key.index(sorted_key[k])
        for row in mat:
            encrypted_text += row[col]
        k += 1
    return encrypted_text


print(encrypt("Hello world", "hack"))

