def divide(a,b):
    try:
        return a/b
    # except:
        # not passing a error type is dangerous because you will catch all errors
    except ZeroDivisionError:
        return "Divide by zero is meaningless"
    except TypeError:
        return "Both arguments need to be numbers"


print(divide(1, 2))
print(divide(1, 0))
print(divide(1, '34'))
