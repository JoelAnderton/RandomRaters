#############################################################################################
# Created by: Joel Anderton
# Created date: 6/8/2018
#
# Purpose: to give 3 raters each a random list of StudyIDs based on a large list of StudyIDs
#          Each list should be unique and not repeat any StudyIDs
#
#############################################################################################

import random
#import pandas as pd


##########################################################
# Use this code below if pandas is installed
#df = pd.read_csv('StudyIDs.csv')
#studyID_list = []  # List of StudyIDs
#for i in df['StudyID']:
#    studyID_list.append(i)  # appends all the StudyIDs to to studyID_list
##########################################################


###########################################################
# Use the code below if pandas is not installed:
import csv
with open('StudyIDs.csv', 'r') as f:  # open StudyIDs.csv
     reader = csv.reader(f, delimiter=',')
     studyID_list = []
     for i in reader:
         studyID_list.append(i[0])  # add the StudyIDs to the list
     studyID_list.remove(studyID_list[0])  # remove the header
##########################################################


rater1 = []  # List of StudyIDs for Rater1
rater2 = []  # List of StudyIDs for Rater2
rater3 = []  # List of StudyIDs for Rater3

studyID_list_length = len(studyID_list)  # total number of StudyIDs

counter = 0
while counter < studyID_list_length:

    # Adds StudyIDs to Rater1's list
    if counter == studyID_list_length:  # if the the end of the StudyID list been reached, exit loop
        break
    else:
        studyID = random.choice(studyID_list)  # chooses a random StudyID
        rater1.append(studyID)  # adds the random StudyID to Rater1's list
        counter += 1  # marks that a StudyID has been used
        studyID_list.remove(studyID)  # removes that StudyID from the list of available StudyIDs to choose from

    # Adds StudyIDs to Rater2's list
    if counter == studyID_list_length:  # if the the end of the StudyID list been reached, exit loop
        break
    else:
        studyID = random.choice(studyID_list)  # chooses a random StudyID
        rater2.append(studyID)  # adds the random StudyID to Rater1's list
        counter += 1  # marks that a StudyID has been used
        studyID_list.remove(studyID)  # removes that StudyID from the list of available StudyIDs to choose from

    # Adds StudyIDs to Rater3's list
    if counter == studyID_list_length:  # if the the end of the StudyID list been reached, exit loop
        break
    else:
        studyID = random.choice(studyID_list)  # chooses a random StudyID
        rater3.append(studyID)  # adds the random StudyID to Rater1's list
        counter += 1  # marks that a StudyID has been used
        studyID_list.remove(studyID)  # removes that StudyID from the list of available StudyIDs to choose from

# Prints out the Rater's lists
print("Rater1: ", rater1)
print("Rater2: ", rater2)
print("Rater3: ", rater3)
