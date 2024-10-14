def find_multiples(init, limit):
    multiples = []
    for i in range(init, limit + 1):
        if i % init == 0:
            multiples.append(i)
    return multiples


print(find_multiples(5, 25))
print(find_multiples(1, 2))
print(find_multiples(2, 6))
