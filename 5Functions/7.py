#Write a function that takes variable number of arguments and returns theeir sum.

def sum_all(*args):
    return sum(args)

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))