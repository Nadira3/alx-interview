def recurse_column(triangle, n):
    if triangle.__len__() == n:
        return triangle
    for i in range(n - 1):
        triangle.append(recurse_row(triangle, [], 0, n))
    return triangle


def recurse_row(triangle, new_row, n, i):
    old_row = triangle[triangle.__len__() - 1]
    if n == 0:
        new_row.append(1)
    elif old_row.__len__() == new_row.__len__():
        new_row.append(1)
    else:
        new_row.append(old_row[n - 1] + old_row[n])
    if triangle.__len__() == n:
        return new_row
    return recurse_row(triangle, new_row, n + 1, i)


def pascal_triangle(n):
    triangle = []
    if n < 1:
        triangle.append([])
        return triangle
    return recurse_column([[1]], n)
