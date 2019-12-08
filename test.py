###################################################################################################################
# Randmom Raters
# Created by: Joel Anderton
# Created date: 12/8/2019
# Purpose: To take a list of StudyIDs and randomize it into separate lists for individual lists for raters
#         - The main list is divided up percentage wise for each rater
#         - There is an option for inter-rater reliabilty as a percentage of the total list
#
###################################################################################################################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
import random
import csv


def get_studyID_list(event=None):
    '''Browse to find the list of StudyIDs'''
    global studyID_path
    global StudyID_list_from_csv
    StudyID_list_from_csv = []
    csv_path = askopenfilename()
    pathEntry.insert(END, csv_path)

    with open(pathEntry, 'r') as f:  # open StudyIDs.csv
         reader = csv.reader(f, delimiter=',')
         studyID_list = []
         for i in reader:
             studyID_list.append(i[0])  # add the StudyIDs to the list
         studyID_list.remove(studyID_list[0])  # remove the header


def randomize(studyID_list, rater2_percent, rater3_percent, reliability_percent):
    '''Take the studyID_list and randomize it.'''
    #list1 = [1,2,3,4,5,6,7,8,9,10]
    random.seed(123)
    random.shuffle(studyID_list)


    len_list = len(studyID_list)
    rater2_percent = rater2_percent / 100
    rater3_percent = rater3_percent / 100
    reliability_percent = reliability_percent / 100

    reliability_end_list = int(len_list * reliability_percent)
    rater2_end_list = int(round(len_list * rater2_percent))
    rater3_end_list = int(round(len_list * rater3_percent))

    random.shuffle(studyID_list)
    reliability_list = []
    for i in studyID_list[:reliability_end_list]:
        reliability_list.append(i)

    rater2 = []
    for i in studyID_list[:rater2_end_list]:
        rater2.append(studyID_list.pop())

    rater3 = []
    for i in studyID_list[:rater3_end_list]:
        rater3.append(studyID_list.pop())


    rater1 = studyID_list + reliability_list
    random.shuffle(rater1)
    rater2 = rater2 + reliability_list
    random.shuffle(rater2)
    rater3 = rater3 + reliability_list
    random.shuffle(rater3)

    #print(rater3)
    #print(rater2)
    #print(rater1)

    #for i in rater3:
    #    print(i, end='')

    with open('Rater1.csv', mode='w') as write_file:
        writer = csv.writer(write_file, lineterminator = '\n')
        writer.writerow(['StudyID'])
        for studyID in rater1:
            writer.writerow([studyID])

    with open('Rater2.csv', mode='w') as write_file:
        writer = csv.writer(write_file, lineterminator='\n')
        writer.writerow(['StudyID'])
        for studyID in rater2:
            writer.writerow([studyID])

    with open('Rater3.csv', mode='w') as write_file:
        writer = csv.writer(write_file, lineterminator='\n')
        writer.writerow(['StudyID'])
        for studyID in rater3:
            writer.writerow([studyID])

    with open('ReliabilityList.csv', mode='w') as write_file:
        writer = csv.writer(write_file, lineterminator='\n')
        writer.writerow(['StudyID'])
        for studyID in reliability_list:
            writer.writerow([studyID])

    print('Done!')
def get_about():
    pass


# Creates main window
root = Tk()
root.title('Random Raters v. 1.0')
root.geometry('450x450+500+200')

studyID_path = StringVar()
rater2 = IntVar()
rater3 = IntVar()
rater4 = IntVar()
rater5 = IntVar()
rater6 = IntVar()
rater7 = IntVar()
rater8 = IntVar()
rater9 = IntVar()
rater10 = IntVar()
reliability_percent = IntVar()


# Title
frame = Frame(root)
title = Label(frame, text='Random Raters')
title.pack()
frame.pack()

# Get StudyID Path Box
frame = Frame(root)
pathLabel = Label(frame, text='StudyID List:')
pathLabel.pack(side=LEFT)
pathEntry = Entry(frame, textvariable=studyID_path)
pathEntry.pack(side=LEFT)
getDataButton1 = Button(frame, text='Browse...', command=get_studyID_list, width=10)
getDataButton1.pack(side=LEFT)
frame.pack()

# Rater2 Percentage
frame = Frame(root)
rater2Label = Label(frame, text='Rater2 Percentage:')
rater2Label.pack(side=LEFT)
rater2Entry = Entry(frame, textvariable=rater2, width=3)
rater2Entry.pack(side=LEFT)
frame.pack()

# Rater3 Percentage
frame = Frame(root)
rater3Label = Label(frame, text='Rater3 Percentage:')
rater3Label.pack(side=LEFT)
rater3Entry = Entry(frame, textvariable=rater3, width=3)
rater3Entry.pack(side=LEFT)
frame.pack()

# Rater4 Percentage
frame = Frame(root)
rater4Label = Label(frame, text='Rater4 Percentage:')
rater4Label.pack(side=LEFT)
rater4Entry = Entry(frame, textvariable=rater4, width=3)
rater4Entry.pack(side=LEFT)
frame.pack()

# Rater5 Percentage
frame = Frame(root)
rater5Label = Label(frame, text='Rater5 Percentage:')
rater5Label.pack(side=LEFT)
rater5Entry = Entry(frame, textvariable=rater5, width=3)
rater5Entry.pack(side=LEFT)
frame.pack()

# Rater6 Percentage
frame = Frame(root)
rater6Label = Label(frame, text='Rater6 Percentage:')
rater6Label.pack(side=LEFT)
rater6Entry = Entry(frame, textvariable=rater6, width=3)
rater6Entry.pack(side=LEFT)
frame.pack()

# Rater7 Percentage
frame = Frame(root)
rater7Label = Label(frame, text='Rater7 Percentage:')
rater7Label.pack(side=LEFT)
rater7Entry = Entry(frame, textvariable=rater7, width=3)
rater7Entry.pack(side=LEFT)
frame.pack()

# Rater8 Percentage
frame = Frame(root)
rater8Label = Label(frame, text='Rater8 Percentage:')
rater8Label.pack(side=LEFT)
rater8Entry = Entry(frame, textvariable=rater8, width=3)
rater8Entry.pack(side=LEFT)
frame.pack()

# Rater9 Percentage
frame = Frame(root)
rater9Label = Label(frame, text='Rater9 Percentage:')
rater9Label.pack(side=LEFT)
rater9Entry = Entry(frame, textvariable=rater9, width=3)
rater9Entry.pack(side=LEFT)
frame.pack()

# Rater10 Percentage
frame = Frame(root)
rater10Label = Label(frame, text='Rater10 Percentage:')
rater10Label.pack(side=LEFT)
rater10Entry = Entry(frame, textvariable=rater10, width=3)
rater10Entry.pack(side=LEFT)
frame.pack()

frame = Frame(root)
lines = Label(frame, text='')
lines.pack()
frame.pack()


# Reliability Percentage
frame = Frame(root)
reliabilityLabel = Label(frame, text='Reliability Percentage:')
reliabilityLabel.pack(side=LEFT)
reliabilityEntry = Entry(frame, textvariable=reliability_percent, width=3)
reliabilityEntry.pack(side=LEFT)
frame.pack()

# Submit button
frame = Frame()
submitButton = Button(frame, text='Submit', command=randomize, width=10)
submitButton.pack()
frame.pack()

# Close button
frame = Frame()
closeButton = Button(frame, text='Close', command=root.destroy, width=10)
closeButton.pack()
frame.pack()

#About button
frame = Frame()
closeButton = Button(frame, text='About', command=get_about, width=10)
closeButton.pack()
frame.pack()

root.mainloop()

