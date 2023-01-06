def double(arg):
    print('Before:', arg)
    arg = arg *2
    print("after:", arg)

def change(arg):
    print('before:', arg)
    arg.append('More data')
    print('after:', arg)

def main():

    num = 10 
    double(num)
    print(num)


    saying = 'hello'
    double(saying)
    print(saying)

    numbers = [42,254,12]
    change(numbers)
    print(numbers)

if __name__ == "__main__":
    main()