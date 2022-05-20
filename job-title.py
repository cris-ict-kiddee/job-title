#!/usr/bin/python3

# Kiddee Grade 8
# Booleans & Conditionals - Job Titles
# This program will accept a predefined employee's first name as a command line argument and print their employee title as: gender title, full name, and job title of the employee in the form

### START - DO NOT EDIT ###
import sys

# list of dictionaries of employee data
# (gender_code must be only 'M' for male or 'F' for female)
employees = [
    {
        'first_name': 'John',
        'last_name': 'Smith',
        'age': 23,
        'gender_code': 'M'
    },
    {
        'first_name': 'Joe',
        'last_name': 'Ruddy',
        'age': 33,
        'gender_code': 'M'
    },
    {
        'first_name': 'Jenny',
        'last_name': 'McPherson',
        'age': 24,
        'gender_code': 'F'
    },
    {
        'first_name': 'Janice',
        'last_name': 'Johnson',
        'age': 33,
        'gender_code': 'F'
    },
    {
        'first_name': 'Jill',
        'last_name': 'Lancaster',
        'age': 46,
        'gender_code': 'F'
    }
]

engineers = ['Joe', 'Jenny']
managers = ['Joe', 'Jill']

def employee_data(first_name):
    ''' return the dictionary for an employee if exists, or None '''
    for data in employees:
        if data['first_name'] == first_name:
            return data
    return None

### END - DO NOT EDIT ###

### EDIT HERE ### 

# check for proper command line arguments or print usage and exit
if len(sys.argv) != 2:
    print("usage: job-title.py <first_name>", file=sys.stderr)
    sys.exit(1)

# get the first_name from the command line argument
command = sys.argv[1]
first_name = command.title()

# get the employee dictionary for this first_name
data = employee_data(first_name)

#get all of their data for each person

ftname = data['first_name']
lsname = data['last_name']

#get their gender

def gender(gender_code):
    if gender_code  == 'M' :
        gc = "Mr."
        return gc
    else:
        gc = "Ms."
        return gc

gen = gender(data['gender_code'])

#get their seniority

def seniority(age):
    if age < '25' :
        ag = "Jr."
    else:
        ag = "Sr."
        return ag

age = seniority(data['age'])

print (gen + ftname + ' ' + lsname + ',' + ' ' + age)
