def main(x, y):
    return euclidean(x, y)

def euclidean(x, y):
        x, y = swap(x, y)
        if x % y != 0:
            y = x % y
            return euclidean(x, y)
        else:
            return y

def swap(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp
    return x, y


if __name__ == '__main__':
    print(main(3127, 8201))
