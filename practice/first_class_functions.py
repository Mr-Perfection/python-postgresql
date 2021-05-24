def divide(dividend, divisor):
    return dividend/divisor

def calc(*values, op):
    return op(*values)

result = calc(10, 5, op=divide)
print(result)

from operator import itemgetter
friends = [
    {"name": "Coolio"}
]
print(itemgetter("name")(friends[0]))