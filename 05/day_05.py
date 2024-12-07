rules = []
updates = []


def laodData(inputString):
    rules.clear()
    updates.clear()

    with open(inputString) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            if line.find("|") != -1:
                rule = []
                rule.append(int(line.split("|")[0]))
                rule.append(int(line.split("|")[1]))
                rules.append(rule)
                continue
            if line.find(",") != -1:
                update = []
                for value in line.split(","):
                    update.append(int(value))
                updates.append(update)


def checkUpdate(update):

    allRulesAreValid = True

    for rule in rules:
        if update.count(rule[0]) == 0 or update.count(rule[1]) == 0:
            continue
        if update.index(rule[0]) < update.index(rule[1]):
            continue
        allRulesAreValid = False

    return allRulesAreValid


def findCorrectUpdates():

    sumOfMiddleValues = 0

    for update in updates:
        if checkUpdate(update):
            sumOfMiddleValues += update[int(len(update)/2-0.5)]
    return sumOfMiddleValues



def adaptAllUpdatesToRules():

    sumOfMiddleValues = 0

    for update in updates:
        if checkUpdate(update):
            continue

        while not checkUpdate(update):
            adaptUpdateToRules(update)

        sumOfMiddleValues += update[int(len(update)/2-0.5)]
    return sumOfMiddleValues



def adaptUpdateToRules(update):
    for rule in rules:
        if update.count(rule[0]) == 0 or update.count(rule[1]) == 0:
            continue
        if update.index(rule[0]) < update.index(rule[1]):
            continue
        indexOfValue2 = update.index(rule[1])
        update.remove(rule[0])
        update.insert(indexOfValue2, rule[0])



def tests():

    laodData("test_files/example")
    assert findCorrectUpdates() == 143
    assert adaptAllUpdatesToRules() == 123

    laodData("test_files/input")
    assert findCorrectUpdates() == 6612
    assert adaptAllUpdatesToRules() == 4944

    print("Tests passed")

if __name__ == '__main__':
    tests()




