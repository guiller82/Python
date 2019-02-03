#one
print ('one')


def func():
    print("func () in one.py")

print("TOP LEVEL in one.py")

if __name__ == "__main__":
    print("one.py is being run direectly")
else:
    print("one.py is being imported")
