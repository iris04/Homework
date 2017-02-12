def small(a, b):
    if a < b:
        return a
    else b < a:
        return b


    num1 = 34
    num2 = 12
    sm = small(num1, num2)
    print "min(%i,%i) returns: %i" % (num1, num2, sm)

    