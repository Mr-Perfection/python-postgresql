def test(**kwargs):
    print(kwargs)

test(name="steph", age=21)

details = {'name': 'stephen', 'age': 21}
test(**details)

def test2(name, age):
    print(name, age)

test2(**details)

def both(*arg, **kwargs):
    print(arg, kwargs)


both(1,2,3, **{'name': 'james', 'age': 30})
both(1,2,3, name="steph", age=4)