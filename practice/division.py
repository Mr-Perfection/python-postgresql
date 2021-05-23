def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0")

    return dividend/divisor


try:
    # average = divide(20, 0)
    average = divide(20, 1)
except ZeroDivisionError as e:
    print(e)
    print('error')
else:
    print('success')
    print(average)
finally:
    print('finally!')

    