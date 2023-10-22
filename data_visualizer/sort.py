# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Gaetan Fodjo, Kalan Caron, George Resendes-Awada, Kalya Tanumihardja"

# Update "" with your team (e.g. T102)
__team__ = "T037"

#==========================================#
# Place your sort_students_age_bubble function after this line


def sort_students_age_bubble(list_dicts: list[dict], order: str) -> list[dict]:
    """
    Returns sorted list either ascending or descending, unless age is not in the dictionary. If "Age" is not a key in the dictionary, functions print a message stating the key is not in the dictionary
    
    Preconditions: order == "A" or "D"
    
    >>>sort_students_age_bubble([{"Age":10,"School":"GP"},{"Age":19,"School":"MS"}], "D")
    
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>> sort_students_age_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    
    "Age" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
    
    """

    for item in list_dicts:
        if 'Age' not in item.keys():
            print("Age key is not present")
            return list_dicts

    if order == "A":
        sort = True

        while sort:
            sort = False

            for i in range(len(list_dicts) - 1):
                if list_dicts[i]["Age"] > list_dicts[i + 1]["Age"]:
                    list_dicts[i], list_dicts[i + 1] = list_dicts[i + 1], list_dicts[i]
                    sort = True

    elif order == "D":
        sort = True

        while sort:
            sort = False

            for i in range(len(list_dicts) - 1):
                if list_dicts[i]["Age"] < list_dicts[i + 1]["Age"]:
                    list_dicts[i], list_dicts[i + 1] = list_dicts[i + 1], list_dicts[i]
                    sort = True

    return list_dicts

#==========================================#
# Place your sort_students_time_selection function after this line


def sort_students_time_selection(lst: list[dict], sort: str) -> list[dict]:
    """Return a sorted list based on the 'StudyTime' attribute. The list
    will be ascending or descending order based on the user input: 'A' for
    ascending, 'D' for descending.
    
    Preconditions: sort == 'A' or 'D'
    
    >>> sort_students_time_selection([{'StudyTime': 10.2, 'School': 'GP'}, {'StudyTime': 19.1, 'School': 'MS'}], 'D')
    
    [{'StudyTime': 19.1, 'School': 'MS'}, {'StudyTime': 10.2, 'School': 'GP'}]
    
    >>> sort_students_time_selection([{'School': 'GP'}, {'School': 'MS'}], 'D')
    
    'StudyTime' key not present
    [{'School': 'GP'}, {'School': 'MS'}]
    
    >>> sort_students_time_selection([], 'D')
    []
    """
    for item in lst:
        if 'StudyTime' not in item.keys():
            print("'StudyTime' key is not present")
            return lst

    if sort == 'A':
        for i in range(len(lst)):
            min_idx = i
            for j in range(i + 1, len(lst)):
                if lst[i]['StudyTime'] > lst[j]['StudyTime']:
                    min_idx = j
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
        return lst

    elif sort == 'D':
        for i in range(len(lst)):
            max_idx = i
            for j in range(i + 1, len(lst)):
                if lst[i]['StudyTime'] < lst[j]['StudyTime']:
                    max_idx = j
            lst[i], lst[max_idx] = lst[max_idx], lst[i]
        return lst

#==========================================#
# Place your sort_students_g_avg_insertion function after this line


def sort_students_g_avg_insertion(student_data: list[dict], order_of_list: str):
    """
    Sorts students by their grade average in either descending or ascending order
    
    Precondtions: Must use the student.csv file or the student.mat file. Both of which have the same style of dictionaries that the code can actually sort.

    >>> sort_students_g_avg_insertion([{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}, {"G_Avg":5.1,"School":"MS"}, {"G_Avg":2.1,"School":"MS"}, {"G_Avg":7.5,"School":"MS"}, {"G_Avg": 4.2,"School":"MS"}], "A")

    [{'G_Avg': 2.1, 'School': 'MS'}, {'G_Avg': 4.2, 'School': 'MS'}, {'G_Avg': 5.1, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 7.5, 'School': 'MS'}, {'G_Avg': 9.1, 'School': 'MS'}]


    >>> sort_students_g_avg_insertion([{"G_Avg":7.2,"School":"GP"}, {"G_Avg":9.1,"School":"MS"}, {"G_Avg":5.1,"School":"MS"}, {"G_Avg":2.1,"School":"MS"}, {"G_Avg":7.5,"School":"MS"}, {"G_Avg": 4.2,"School":"MS"}], "D")

    [{'G_Avg': 9.1, 'School': 'MS'}, {'G_Avg': 7.5, 'School': 'MS'}, {'G_Avg': 7.2, 'School': 'GP'}, {'G_Avg': 5.1, 'School': 'MS'}, {'G_Avg': 4.2, 'School': 'MS'}, {'G_Avg': 2.1, 'School': 'MS'}]


    >>> sort_students_g_avg_insertion([{"School":"GP"},{"School":"MS"}], "D")
    Key is not in the list
    [{'School': 'GP'}, {'School': 'MS'}]


    >>> sort_students_g_avg_insertion([], "")
    []
    """

    # checks to make sure all items in list have the 'G_Avg" key
    for items in student_data:  # looks at all the dictonary items in the data
        if 'G_Avg' not in items.keys():  # checks to see if the key 'G_Avg' is there
            print("Key is not in the list")  # tells user key is not in list
            return student_data  # returns orginal list

    if order_of_list == 'A':  # If user wants list to be in ascending order
        for i in range(1, len(student_data)):  # Traverse through 1 to len(student_data)
            studenti = student_data[i]
            # choose key depending on what the value of 'G_Avg'
            keyi = studenti['G_Avg']
            j = i - 1
            studentj = student_data[j]
            keyj = studentj['G_Avg']
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and keyi < keyj:
                student_data[j + 1] = student_data[j]
                j -= 1
                # Update the j value so the while condition sorts properly
                studentj = student_data[j]
                keyj = studentj['G_Avg']
            student_data[j + 1] = studenti  # swaps the value

    elif order_of_list == 'D':  # if user wants list in decending order
        for i in range(1, len(student_data)):  # Traverse through 1 to len(student_data)
            studenti = student_data[i]
            # choose keyi depending on what the value of 'G_Avg'
            keyi = studenti['G_Avg']
            j = i - 1
            studentj = student_data[j]
            keyj = studentj['G_Avg']
            # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
            while j >= 0 and keyi > keyj:
                student_data[j + 1] = student_data[j]
                j -= 1
                # Update the j value so the while condition sorts properly
                studentj = student_data[j]
                keyj = studentj['G_Avg']
            student_data[j + 1] = studenti  # swaps the value
    return student_data

#==========================================#
# Place your sort_students_failures_bubble function after this line


def sort_students_failures_bubble(list1: list[dict], order: str) -> list:
    """
    The function uses the bubble sort algorithm to sort the list of students’ dictionaries by the “Failures” attribute.
    'A' or 'D' for ascending or descending order respectively as second input
    
    Preconditions: order == 'A' or 'D', dictionaries must include 'Failures' as a key
    
    Examples: 
    >>>sort_students_failures_bubble(
    [{"Failures":10,"School":"GP"},{"Failures":19,"School":"MS"}], "D")
    [{"Failures": 19, "School":"MS"}, {"Failures":10, "School":"GP"}]
    
    >>> sort_students_failures_bubble([{"School":"GP"}, {"School":"MS"}], "D")
    "Failures" key is not present.
    [{"School":"GP"}, {"School":"MS"}]
     """

    for item in list1:
        if 'Failures' not in item.keys():
            print("Failures key is not present")
            return list1

    if order == 'A':
        swap = True
        while swap:
            swap = False
            for i in range(len(list1) - 1):
                if list1[i]['Failures'] > list1[i + 1]['Failures']:
                    aux = list1[i]
                    list1[i] = list1[i + 1]
                    list1[i + 1] = aux
                    swap = True

    elif order == 'D':
        swap = True
        while swap:
            swap = False
            for i in range(len(list1) - 1):
                if list1[i]['Failures'] < list1[i + 1]['Failures']:
                    aux = list1[i]
                    list1[i] = list1[i + 1]
                    list1[i + 1] = aux
                    swap = True

    return list1

#==========================================#
# Place your sort function after this line


def sort_by_key(lst: list[dict], order: str, attribute: str) -> list[dict]:
    """Return a sorted list according to the given attribute in ascending or 
    descending order based on the user input: 'A' for ascending, 'D' for 
    descending.
    
    Preconditions: order == 'A' or 'D'
    
    >>> sort_by_key([{"Age":10,"School":"GP"},{"Age":19.1,"School":"MS"}],"D","Age")
    [{"Age": 19, "School":"MS"}, {"Age":10, "School":"GP"}]
    
    >>> sort_by_key([{"School":"GP"},{"School":"MS"}], "D", "School")
    Cannot be sorted by School
    [{"School":"GP"},{"School":"MS"}]
    """
    if attribute == 'Age':
        return sort_students_age_bubble(lst, order)

    elif attribute == 'StudyTime':
        return sort_students_time_selection(lst, order)

    elif attribute == 'G_Avg':
        return sort_students_g_avg_insertion(lst, order)

    elif attribute == 'Failures':
        return sort_students_failures_bubble(lst, order)

    else:
        print('Cannot be sorted by', attribute)
        return lst

# Do NOT include a main script in your submission
