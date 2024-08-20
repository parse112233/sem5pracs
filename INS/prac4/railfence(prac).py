def encrypt(msg, rails):
    msg.replace(" ", "")
    mat = [['' for i in range(len(msg))] for j in range(rails)]

    row, check = 0, 0
    for i in range(len(msg)):
        if check == 0:
            mat[row][i] = msg[i]
            row += 1
            if row == rails:
                check = 1
                row -= 1
        else:
            row -= 1
            mat[row][i] = msg[i]
            if row == 0:
                check = 0
                row = 1
    print(mat)
    print(row, check)
    cipher = "".join("".join(row) for row in mat)
    return cipher

print(encrypt("hellos",3))
