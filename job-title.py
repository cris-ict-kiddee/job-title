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

#Print a gender title infront of their name
def gender(gender_code):
    '''TODO: add a docstring comment to every function definition, describing what it does, what arguments are passed in, and what value is returned'''
    if gender_code  == 'M' :
        gc = "Mr."
    else:
        gc = "Ms."

    return gc


def seniority(age):
    '''Print thier seniority infront of their job to justify their age'''
    if age < 25 :
        ag = "Jr. "
    elif age >= 35 :
        ag = "Sr. "
    else:
        ag = ""

    return ag


def job_title(first_name):
    """Return the job string given first name """
    if first_name in engineers:
        if first_name in managers:
            jb = "Engineering Manager"
        else:
            jb = "Engineer"
    else: #Not a engineer
        if first_name in managers:
            jb = "Manager"
        else:
            jb = "Employees"    

    return jb


def employee_job_title(first_name):
    """returns a string containing an employees' full job title given a string `first_name`"""
    ftname = data['first_name']
    lsname = data['last_name']

    #get their gender
    gen = gender(data['gender_code'])

    #get their seniority
    age = seniority(data['age'])

    # get their job title
    job = job_title(data['first_name'])

    # TODO an f-string might be easier to read
    return (f"{gen} {ftname} {lsname}, {age}{job}")


# check for proper command line arguments or print usage and exit
if len(sys.argv) == 2:
    # print 1 employee giving first name argument 
    command = sys.argv[1]
    first_name = command.title()
    # get the employee dictionary for this first_name
    data = employee_data(first_name)
    if data == None:
        print("no such employee: {first_name}", file=sys.stderr)
        sys.exit(1)
    output = employee_job_title(data)
    print(output)
elif len(sys.argv) == 1:
    #print all employee
    for data in employees:
        output = employee_job_title(data)
        print(output)
else:
    print("usage: job-title.py <first_name>", file=sys.stderr)
    sys.exit(1)

# TODO print error message "no such employee: {first_name}" and exit if data == None

# this is how we print one job title,
# TODO how would we print all job titles?
