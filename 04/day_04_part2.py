
def loadDataAsDoubleArray(inputString):
    data = ""
    with (open(inputString) as f):
        lines = f.readlines()
        for line in lines:
            for char in line:
                if char != "\n":
                    data += char
    return data



def countCrossedMAS(data, dataSize):

    count = 0

    position = data.find("A")
    while position != -1:
        data = data.replace("A", "-", 1)
        if position < dataSize or position > len(data) - dataSize:
            position = data.find("A")
            continue

        if position % dataSize == 0 or position % dataSize == dataSize - 1:
            position = data.find("A")
            continue

        countMas = 0

        if data[position - dataSize -1] == "M" and data[position + dataSize + 1] == "S":
            countMas += 1
        if data[position - dataSize -1] == "S" and data[position + dataSize + 1] == "M":
            countMas += 1
        if data[position - dataSize + 1] == "M" and data[position + dataSize - 1] == "S":
            countMas += 1
        if data[position - dataSize + 1] == "S" and data[position + dataSize - 1] == "M":
            countMas += 1

        if countMas == 2:
            count += 1

        position = data.find("A")

    return count




def tests():

    data = loadDataAsDoubleArray("test_files/example")
    assert countCrossedMAS(data, 10) == 9

    data = loadDataAsDoubleArray("test_files/input")
    assert countCrossedMAS(data, 140) == 1992

    print("Tests passed")

if __name__ == '__main__':
    tests()




