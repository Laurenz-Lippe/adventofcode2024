import re

def loadData(input):
    memory = ""
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            memory = memory + line
    return memory


def findMultiplies(memory):
    x = re.findall("mul\(\d+,\d+\)", memory)
    return x


def doMultiplay(multiply):
    x = re.findall("\d+", multiply)
    return int(x[0]) * int(x[1])


def removeDontParts(memory):
    while memory.find("don't()") != -1:
        pin = memory.find("don't()")
        pinDo = memory.find("do()", pin, len(memory))
        if memory.find("do()") != -1:
            memory = memory[:pin] + memory[pinDo + 4:]
        else:
            memory = memory[:pin]
    return memory



def calcMultiplies(memory, enableDoDonts):

    product = 0
    if enableDoDonts:
        memory = removeDontParts(memory)
    multiplies = findMultiplies(memory)
    for multiply in multiplies:
        product += doMultiplay(multiply)

    return product


def tests():
    memory = loadData("test_files/example")
    assert calcMultiplies(memory, False) == 161
    memory = loadData("test_files/example2")
    assert calcMultiplies(memory, True) == 48

    memory = loadData("test_files/input")
    assert calcMultiplies(memory, False) == 191183308
    assert calcMultiplies(memory, True) == 92082041

    print("Tests passed")

if __name__ == '__main__':
    tests()

    memory = loadData("test_files/input")
    print("Task 1: search for mul and calculate the product")
    print(calcMultiplies(memory, False))
    print("Task 2: search for mul and calculate the product, but ignore do() and don't()")
    print(calcMultiplies(memory, True))


