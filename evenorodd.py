def Evenoradd(x):
    if x % 2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("Enter a number : "))
    result = Evenoradd(a)
    print(result)