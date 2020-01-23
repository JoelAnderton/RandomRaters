###################################################################################################################
# Random Raters
# Created by: Joel Anderton
# Created date: 12/9/2019
# Purpose: To take a list of StudyIDs and randomize it into separate lists for individual lists for raters
#         - The main list is divided up percentage wise for each rater
#         - There is an option for inter-rater reliability as a percentage of the total list
#
###################################################################################################################

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import random
import csv


def get_studyID_list(event=None):
    """Browse to find the list of StudyIDs"""
    global csv_path
    global studyID_list
    studyID_list = []
    csv_path = askopenfilename()
    pathEntry.insert(END, csv_path)


def randomize(event=None):
    """Take the studyID_list and randomize it."""
    # opens .csv file
    studyID_list = []
    with open(pathEntry.get(), 'r') as f:
        reader = csv.reader(f, delimiter=',')  # reads in .csv file
        if header.get() == True:
            next(reader)
        for rowDict in reader:
            studyID = rowDict[0].upper()  # if the StudyID is typed in lowercase, this changes it to uppercase
            studyID_list.append(studyID)

    # Check raters total 100%
    total_raters = update_rater1()
    if total_raters < 1 or total_raters > 99:
        messagebox.showwarning('Error', 'Total of all percentages do not total 100%')
    else:
        # Check reliability < 100%
        if check_reliability() == 1:

            reliability = int(reliabilityEntry.get())
            rater2 = int(rater2Entry.get())
            rater3 = int(rater3Entry.get())
            rater4 = int(rater4Entry.get())
            rater5 = int(rater5Entry.get())
            rater6 = int(rater6Entry.get())
            rater7 = int(rater7Entry.get())
            rater8 = int(rater8Entry.get())
            rater9 = int(rater9Entry.get())
            rater10 = int(rater10Entry.get())

            reliability_list = []

            # Shuffle list
            random.seed(123)
            random.shuffle(studyID_list)

            # Find List Length
            len_list = len(studyID_list)

            # Create reliability list
            if reliability >= 1:
                reliability_percent = reliability / 100
                reliability_end_list = int(len_list * reliability_percent)
                for i in studyID_list[:reliability_end_list]:
                    reliability_list.append(studyID_list.pop())

                with open('ReliabilityList.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in sorted(reliability_list):
                        writer.writerow([studyID])
                len_list = len(studyID_list) #reset list length

            # Create rater2 list
            if rater2 >= 1:
                rater2_percent = rater2 / 100
                rater2_end_list = int(round(len_list * rater2_percent))
                rater2_list = []
                for i in studyID_list[:rater2_end_list]:
                    rater2_list.append(studyID_list.pop())

            # Create rater 3 list
            if rater3 >= 1:
                rater3_percent = rater3 / 100
                rater3_end_list = int(round(len_list * rater3_percent))
                rater3_list = []
                for i in studyID_list[:rater3_end_list]:
                    rater3_list.append(studyID_list.pop())

            # Create rater 4 list
            if rater4 >= 1:
                rater4_percent = rater4 / 100
                rater4_end_list = int(round(len_list * rater4_percent))
                rater4_list = []
                for i in studyID_list[:rater4_end_list]:
                    rater4_list.append(studyID_list.pop())

            # Create rater 5 list
            if rater5 >= 1:
                rater5_percent = rater5 / 100
                rater5_end_list = int(round(len_list * rater5_percent))
                rater5_list = []
                for i in studyID_list[:rater5_end_list]:
                    rater5_list.append(studyID_list.pop())

            # Create rater 6 list
            if rater6 >= 1:
                rater6_percent = rater6 / 100
                rater6_end_list = int(round(len_list * rater6_percent))
                rater6_list = []
                for i in studyID_list[:rater6_end_list]:
                    rater6_list.append(studyID_list.pop())

            # Create rater 7 list
            if rater7 >= 1:
                rater7_percent = rater7 / 100
                rater7_end_list = int(round(len_list * rater7_percent))
                rater7_list = []
                for i in studyID_list[:rater7_end_list]:
                    rater7_list.append(studyID_list.pop())

            # Create rater 8 list
            if rater8 >= 1:
                rater8_percent = rater8 / 100
                rater8_end_list = int(round(len_list * rater8_percent))
                rater8_list = []
                for i in studyID_list[:rater8_end_list]:
                    rater8_list.append(studyID_list.pop())

            # Create rater 9 list
            if rater9 >= 1:
                rater9_percent = rater9 / 100
                rater9_end_list = int(round(len_list * rater9_percent))
                rater9_list = []
                for i in studyID_list[:rater9_end_list]:
                    rater9_list.append(studyID_list.pop())

            # Create rater 10 list
            if rater10 >= 1:
                rater10_percent = rater10 / 100
                rater10_end_list = int(round(len_list * rater10_percent))
                rater10_list = []
                for i in studyID_list[:rater10_end_list]:
                    rater10_list.append(studyID_list.pop())

            # Rater1 List - csv
            rater1 = sorted(list(set(studyID_list + reliability_list)))
            with open('Rater1.csv', mode='w') as write_file:
                writer = csv.writer(write_file, lineterminator='\n')
                writer.writerow(['StudyID'])
                for studyID in rater1:
                    writer.writerow([studyID])

            # Rater2 List - csv
            if rater2 >= 1:
                rater2_list_all = sorted(list(set(rater2_list + reliability_list)))
                with open('Rater2.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater2_list_all:
                        writer.writerow([studyID])

            # Rater3 List - csv
            if rater3 >= 1:
                rater3_list_all = sorted(list(set(rater3_list + reliability_list)))
                with open('Rater3.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater3_list_all:
                        writer.writerow([studyID])

            # Rater4 List - csv
            if rater4 >= 1:
                rater4_list_all = sorted(list(set(rater4_list + reliability_list)))
                with open('Rater4.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater4_list_all:
                        writer.writerow([studyID])

            # Rater5 List - csv
            if rater5 >= 1:
                rater5_list_all = sorted(list(set(rater5_list + reliability_list)))
                with open('Rater5.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater5_list_all:
                        writer.writerow([studyID])

            # Rater6 List - csv
            if rater6 >= 1:
                rater6_list_all = sorted(list(set(rater6_list + reliability_list)))
                with open('Rater6.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater6_list_all:
                        writer.writerow([studyID])

            # Rater7 List - csv
            if rater7 >= 1:
                rater7_list_all = sorted(list(set(rater7_list + reliability_list)))
                with open('Rater7.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater7_list_all:
                        writer.writerow([studyID])

            # Rater8 List - csv
            if rater8 >=1:
                rater8_list_all = sorted(list(set(rater8_list + reliability_list)))
                with open('Rater8.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater8_list_all:
                        writer.writerow([studyID])

            # Rater9 List - csv
            if rater9 >=1:
                rater9_list_all = sorted(list(set(rater9_list + reliability_list)))
                with open('Rater9.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater9_list_all:
                        writer.writerow([studyID])

            # Rater10 List - csv
            if rater10 >=1:
                rater10_list_all = sorted(list(set(rater10_list + reliability_list)))
                with open('Rater10.csv', mode='w') as write_file:
                    writer = csv.writer(write_file, lineterminator='\n')
                    writer.writerow(['StudyID'])
                    for studyID in rater10_list_all:
                        writer.writerow([studyID])

            messagebox.showinfo('Done', 'Done!')


def update_rater1():
    """Updates Rater1 percentage"""
    new_rater1 = 100 - (rater2.get() + rater3.get() + rater4.get() + rater5.get() + rater6.get() + rater7.get() +
                        rater8.get() + rater9.get() + rater10.get())
    return new_rater1


def check_reliability():
    """Check that the Reliability percentage is between 0 and 100%"""
    if reliability_percent.get() < 0 or reliability_percent.get() > 100:
        messagebox.showwarning('Error', 'Reliability percent is not between 0 and 100%')
        return 0
    else:
        return 1


def callback(*args):
    """Automatically updates Rater1 Percentage when the percentages of other raters changes"""
    new_rater1 = update_rater1()
    rater1_percent.configure(state='normal')
    rater1.set(new_rater1)
    rater1_percent.configure(state='disable')


def get_about():
    messagebox.showinfo('About', '''    Created by: Joel Anderton 
        Created date: 12/9/2019

        Random Raters
        version: 1.1''')


# Creates main window
root = Tk()
root.title('Random Raters v. 1.1')
root.geometry('450x550+500+200')

studyID_path = StringVar()
header = BooleanVar()
rater1 = IntVar()
rater2 = IntVar()
rater3 = IntVar()
rater4 = IntVar()
rater5 = IntVar()
rater6 = IntVar()
rater7 = IntVar()
rater8 = IntVar()
rater9 = IntVar()
rater10 = IntVar()
reliabilityType = IntVar()
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

# Header checkbox
frame = Frame(root)
headerCheckBut = Checkbutton(frame, text='Header in first row?', variable=header)
headerCheckBut.pack()
frame.pack()

# Rater1
frame = Frame(root)
rater1Label = Label(frame, text='Rater1 Percentage')
rater1Label.pack(side=LEFT)
rater1_percent = Entry(frame, textvariable=rater1, width=3, state='disabled')
rater1.set(50)
rater1_percent.pack(side=RIGHT)
frame.pack()

# Rater2 Percentage
frame = Frame(root)
rater2Label = Label(frame, text='Rater2 Percentage:')
rater2Label.pack(side=LEFT)
rater2Entry = Entry(frame, textvariable=rater2, width=3)
rater2.set(50)
rater2Entry.pack(side=LEFT)
frame.pack()

# Rater3 Percentage
frame = Frame(root)
rater3Label = Label(frame, text='Rater3 Percentage:')
rater3Label.pack(side=LEFT)
rater3Entry = Entry(frame, textvariable=rater3, width=3)
rater3.set(0)
rater3Entry.pack(side=LEFT)
frame.pack()

# Rater4 Percentage
frame = Frame(root)
rater4Label = Label(frame, text='Rater4 Percentage:')
rater4Label.pack(side=LEFT)
rater4Entry = Entry(frame, textvariable=rater4, width=3)
rater4.set(0)
rater4Entry.pack(side=LEFT)
frame.pack()

# Rater5 Percentage
frame = Frame(root)
rater5Label = Label(frame, text='Rater5 Percentage:')
rater5Label.pack(side=LEFT)
rater5Entry = Entry(frame, textvariable=rater5, width=3)
rater5.set(0)
rater5Entry.pack(side=LEFT)
frame.pack()

# Rater6 Percentage
frame = Frame(root)
rater6Label = Label(frame, text='Rater6 Percentage:')
rater6Label.pack(side=LEFT)
rater6Entry = Entry(frame, textvariable=rater6, width=3)
rater6.set(0)
rater6Entry.pack(side=LEFT)
frame.pack()

# Rater7 Percentage
frame = Frame(root)
rater7Label = Label(frame, text='Rater7 Percentage:')
rater7Label.pack(side=LEFT)
rater7Entry = Entry(frame, textvariable=rater7, width=3)
rater7.set(0)
rater7Entry.pack(side=LEFT)
frame.pack()

# Rater8 Percentage
frame = Frame(root)
rater8Label = Label(frame, text='Rater8 Percentage:')
rater8Label.pack(side=LEFT)
rater8Entry = Entry(frame, textvariable=rater8, width=3)
rater8.set(0)
rater8Entry.pack(side=LEFT)
frame.pack()

# Rater9 Percentage
frame = Frame(root)
rater9Label = Label(frame, text='Rater9 Percentage:')
rater9Label.pack(side=LEFT)
rater9Entry = Entry(frame, textvariable=rater9, width=3)
rater9.set(0)
rater9Entry.pack(side=LEFT)
frame.pack()

# Rater10 Percentage
frame = Frame(root)
rater10Label = Label(frame, text='Rater10 Percentage:')
rater10Label.pack(side=LEFT)
rater10Entry = Entry(frame, textvariable=rater10, width=3)
rater10.set(0)
rater10Entry.pack(side=LEFT)
frame.pack()

frame = Frame(root)
lines = Label(frame, text='')
lines.pack()
frame.pack()

# Reliability type
frame = Frame(root)
reliabilityTypeLabel = Label(frame, text='Choose Reliability Type:')
reliabilityTypeLabel.pack(side=LEFT)
frame.pack()

frame = Frame(root)
radio_same = Radiobutton(frame, text="Same Across All", padx=20, variable=reliabilityType, value=1)
radio_same.pack()
radio_one = Radiobutton(frame, text="1 on 1                ", padx=20, variable=reliabilityType, value=2)
radio_one.pack()
frame.pack()

# Reliability Percentage
frame = Frame(root)
reliabilityLabel = Label(frame, text='Reliability Percentage:')
reliabilityLabel.pack(side=LEFT)
reliabilityEntry = Entry(frame, textvariable=reliability_percent, width=3)
reliabilityEntry.pack(side=LEFT)
frame.pack()

rater2.trace("w", callback)
rater3.trace("w", callback)
rater4.trace("w", callback)
rater5.trace("w", callback)
rater6.trace("w", callback)
rater7.trace("w", callback)
rater8.trace("w", callback)
rater9.trace("w", callback)
rater10.trace("w", callback)
reliability_percent.trace("w", callback)

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

# About button
frame = Frame()
closeButton = Button(frame, text='About', command=get_about, width=10)
closeButton.pack()
frame.pack()

root.mainloop()

