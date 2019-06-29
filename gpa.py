import csv
import pandas as pd #python library for manipulating data



# reading data from file and extracting the courses
def readFromFile(result=None):
    course= []
    with open('mit.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_file)
        for row in csv_reader:
                    course.append(row)
        course = [c[3:] for c in course]
        return course        




#collection of data from the extracted courses (course credits and units)
# the function returns and array of credits and units of the courses
def collateData():
    data = readFromFile()
    get_scores = [int(s.split(",")[0]) for c in data for s in c ]
    get_credits = [int(s.split(",")[1]) for c in data for s in c ]
    return get_scores,get_credits



# calculating gpa based on the extracted course credits and units
def gpa():
    grade = {"a":5,"b":4,"c":3,"d":2,"e":1,"f":0}
    get_scores,get_credits = collateData()
    get_units = readFromFile()
    sum_units = sum([int(c.split(",")[1]) for c in get_units[0]])
    for c in get_scores:
        if int(c) >= 70:
            get_scores[get_scores.index(c)] = grade["a"] * int(get_credits[get_scores.index(c)])/int(sum_units)
        elif int(c) >= 60 and int(c) < 70:
            get_scores[get_scores.index(c)] = grade["b"] * int(get_credits[get_scores.index(c)])/int(sum_units)
        elif int(c) >= 50 and int(c) <= 69:
            get_scores[get_scores.index(c)] = grade["c"] * int(get_credits[get_scores.index(c)])/int(sum_units)
        elif int(c) >= 45 and int(c) <= 49:
            get_scores[get_scores.index(c)] = grade["d"] * int(get_credits[get_scores.index(c)])/int(sum_units)
        elif int(c) >= 40 and int(c) <= 44:
            get_scores[get_scores.index(c)] = grade["e"] * int(get_credits[get_scores.index(c)])/int(sum_units)
        elif int(c) >=0 and int(c) <= 39:
            get_scores[get_scores.index(c)] = grade["f"] * int(get_credits[get_scores.index(c)])/int(sum_units)

    slice_no = int(len(get_scores)/len(get_units))
    prv = slice_no
    result = [] 
    nxt = 0
    sum_up =get_scores[:18]
    for c in range(len(get_units)):
        nxt +=slice_no
        prv =nxt - slice_no
        result.append(round(sum(get_scores[prv:nxt]),2))
    return result


# updating the csv file with the calculated gpa
def updateFile():
    result = gpa()
    df = pd.read_csv('mit.csv')
    df.set_index('S/N', inplace=True)
    df["GPA"] = result
    return df.to_csv('mitgpa.csv')


updateFile()



