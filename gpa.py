import csv
import pandas as pd #python library for manipulating data


class gpa():

    def __init__(self,file):
        self.file = file

    # reading data from csv file and extracting the data
    def readDataFile(self):
        course= []
        with open(self.file) as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=',')
            next(csv_data)
            for row in csv_reader:
                        course.append(row)
            course = [crs[3:] for crs in course]
            return course        




    #collection of data from the extracted csv data (course credits and units)
    # the function returns an array of credits and units of the courses
    def mergeData(self):
        data = self.readDataFile()
        get_points = [int(s.split(",")[0]) for c in data for s in c ]
        get_credits = [int(s.split(",")[1]) for c in data for s in c ]
        return get_points,get_credits



    # calculating gp based on the extracted course data for credits and units
    def gpa(self):
        grade = {"a":5,"b":4,"c":3,"d":2,"e":1,"f":0}
        get_points,get_credits = self.mergeData()
        get_units = self.readDataFile()
        sum_units = sum([int(c.split(",")[1]) for c in get_units[0]])
        for c in get_points:
            if int(c) >= 70:
                get_points[get_points.index(c)] = grade["a"] * int(get_credits[get_points.index(c)])/int(sum_units)
            elif int(c) >= 60 and int(c) < 70:
                get_points[get_points.index(c)] = grade["b"] * int(get_credits[get_points.index(c)])/int(sum_units)
            elif int(c) >= 50 and int(c) <= 69:
                get_points[get_points.index(c)] = grade["c"] * int(get_credits[get_points.index(c)])/int(sum_units)
            elif int(c) >= 45 and int(c) <= 49:
                get_points[get_points.index(c)] = grade["d"] * int(get_credits[get_points.index(c)])/int(sum_units)
            elif int(c) >= 40 and int(c) <= 44:
                get_points[get_points.index(c)] = grade["e"] * int(get_credits[get_points.index(c)])/int(sum_units)
            elif int(c) >=0 and int(c) <= 39:
                get_points[get_points.index(c)] = grade["f"] * int(get_credits[get_points.index(c)])/int(sum_units)

        slice_no = int(len(get_points)/len(get_units))
        prev = slice_no
        result = [] 
        nxt = 0
        sum_up =get_points[:18]
        for c in range(len(get_units)):
            nxt +=slice_no
            prev =nxt - slice_no
            result.append(round(sum(get_points[prev:nxt]),2))
        return result


    # updating the csv file with the calculated gpa
    def updateGpaFile(self):
        result = self.gpa()
        df = pd.read_csv(self.file)
        df.set_index('S/N', inplace=True)
        df["GPA"] = result
        return df.to_csv('gp.csv')


gp = gpa("gpmit.csv")
gp.updateGpaFile()