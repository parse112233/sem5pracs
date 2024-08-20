# Railfence cipher
# Create an empty matrix where the column length will be equal to the length of the text
# For ex:
#   plaint text = "HELLOS"
#   MATRIX = [
#       [0, 0, 0, 0, 0, 0 ],
#       [0, 0, 0, 0, 0, 0 ],
#       [0, 0, 0, 0, 0, 0 ],
#       ]
#   INSERT THE TEXT IN RAILFENCE ORDER
#   MATRIX = [
#        [H, 0, 0, 0, O, 0 ],
#        [0, E, 0, L, 0, S ],
#        [0, 0, L, 0, 0, 0 ],
#        ]

# Dimensions
m = 3  # Number of rows
n = 4  # Number of columns

# Create an empty matrix
matrix = [[0] * n for _ in range(m)]
# print(matrix)

def encrypt(msg:str, rails:int):
    m = rails
    n = len(msg)

    empty_matrix = [[""] * n for _ in range(m)]

    for i in range(len(msg)):
        if

    print(empty_matrix)

encrypt("Hellos",3)