import re

def loadDataAsDoubleArray(inputString):
    data = []
    with open(inputString) as f:
        lines = f.readlines()
        for line in lines:
            innerData = []
            for char in line:
                if char != "\n":
                    innerData.append(char)
            data.append(innerData)
    return data



def countXMAS(data):

    count = 0

    count += findHorizontal(data, "XMAS")
    count += findVertical(data, "XMAS")
    count += findDiagonalTopLeftBottomRight(data, "XMAS")
    count += findDiagonalTopRightBottomLeft(data, "XMAS")

    return count



def findHorizontal(data, word):
    count = 0
    for line in data:
        text = "".join(line)
        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    return count

def findVertical(data, word):
    count = 0
    for i in range(0,len(data[0])):
        text = ""
        for j in range(0, len(data)):
            text += data[j][i]
        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    return count


def findDiagonalTopLeftBottomRight(data, word):
    count = 0
    for i in range(0,len(data)):
        text = ""
        for j in range(0,len(data)):
            if j+i < len(data):
                text += data[j][j+i]
        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    for i in range(1,len(data)):
        text = ""
        for j in range(0,len(data)):
            if j+i < len(data):
                text += data[j+i][j]
        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    return count


def findDiagonalTopRightBottomLeft(data, word):
    count = 0
    for i in range(0,len(data)):
        text = ""
        for j in range(0,len(data)):
            if j+i < len(data):
                text += data[j][len(data)-1-j-i]
        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    for i in range(1,len(data)):
        text = ""
        for j in range(0,len(data)):
            if j+i < len(data):
                text += data[j+i][len(data)-1-j]

        count += len(re.findall("XMAS", text))
        count += len(re.findall("SAMX", text))

    return count



def tests():

    data = loadDataAsDoubleArray("test_files/example")

    assert countXMAS(data) == 18

    data = loadDataAsDoubleArray("test_files/input")
    print (countXMAS(data))
    assert countXMAS(data) != 209


    print("Tests passed")

if __name__ == '__main__':
    tests()




