
list1 = []
list2 = []


def loadData(input):
    list1.clear()
    list2.clear()

    file = open(input, 'r')
    for line in file:
        strings = line.split("   ")
        num1 = int(strings[0])
        num2 = int(strings[1])
        list1.append(num1)
        list2.append(num2)
    file.close()
    return list1, list2


def sortList():
    list1.sort()
    list2.sort()

def calcDiff(list1, list2):
    diff = 0
    for i in range(len(list1)):
        diff += abs(list1[i] - list2[i])

    return diff


def getSimilarityScore(list1, list2):
    score= 0
    for i in range(len(list1)):
        count = 0
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                count += 1
        score += count*list1[i]
    return score


def tests():

    loadData("test_files/example")
    sortList()
    assert calcDiff(list1, list2) == 11
    assert getSimilarityScore(list1, list2) == 31

    loadData("test_files/input")
    sortList()
    assert calcDiff(list1, list2) == 1646452
    assert getSimilarityScore(list1, list2) == 23609874

    print("Tests passed")



if __name__ == '__main__':

    tests()

    loadData("test_files/input")
    sortList()
    print("Answer 1: Calculate the difference between the two lists")
    print(calcDiff(list1, list2))
    print("Answer 2: Calculate similarity as a score between the two lists")
    print(getSimilarityScore(list1, list2))


