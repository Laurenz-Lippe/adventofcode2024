

def loadData(inputString):
    reports = []
    with open(inputString) as f:
        lines = f.readlines()

        for line in lines:
            strings = line.split(" ")
            strings = [int(i) for i in strings]
            reports.append(strings)
    return reports


def countGoodReports(reports, deleteableElements):
    countGoodReports = 0

    for report in reports:
        if checkSingleReport(report, deleteableElements):
            countGoodReports += 1

    return countGoodReports


def checkSingleReport(report, deleteableElements):
    if deleteableElements == -1:
        return False
    deleteableElements -= 1

    ascending = True
    descending = True

    for i in range(0, len(report) - 1):
        if report[i] == report[i + 1] or abs(report[i] - report[i + 1]) > 3:
            if checkChildrenReports(report, i, deleteableElements):
                continue
            ascending = False
            descending = False

        if report[i] > report[i + 1]:
            if checkChildrenReports(report, i, deleteableElements):
                continue
            descending = False
        else:
            if checkChildrenReports(report, i, deleteableElements):
                continue
            ascending = False

    return ascending or descending

def checkChildrenReports(report, i, deleteableElements):
    report_left = report.copy()
    report_right = report.copy()
    report_left.pop(i)
    report_right.pop(i + 1)

    return checkSingleReport(report_left, deleteableElements) or checkSingleReport(report_right, deleteableElements)


def tests():
    assert countGoodReports(loadData("test_files/input"),0) == 490
    assert countGoodReports(loadData("test_files/input"),1) == 536

    assert countGoodReports(loadData("test_files/example"),0) == 2
    assert countGoodReports(loadData("test_files/example"),1) == 4


    assert countGoodReports(loadData("test_files/example_leon"),0) == 213
    assert countGoodReports(loadData("test_files/example_leon"),1) == 285


    print("Tests passed")



if __name__ == '__main__':

    # start test_files
    tests()

    print("Task 1: Check good Reports - Report has to be ascending or descending and each step is max 3")
    print(countGoodReports(loadData("test_files/input"),0))

    print("Task 2: Count good reports - Report has to be ascending or descending and each step is max 3 - But one step can be removed")
    print(countGoodReports(loadData("test_files/input"),1))


