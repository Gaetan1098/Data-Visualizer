# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Gaetan Fodjo"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101263973"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-037"

#==========================================#
# Place your script for your batch_UI after this line

import load_data
import curve_fit
import histogram
import sort

filename = "batchUI.txt"

batch_file = open(filename)

prompt = ""

#formatting every line in the file
for line in batch_file:
        #removing all the new lines at the end of every line
        inputs = line.strip("\n")
        #splitting the commands by the semicolon seperator inturn removing the semicolon
        inputs = inputs.split(";")
        #assigning commands to corresponding inputs, it is what we do for every input
        prompt = inputs[0]

        print("The available commands are:\nL)oad Data\nS)ort Data\nC)urve Fit\nH)istogram\nE)xit\n\nPlease type your command:", prompt)

        if prompt == "L" or prompt == "l":

                load_data1 = inputs[1]
                print("Please enter the name of the file:", load_data1)
                while True:

                        load_data2 = inputs[2]
                        print("Please enter the attribute to use as a filter:", load_data2)

                        if load_data2 == "School":
                                load_data3 = inputs[3]
                                print("Please enter the value of the attribute:", load_data3)
                                load = load_data.load_data(load_data1, (load_data2, load_data3))
                                final = load_data.add_average(load)
                                break
                        elif load_data2 == "Health" or load_data2 == "Age" or load_data2 == "Failures":
                                load_data3 = inputs[3]
                                print("Please enter the value of the attribute:", load_data3)
                                load = load_data.load_data(load_data1, (load_data2, int(load_data3)))
                                final = load_data.add_average(load)
                                break
                        elif load_data2 == "All":
                                load_data = 0
                                load = load_data.load_data(load_data1, (load_data2, int(load_data3)))
                                final = load_data.add_average(load)
                                break
                        else:
                                print("Invalid attribute.")
                                continue

                print("Data loaded\n")

        elif prompt == "S" or prompt == "s":
                if "final" in globals():
                        sort1 = inputs[1]
                        print("Please enter the attribute you want to use for sorting:\n'Age' 'StudyTime' 'Failures' 'G_Avg'\n>>>", sort1)
                        for item in final:
                                if sort1 not in item.keys():
                                        print("Invalid command. Cannot be sorted by", sort1, "\n")
                                        break
                                else:
                                        sort2 = inputs[2]
                                        print("Ascending (A) or Descending (D) order:", sort2)
                                        if sort2 == "A":
                                                sorting = sort.sort_by_key(final, "A", sort1)
                                                sort3 = inputs[3]
                                                print("Data Sorted. Do you want to display the data? (Y or N):", sort3)
                                                if sort3 == "Y":
                                                        print(sorting, "\n")
                                                else:
                                                        print("\n")
                                                break

                                        elif sort2 == "D":
                                                sorting = sort.sort_by_key(final, "D", sort1)
                                                sort3 = inputs[3]
                                                print("Data Sorted. Do you want to display the data? (Y or N):", sort3)
                                                if sort3 == "Y":
                                                        print(sorting, "\n")
                                                else:
                                                        print("\n")
                                                break
                                        else:
                                                print("\n")
                                        break
                else:
                        print("File not loaded. Please, load a file first.\n")

        elif prompt == "c" or prompt == "C":
                if "final" in globals():
                        curve1 = inputs[1]
                        print("Please enter the attribute you want to use to find the best fit for G_Avg:", inputs[1])
                        for item in final:
                                if curve1 not in item.keys():
                                        print("Invalid command\n")
                                        break
                                else:
                                        curve2 = inputs[2]
                                        print("Please enter the order of the polynomial to be fitted:", inputs[2])
                                        print(curve_fit.curve_fit(final, curve1, int(curve2)), "\n")
                                        break
                else:
                        print("File not loaded. Please, load a file first.\n")

        elif prompt == "h" or prompt == "H":
                if "final" in globals():
                        hist1 = inputs[1]
                        print("Please enter the attribute you want to use for plotting:", hist1)
                        for item in final:
                                if hist1 not in item.keys():
                                        print("Invalid command.\n")
                                        break
                                else:
                                        hist = histogram.histogram(final, hist1)
                                        print("")
                                        break

                else:
                        print("File not loaded. Please, load a file first.\n")

        else:
                print("Invalid command.\n")

batch_file.close()

if prompt == "e" or prompt == "E":
        print("Program terminated")



