def test_return_list():
    #Complete the function with your test cases

    #test that student_school_list returns a list (3 different test cases required)

    check.equal(type(load_data.student_school_list('student-test.csv', 'CF')), list)
    check.equal(type(load_data.student_school_list('student-test.csv', 'GP')), list)
    check.equal(type(load_data.student_school_list('student-test.csv', 'MB')), list)

    #test that student_age_list returns a list (3 different test cases required)

    check.equal(isinstance(load_data.student_age_list('student-test.csv', 19), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 15), list), True)
    check.equal(isinstance(load_data.student_age_list('student-test.csv', 7), list), True)

    #test that student_health_list returns a list (3 different test cases required)

    check.equal(type(load_data.student_health_list('student-test.csv', 5)), list)
    check.equal(type(load_data.student_health_list('student-test.csv', 3)), list)
    check.equal(type(load_data.student_health_list('student-test.csv', 10)), list)

    #test that student_failures_list returns a list (3 different test cases required)

    check.equal(type(load_data.student_failures_list('student-test.csv', 4)), list)
    check.equal(type(load_data.student_failures_list('student-test.csv', 6)), list)
    check.equal(type(load_data.student_failures_list('student-test.csv', 1)), list)

    #test that load_data returns a list (6 different test cases required)

    check.equal(type(load_data.load_data('student-test.csv', ('All', 4))), list)
    check.equal(type(load_data.load_data('student-test.csv', ('Failures', 3))), list)
    check.equal(type(load_data.load_data('student-test.csv', ('Health', 5))), list)
    check.equal(type(load_data.load_data('student-test.csv', ('Age', 20))), list)
    check.equal(type(load_data.load_data('student-test.csv', ('School', 'CF'))), list)
    check.equal(type(load_data.load_data('student-test.csv', ('Age', 15))), list)

     #test that add_average returns a list (3 different test cases required)

    check.equal(type(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])), list)
    check.equal(type(load_data.add_average([{'School': 'CF', 'Age': 17, 'StudyTime': 3, 'Failures': 3, 'Health': 4, 'Absences': 2, 'G1': 4, 'G2': 6, 'G3': 8}])), list)
    check.equal(type(load_data.add_average([{'School': 'MB', 'Age': 20, 'StudyTime': 1, 'Failures': 5, 'Health': 5, 'Absences': 4, 'G1': 0, 'G2': 7, 'G3': 5}])), list)

    check.summary()


# Place test_return_list_correct_lenght function here

def test_return_list_correct_lenght():
    #Complete the function with your test cases
    """Check the length of the lists outputted by each function."""

    #test that student_school_list returns a list with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_school_list("student-test.csv", "A")), 0)
    check.equal(len(load_data.student_school_list("student-test.csv", "GP")), 3)
    check.equal(len(load_data.student_school_list("student-test.csv", "MS")), 4)

    #test that student_age_list returns a list with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_age_list("student-test.csv", 19)), 0)
    check.equal(len(load_data.student_age_list("student-test.csv", 18)), 4)
    check.equal(len(load_data.student_age_list("student-test.csv", 17)), 6)

    #test that student_health_list returns a list with the correct lenght (3 different test cases required)

    check.equal(len(load_data.student_health_list("student-test.csv", 6)), 0)
    check.equal(len(load_data.student_health_list("student-test.csv", 1)), 1)
    check.equal(len(load_data.student_health_list("student-test.csv", 3)), 8)

    #test that student_failures_list returns a list with the correct lenght(3 different test cases required)

    check.equal(len(load_data.student_failures_list("student-test.csv", 4)), 0)
    check.equal(len(load_data.student_failures_list("student-test.csv", 0)), 11)
    check.equal(len(load_data.student_failures_list("student-test.csv", 2)), 2)

    #test that load_data returns a list with the correct lenght (6 different test cases required)

    check.equal(len(load_data.load_data("student-test.csv", ("School", "A"))), 0)
    check.equal(len(load_data.load_data("student-test.csv", ("School", "BD"))), 3)
    check.equal(len(load_data.load_data("student-test.csv", ("Age", 15))), 3)
    check.equal(len(load_data.load_data("student-test.csv", ("Health", 5))), 3)
    check.equal(len(load_data.load_data("student-test.csv", ("All", 6))), 15)
    check.equal(len(load_data.load_data("student-test.csv", ("Grades", 2))), 0)

    #test that add_average returns a list with the correct lenght (3 different test cases required)

    check.equal(len(load_data.add_average([{'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])), 1)
    check.equal(len(load_data.add_average([])), 0)
    check.equal(len(load_data.add_average([{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
                                           {'School': 'BD', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8},
                                           {'School': 'BD', 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12},
                                           {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])), 4)

    check.summary()


#Place test_return_correct_dict_inside_list function here

def test_return_correct_dict_inside_list():
    #Complete the function with your test cases

    #test that student_school_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal(load_data.student_school_list("student-test.csv", "GP")[::len(load_data.student_school_list("student-test.csv", "GP")) - 1], [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 15, 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}])

    check.equal(load_data.student_school_list("student-test.csv", "MB")[::len(load_data.student_school_list("student-test.csv", "MB")) - 1], [{'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 10, 'G2': 12, 'G3': 12}])

    check.equal(load_data.student_school_list("student-test.csv", "CF")[::len(load_data.student_school_list("student-test.csv", "CF")) - 1], [{'Age': 15, 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'Age': 17, 'StudyTime': 1.0, 'Failures': 2, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}])

    #test that student_age_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal(load_data.student_age_list("student-test.csv", 18)[::len(load_data.student_age_list("student-test.csv", 18)) - 1], [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])

    check.equal(load_data.student_age_list("student-test.csv", 17)[::len(load_data.student_age_list("student-test.csv", 17)) - 1], [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1': 5, 'G2': 5, 'G3': 6}, {'School': 'MS', 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}])

    check.equal(load_data.student_age_list("student-test.csv", 15)[::len(load_data.student_age_list("student-test.csv", 15)) - 1], [{'School': 'GP', 'StudyTime': 2.0, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}, {'School': 'CF', 'StudyTime': 5.0, 'Failures': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}])

    #test that student_health_list returns a correct dictionary inside the list  (3 different test cases required)

    check.equal(load_data.student_health_list("student-test.csv", 3)[::len(load_data.student_health_list("student-test.csv", 3)) - 1], [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'BD', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 1, 'G1': 13, 'G2': 12, 'G3': 12}])

    check.equal(load_data.student_health_list("student-test.csv", 5)[::len(load_data.student_health_list("student-test.csv", 5)) - 1], [{'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])

    check.equal(load_data.student_health_list("student-test.csv", 4)[::len(load_data.student_health_list("student-test.csv", 4)) - 1], [{'School': 'BD', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}, {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 4, 'G1': 14, 'G2': 14, 'G3': 14}])

    #test that student_failures_list returns a correct dictionary inside the list (3 different test cases required)

    check.equal(load_data.student_failures_list("student-test.csv", 0)[::len(load_data.student_failures_list("student-test.csv", 0)) - 1], [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])

    check.equal(load_data.student_failures_list("student-test.csv", 3)[0], {'School': 'GP', 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})

    check.equal(load_data.student_failures_list("student-test.csv", 2)[::len(load_data.student_failures_list("student-test.csv", 2)) - 1], [{'School': 'CF', 'Age': 15, 'StudyTime': 5.0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 9, 'G3': 7}, {'School': 'CF', 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'G1': 7, 'G2': 6, 'G3': 0}])

    #test that load_data returns a correct dictionary inside the list (6 different test cases required)

    check.equal(load_data.load_data("student-test.csv", ('All', "a"))[::len(load_data.load_data("student-test.csv", ("All", "a"))) - 1], [{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'MS', 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'G1': 9, 'G2': 8, 'G3': 8}])

    check.equal(load_data.load_data("student-test.csv", ('Failures', 1))[0], {'School': 'CF', 'Age': 16, 'StudyTime': 2.0, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12})

    check.equal(load_data.load_data("student-test.csv", ('School', "BD"))[::len(load_data.load_data("student-test.csv", ("School", "BD"))) - 1], [{'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'G1': 8, 'G2': 8, 'G3': 8}, {'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'G1': 10, 'G2': 9, 'G3': 9}])

    check.equal(load_data.load_data("student-test.csv", ('Age', 16))[::len(load_data.load_data("student-test.csv", ("Age", 16))) - 1], [{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}, {'School': 'CF', 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}])

    check.equal(load_data.load_data("student-test.csv", ('Health', 1))[0], {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9})

    check.equal(load_data.load_data("student-test.csv", ('Absences', 6)), [])

    #test that add_average returns a lcorrect dictionary inside the list  (3 different test cases required)

    check.equal(load_data.add_average([{'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9}])[0], {'School': 'MS', 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 7, 'G1': 10, 'G2': 9, 'G3': 9, 'G_Avg': 9.33})

    check.equal(load_data.add_average([{'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}])[0], {'School': 'MB', 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5, 'G_Avg': 5.0})

    check.equal(load_data.add_average([{'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}])[0], {'School': 'GP', 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67})

    check.summary()


#Place test_add_average function here

def test_add_average():
    # Complete the function with your test cases

    # test that the function does not change the lengh of the list provided as input parameter (5 different test cases required)
    # 1 test with School not being in directory
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv.', ('School', 'GP')))), 3)
    # 2 test with Health not being in directory
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv.', ('Health', 3)))), 8)
    # 3 test with Age not being in directory
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv.', ('Age', 16)))), 2)
    # 4 test with Failures not being in directory
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv.', ('Failures', 1)))), 1)
    # 5 test with All being in directory
    check.equal(len(load_data.add_average(
        load_data.load_data('student-test.csv.', ('All', 0)))), 15)

    # test that the function returns an empty list when it is called whith an empty list
    check.equal(load_data.add_average([]), [])

    # test that the function inscrememnts the number of keys of the dictionary inside the list by one  (5 different test cases required)
    # 1 test with School not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('School', 'GP')))
    test_dict = test_list[0]
    check.equal((len(test_dict)), 9)
    # 2 test with Health not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Health', 5)))
    test_dict = test_list[0]
    check.equal((len(test_dict)), 9)
    # 3 test with Age not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Age', 15)))
    test_dict = test_list[0]
    check.equal((len(test_dict)), 9)
    # 4 test with Failures not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Failures', 2)))
    test_dict = test_list[0]
    check.equal((len(test_dict)), 9)
    # 5 test with All being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('All', -1)))
    test_dict = test_list[0]
    check.equal((len(test_dict)), 10)

    # test that the G_Avg value is properly calculated  (5 different test cases required)

    # 1 test with School not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('School', 'GP')))
    test_dict = test_list[0]
    check.within(float(test_dict['G_Avg']), 5.66, 0.01)
    # 2 test with Health not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Health', 5)))
    test_dict = test_list[0]
    check.within(float(test_dict['G_Avg']), 11.33, 0.01)
    # 3 test with Age not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Age', 15)))
    test_dict = test_list[0]
    check.within(float(test_dict['G_Avg']), 8.33, 0.01)
    # 4 test with Failures not being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('Failures', 2)))
    test_dict = test_list[0]
    check.within(float(test_dict['G_Avg']), 7, 0.01)
    # 5 test with All being in directory
    test_list = load_data.add_average(
        load_data.load_data('student-test.csv.', ('All', 0)))
    test_dict = test_list[0]
    check.within(float(test_dict['G_Avg']), 5.66, 0.01)

    # check.summary()
    check.summary()

# Do NOT include a main script in your submission

