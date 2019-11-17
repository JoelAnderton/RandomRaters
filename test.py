import random

import csv
with open('StudyIDs.csv', 'r') as f:  # open StudyIDs.csv
     reader = csv.reader(f, delimiter=',')
     studyID_list = []
     for i in reader:
         studyID_list.append(i[0])  # add the StudyIDs to the list
     studyID_list.remove(studyID_list[0])  # remove the header


#list1 = [1,2,3,4,5,6,7,8,9,10]

random.shuffle(studyID_list)


len_list = len(studyID_list)
rater2_percent = 40 / 100
rater3_percent = 40 / 100

rater2_end_list = int(len_list * rater2_percent)
rater3_end_list = int(len_list * rater3_percent)

rater2 = []
for i in studyID_list[:rater2_end_list]:
    rater2.append(studyID_list.pop())

rater3 = []
for i in studyID_list[:rater3_end_list]:
    rater3.append(studyID_list.pop())

rater1 = studyID_list
print(rater3)
print(rater2)
print(rater1)

