print("hallo jarvis")
def func(n):
    if n<0:
        return 1
    return n*(func(n-1))