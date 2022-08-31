import csv
import json
import os


# create a csv file
if(os.path.exists("users.csv")):
    pass
else:
    with open('users.csv','w') as user_csv_file:
        pass

#open csv file
with open('stud_course_database.csv', 'r') as csvfile:
    #traverse csv file
    courses = []
    emails = []
    users = []
    data = []
    names = []
    phones = []
    for row in csv.reader(csvfile):
        temp = []
        if row[2].strip().upper() not in courses:
            courses.append(row[2].strip().upper())
        name = row[1].strip()
        if name not in names:
            names.append(name)
        email = row[3].strip()
        if email not in emails:
            emails.append(email)
        phone = row[4].strip()
        if phone not in phones:
            phones.append(phone)
        temp = [name, email, phone]
        data.append(temp)

    
    
    print("length of data without any striping",1686) #1686
    print("length of data after stripping",len(data)) #1686

    print(len(names)) #unique names
    print(len(emails)) #unique emails
    print(len(phones)) #unique phones

    print(courses)
    print(len(courses))

    java_category = [i for i in courses if 'JAVA' in i]
    print(java_category)

    python_category = [i for i in courses if 'PYTHON' in i]
    print(python_category)

    dot_net_category = [i for i in courses if 'NET' in i]
    print(dot_net_category)

    test_category = [i for i in courses if 'TEST' in i]
    print(test_category)

    other_category = [i for i in courses if i not in java_category and i not in python_category and i not in dot_net_category and i not in test_category]
    print(other_category)

    with open('courses.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for course in courses:
            writer.writerow([course])
    
    with open('users.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for user in data:
            writer.writerow(user)
        
