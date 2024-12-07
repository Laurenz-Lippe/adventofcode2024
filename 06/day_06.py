


def loadData(inputString, dataSize):

    data = "|"

    with open(inputString) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            data += line + ("|")

    print(data)
    return data



def tests():

    loadData("test_files/example", 10)

    #loadData("test_files/input")


    print("Tests passed")

if __name__ == '__main__':
    tests()




