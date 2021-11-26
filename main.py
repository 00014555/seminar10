def calculateTotal(finalMarks):
    total = 0
    for key in finalMarks:
        total = total+finalMarks[key]
    return total


def calculateAverage(finalMarks):
     average = calculateTotal(finalMarks) / len(finalMarks)
     return average

def display_average(finalMarks):
    print(finalMarks)

def main():
    marks = {'CSF': 75, 'FunPro': 80, 'WT': 85}
    display_average(calculateAverage(marks))

if __name__ == '__main__':
    main()



