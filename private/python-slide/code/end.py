__builtins__.end = None

def test(x):
    if x > 0:
        print "a"
    else:
        print "b"
    end
end


def main():
    test(1)
    print('I can use end!')
end


if __name__ == "__main__":
    main()
