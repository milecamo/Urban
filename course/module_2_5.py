# Задача "Матрица воплоти"

def get_matrix(n, m, value):
    matrix = []
    if n > 0 and m > 0:
        for i in range(n):
            matrix.append([])
            for j in range(m):
                # if isinstance(value, list):
                #     matrix[i].append(value[i * m + j])
                # else:
                matrix[i].append(value)
    return matrix


# result = get_matrix(2, 3, [1, 2, 3, 4, 5, 6])
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# print(result)
print(result1)
print(result2)
print(result3)
