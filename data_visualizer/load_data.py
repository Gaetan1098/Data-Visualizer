# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Gaetan Fodjo, Kalan Caron, George Resendes-Awada, Kalya Tanumihardja"

# Update "" with your team (e.g. T102)
__team__ = "T037"

import string
#==========================================#


def student_school_list(filename: str, school: str) -> list[dict]:
    """Return a list of students (stored as a dictionary) from the school
    given.
    
    Preconditions: none
    
    >>> student_school_list('student-mat.csv', 'GP')
    [{'Age': 18, 'StudyTime': 1.8, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {another element}, ]
    """
    school_list = []
    infile = open(filename, "r")
    infile.readline()
    for line in infile:
        d = {'Age': '', 'StudyTime': '', 'Failures': '', 'Health': '',
             'Absences': '', 'G1': '', 'G2': '', 'G3': ''}
        lst = line.split(',')
        if lst[0] == school.upper():
            d['Age'] = int(lst[1])
            d['StudyTime'] = float(lst[2])
            d['Failures'] = int(lst[3])
            d['Health'] = int(lst[4])
            d['Absences'] = int(lst[5])
            d['G1'] = int(lst[6])
            d['G2'] = int(lst[7])
            d['G3'] = int(lst[8])
            school_list.append(d)
    infile.close()
    return school_list


#==========================================#
def student_health_list(file: str, status: int) -> list[dict]:
    """returns all data in terms of the student's health, with an inputted file /
    name.
    
    Preconditions: File must be inputted as .csv 
    """

    infile = open(file, 'r')
    infile.readline()
    pupils, code = [], []

    for i in infile:
        i = i.strip()
        ilist = i.split(",")
        student_profile = {}
        if int(ilist[4]) == status:
            student_profile = {
              "School": str(ilist[0]),
              "Age": int(ilist[1]),
              "StudyTime": float(ilist[2]),
              "Failures": int(ilist[3]),
              "Absences": int(ilist[5]),
              "G1": int(ilist[6]),
              "G2": int(ilist[7]),
              "G3": int(ilist[8]),
                }
            pupils += [student_profile]

    return pupils


#==========================================#
def student_age_list(filename: str, age: int) -> list[dict]:
    """
    return a list of all the students of the imputted age and their other stats in directories like Studytime, Health, Absences, G1, G2 and G3

    Predonditions: Age > 0

    >>> student_age_list('student-mat.csv.', 15)
    [{'School': 'CF', 'StudyTime': 2, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'StudyTime': 2, 'Failure': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7},
    [new element],
    ]

    >>> student_age_list('student-mat.csv.', 4)
    []

    """

    infile = open(filename, "r")  # open the file again
    infile.readline()

    outputlist = []

    for line in infile:  # read every line of the file
        directory = {}
        line = line.strip() # create a line that splits off the new lines
        line_list = line.split(",") #creates a list of the previous lines while splitting off the comma
        if line_list[1] == str(age):
            directory['School'] = str(line_list[0])
            directory['StudyTime'] = float(line_list[2])
            directory['Failures'] = int(line_list[3])
            directory['Health'] = int(line_list[4])
            directory['Absences'] = int(line_list[5])
            directory['G1'] = int(line_list[6])
            directory['G2'] = int(line_list[7])
            directory['G3'] = int(line_list[8])
            outputlist.append(directory) # add the newly created directory to the list

    infile.close()  # close the file
    return outputlist # return newly created list


#==========================================#
def student_failures_list(filename: str, fails: int) -> list[dict]:
    """
    The function returns a list of students (stored as a dictionary) with the same amount
    of failures as the input parameter.
    
    Preconditions: fails > 0
    
    Examples:
    >>> student_failures_list('student-mat.csv', 0)
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3, 'Absences': 7,
     'G1': 12, 'G2': 13, 'G3': 14},{another element}, …]
    """
    with open(filename, 'r') as content:

        content.readline()

        students = []

        for line in content:
            studentdata = {}
            line = line.strip()
            word_list = line.split(',')
            if int(word_list[3]) == fails:
                studentdata['School'] = str(word_list[0])
                studentdata['Age'] = int(word_list[1])
                studentdata['StudyTime'] = float(word_list[2])
                studentdata['Health'] = int(word_list[4])
                studentdata['Absences'] = int(word_list[5])
                studentdata['G1'] = int(word_list[6])
                studentdata['G2'] = int(word_list[7])
                studentdata['G3'] = int(word_list[8])
                students.append(studentdata)

    return students


#==========================================#
def load_data(filename: str, pair: tuple[str]) -> list[dict]:
    """
    This function returns a list of students stored as dictionaries with their data from the file name as asked from the tuple values.
    
    Preconditions: pair[0] == "School" or "Age" or "Health" or "Failures" or "All"
    
    Examples: 
    >>> load_data('student-mat.csv', (‘Failures’, 0))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Health': 3,
     'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
     {another element},
     …
    ] 
    >>> load_data('student-mat.csv', (‘All’, -1))
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
     'Health': 3, 'Absences': 7, 'G1': 12, 'G2': 13, 'G3': 14},
     {another element},
     …
    ] 
    >>> load_data('student-mat.csv', (‘G1’, 10))
    Invalid Value 
    []
    """
    students = []

    if pair[0] == "All":
        with open(filename, 'r') as content:

            content.readline()

            for line in content:
                studentdata = {}
                line = line.strip()
                word_list = line.split(',')
                studentdata['School'] = str(word_list[0])
                studentdata['Age'] = int(word_list[1])
                studentdata['StudyTime'] = float(word_list[2])
                studentdata['Failures'] = int(word_list[3])
                studentdata['Health'] = int(word_list[4])
                studentdata['Absences'] = int(word_list[5])
                studentdata['G1'] = int(word_list[6])
                studentdata['G2'] = int(word_list[7])
                studentdata['G3'] = int(word_list[8])
                students.append(studentdata)

        return students

    elif pair[0] == "Failures":
        return student_failures_list(filename, pair[1])

    elif pair[0] == "School":
        return student_school_list(filename, pair[1])

    elif pair[0] == "Age":
        return student_age_list(filename, pair[1])

    elif pair[0] == "Health":
        return student_health_list(filename, pair[1])

    else:
        print("Invalid Value")
        return students


#==========================================#
def add_average(studentdata: list[dict]) -> list[dict]:
    """
    This function returns a list of student data as dictionanries updated with their grade averages
    
    Examples:
    >>> add_average([ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7,
    'Failures': 1, 'Health': 3, 'Absences': 7,
   'G1': 5, 'G2': 6, 'G3': 6},
    {another element},
    … ] )
    [ {'School': 'GP', 'Age': 18, 'StudyTime': 6.7, 'Failures': 1,
    'Health': 3, 'Absences': 7, 'G1': 5, 'G2': 6, 'G3': 6,
    'G_Avg': 5.67 },
   {another element},
    …
   ]
    """

    if len(studentdata) == 0:
        return []

    avgdict = {}
    for i in range(len(studentdata)):
        avg = round((int(studentdata[i].get('G1')) + int(studentdata[i].get('G2')) + int(studentdata[i].get('G3'))) / 3, 2)
        avgdict = {'G_Avg': avg}
        studentdata[i].update(avgdict)

    return studentdata

# Do NOT include a main script in your submission
