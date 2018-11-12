#function
def fun_a():
    return 'a'

#generator
def gen_a():
    yield 'b'
    yield 'a'
    yield 'v'

print(fun_a())
print(gen_a())
ret = gen_a()
print(next(ret))
print(next(ret))
print(next(ret))

#large file iteration using generators
def Beerdata():
    f = open("recipeData.csv")
    for line in f:
        yield line
beer = Beerdata()

#print([next(beer) for __ in range(23)])

# for beer in Beerdata():
#     print(beer)

# print(next(beer))
# print(next(beer))
# print(next(beer))

#generator expression

lis = [n**2 for n in [1,2,3,4,5]]
ge = (n**2 for n in [1,2,3,4,5])

# print(lis)
#
# print(next(ge))
lines = (line for line in open('recipeData.csv'))
#lines = (gg for gg in open('output.txt'))

print(next(lines))

cols = (l.split(',') for l in lines)

columns = next(cols)
beerdicts = (dict(zip(columns,data)) for data in cols)

# for var in beerdicts:
#     print(var)

print(next(beerdicts))

#consume generator

beer_counts = {'Style':4324}
for bd in beerdicts:
    if bd["Style"] not in beer_counts:
        beer_counts[bd["Style"]] = 1
    else:
        beer_counts[bd["Style"]] += 1

print(beer_counts)
