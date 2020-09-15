def addition(n):
    return n+n
numbers = (1,2,3,4)
result = map(addition,numbers)
print(list(result))
result1 = map(lambda x: x+x,numbers)
print(list(result1))

#above use of map and lambda

#below generator, lazy evaluation
def cube(n):
    return n*3
def simplifiedGenerator(n):
    generatedResults = []
    currentN = 1
    while currentN <n:
        generatedResults.append(cube(currentN))
        currentN += 1
    return generatedResults
print(simplifiedGenerator(6))

def GeneratorUsingYield(n):
    currentN = 1
    while currentN < n:
        yield cube(currentN)
        currentN +=1

generatedvalues = GeneratorUsingYield(10)
print([ i for i in generatedvalues])


originallist = range(1,11)
for x in originallist:
    print (x)


for i in range(1,11):
    print(cube(i))
cubeUsingListComprehensions = [cube(x) for x in originallist]
print(cubeUsingListComprehensions)

# Application for list comprehension
print([[x,y] for x in [1,2,3] for y in[4,5,6]])
