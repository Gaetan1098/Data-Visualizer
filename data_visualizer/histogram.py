#==========================================#
# imports required
import matplotlib.pyplot as plt
import numpy as np

# testing imports

# Place your histogram function after this line


def histogram(dictionary_lst: list[dict[str]], plotted_string: str):
    """
    This function displays the data in the dictionary in the form of a histogram. The bars show how many students have each value of a key

    Precondtions: Must use the student.csv file or the student.mat file. Both of which have the same style of dictionaries that the code can actually sort.

    >>> histogram([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 4, 'G2': 4, 'G3': 5, 'G_Avg': 4.33}, {'School': 'MB', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 2, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 4, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5}], "School")
    <Figure is displayed>

    >>> histogram([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67}, {'School': 'GP', 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 4, 'G2': 4, 'G3': 5, 'G_Avg': 4.33}, {'School': 'MB', 'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 2, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.33}, {'School': 'MB', 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 4, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5}], "G_Avg")
    <Figure is displayed>

    >>> histogram([{}, "not real")

    Key is not in the list or Key is not appropriate
    [{}]

    """
    # checks to make sure all items in list have the 'G_Avg" key
    for items in dictionary_lst:  # looks at all the dictonary items in the data
        if plotted_string not in items.keys():  # checks to see if the key 'G_Avg' is there
            # tells user key is not in list
            print("Key is not in the list or Key is not appropriate")
            return dictionary_lst  # returns orginal list

    fig1 = plt.figure()  # creates a graph
    # gives the graph a title
    plt.title("Students " + plotted_string + " Values")
    plt.xlabel(plotted_string + " Value")  # gives the x axis a subtitle
    plt.ylabel("Number of students")  # gives the y axis a subtitle
    if plotted_string == "School":  # if graphing keys with string values like "School"
        number_of_students = [0] * 5
        # sorts each student with their coresponding school
        for i in range(0, len(dictionary_lst)):
            if dictionary_lst[i]["School"] == "GP":
                number_of_students[0] += 1
            elif dictionary_lst[i]["School"] == "MB":
                number_of_students[1] += 1
            elif dictionary_lst[i]["School"] == "CF":
                number_of_students[2] += 1
            elif dictionary_lst[i]["School"] == "BD":
                number_of_students[3] += 1
            elif dictionary_lst[i]["School"] == "MS":
                number_of_students[4] += 1
        # plots the x and y dimenstions of each bar
        plt.bar(["GP", "MB", "CF", "BD", "MS"], number_of_students)

    # If graphing keys with numerical values
    elif plotted_string == "Age" or "StudyTime" or "Failures" or "Health" or "Absences" or "G1" or "G2" or "G3" or "G_Avg":
        number_of_students = [0] * 25
        # sorts each student with their coresponding key value
        for i in range(0, len(dictionary_lst)):
            for number in range(0, 25):
                # creates a range on numbers that each student is able to be sorted into
                if number <= dictionary_lst[i][plotted_string] < (number + 1):
                    number_of_students[number] += 1
                    # plots the x and y dimenstions of each bar
        plt.bar(range(0, 25), number_of_students)

    plt.grid()  # adds a grid to the graph
    plt.show()  # shows the graph to the user
    return

# Do NOT include a main script in your submission
