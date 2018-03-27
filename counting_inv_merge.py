"""
@Harsha
Date : 21/3/18
"""


def merge_and_count(X, Y):
    count = 0
    C = []
    i, j = 0, 0
    min_size = min(len(X), len(Y))
    for it in range(min_size):
        C.append(min(X[i], Y[j]))
        if Y[j] < X[i]:
            count += len(Y[j:])
            j += 1
        else:
            i += 1
    if i < j:
        C.extend(X[i:])
    elif j > i:
        C.extend(Y[j:])
    return count, C


def sort_and_count(L):
    if len(L) == 1:
        return 0, L
    else:
        mid = int(len(L) / 2)
        A, B = L[:mid], L[mid:]
        count1, A = sort_and_count(A)
        count2, B = sort_and_count(B)
        r, L = merge_and_count(A, B)
    return count1 + count2 + r, L


if __name__ == "__main__":
    L = [2, 1, 3, 1, 2]
    count, L = sort_and_count(L)
    print(count)
