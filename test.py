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
reliablity_percent = 10 / 100

reliablity_end_list = int(len_list * reliablity_percent)
rater2_end_list = int(round(len_list * rater2_percent))
rater3_end_list = int(round(len_list * rater3_percent))

random.shuffle(studyID_list)
reliability_list = []
for i in studyID_list[:reliablity_end_list]:
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

print(rater3)
print(rater2)
print(rater1)

