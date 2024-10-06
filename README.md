T-037GROUP Version 1.0 04/12/23

<header id="top"></header>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
 <li><a href="#description">Description</a></li>
    <ul>
        <li><a href="#load-data-module">Load Data Module</a></li>
        <li><a href="#sort-plot-module">Sort Plot Module</a></li>
        <li><a href="#optimization-module">Optimization Module</a></li>
        <li><a href="#text-ui-module">Text UI Module</a></li>
        <li><a href="#batch-ui-module">Batch UI Module</a></li>
      </ul>
    </li>
    <li><a href="#Dependancies">Dependancies</a></li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#loading-data-set-functions">Loading Data Set Functions</a></li>
        <li><a href="#loading-data-test-functions">Loading Data Test Functions</a></li>
        <li><a href="#implement-sorting-curve-fitting-and-plotting-functions">Implement Sorting, Curve Fitting and Plotting Functions</a></li>
        <li><a href="#optimization-and-user-interfaces">Optimization and User Interfaces</a></li>
      </ul>
    </li>
    <li><a href="#contact-information">Contact Information</a></li>
    <li><a href="#Work Division">Work Division</a></li>
    <li><a href="#Legal licenses">Legal Licenses</a></li>
  </ol>
</details>

<!-- DESCRIPTION -->
## **Description**
_________
A Python program for plotting and graphing Excel data, streamlining data visualization and analysis. Implemented using Python’s matplotlib, numpy, and scipy libraries for enhanced graph plotting. Extracted and sorted Excel data into lists and dictionaries using bubble, insertion, and selection algorithms. Conducted software unit tests using Python’s unittest library, enhancing code reliability and functionality.

### Load Data (Type Module)
* Set Functions
  * Returns dictionary with attributes listed above depending on function 
* Test Functions
  * Test proper storage of dictionary data based on two parameters, the file of the data location and a tuple with a pair of values. Unit testing
* Add Average
  * Adds average of students grades based on the three grade attributes in a given dictionary, and adds the grade average as a new attribute.

### Sorting Data
* Sorting Functions
  * sort_students_bubble takes a list of dictionaries, as well as a direction indicator and creates a sorted list for any given attribute in the dictionary. This is done in either descending or ascending order
* Sorting Module
  * Implements developed sorting functions in order to sort the list of students' dictionaries. Must be sorted for an attribute with an integer value
### Optimization 
* Curve_fit
  * Returns a string representation of the equation of the best fit for the average of G_Avg for any chosen attribute and degree. 
* Histogram
  * Goes through all students and stores the number of students that are at each level of a chosen attribute. Based on the matplotlib library.
### Text User Interface
* Allows user to interact with given functions by answering prompts. A new meny may appear after execution, prompting for extra information, or other results are displayed.

### Batch User Interface
* Uses all the same commands as the text UI and should function similarly. Input will instead be taken from a text file.


<!-- INSTALLATION -->
## **Installation**
___
* Runs using **Python Version 3.10.9** on  **Wing 101 Version 8.3.3**:
* **Python Version 3.10.9** can be installed here: https://www.python.org/downloads/windows/
* Libraries NumPy, Matplotlib, as well as SciPy must be installed through command prompts:
    * python -m pip
    install -U matplotlib
    * python -m pip
    install -U numpy
    * python -m pip
    instal -U scipy
* These files must be placed in the folder titled "data_visualizer" as a zip file:
    * load_data.py
    * test_load_data.py
    * sort.py
    * curve_fit.py
    * histogram.py
    * text_UI.py
    * batch_UI.py
    * check.py
    * student-test.csv
    * README.md (Youre reading this right now)



<!-- Usage -->
## **Usage**
___
* Refer to included user video

<!-- CONTACT -->
## **Contact Information**
---

* GROUP LEADER: Gaetan Fodjo - gaetanfodjo@gmail.com
<!-- Credits -->
## **Credits**
___
George Resendes-Awada
* student_health_list function
* test_return_list function
* sort_students_age_bubble function
* curve_fit function
* README.md file

Kalan Caron
* student_age_list function
* add_average test function
* sort_students_g_avg_insertion function
* histogram function
* user video

Kalya Tanumihardja
* student_school_list function
* test_return_list_correct_length function
* sort_students_time_selection function
* sort function
* text_UI module

Gaetan Fodjo (LEADER)
* student_failures_list function
* load_data function
* add_average function
* test_return_correct_dict_inside_list function
* sort_students_failures_bubble function
* batch_UI module

<!-- LICENSE -->
## **License**
___
Copyright (c) 2023
T037GROUP

This software and its documentation are copyrighted and protected by the laws of Canada. Unauthorized reproduction or distribution of this software, or any portion of it, may result in severe civil and criminal penalties, and will be prosecuted to the maximum extent possible under the law.

This software is licensed, not sold, to you for use only under the terms of this license agreement. Any use, reproduction or distribution of the software not in accordance with the terms of this license agreement is expressly prohibited.

By using this software, you acknowledge that you have read this license agreement, understand it, and agree to be bound by its terms and conditions. If you do not agree to the terms and conditions of this license agreement, do not use this software.

This software is provided "as is" without warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of this software is with you.

In no event will the author, copyright holder, or any other party who may have contributed to the development or distribution of this software be liable for any damages whatsoever, including but not limited to, direct, indirect, special, incidental or consequential damages arising out of the use or inability to use this software, even if advised of the possibility of such damages.

This license agreement shall be governed by and construed in accordance with the laws of Canada, without giving effect to any principles of conflicts of law.
