#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:25:37 2022

@author: paddy
"""

import pandas as pd

# read the data

# short quizzes 1 and 2
sq1 = pd.read_csv('allResults/IC152-Dec2021-Exams-Short Quiz 1-grades.csv',index_col='Email address',na_values='-',skipfooter=1)
sq2 = pd.read_csv('allResults/IC152-Dec2021-Exams-Short quiz 2-grades.csv',index_col='Email address',na_values='-',skipfooter=1)


# prog test1 q1
pt1_1 = pd.read_csv('allResults/IC152_Jan_2022_Prog_Test_One_Q1_Q4_report_2022-01-08T12_19_56.csv',index_col='Candidate Email')
# two batches for q2
pt1_2a = pd.read_csv('allResults/IC152_Jan_2022_Prog_Test_One_Q2A_Q4_report_2022-01-08T12_23_18.csv',index_col='Candidate Email')
pt1_2b = pd.read_csv('allResults/IC152_Jan_2022_Prog_Test_One_Q2B_Q4_report_2022-01-08T12_23_40.csv',index_col='Candidate Email')
# two batches for q3
pt1_3a = pd.read_csv('allResults/IC152_Jan_2022_Prog_Quiz_One_Q3A_Q4_report_2022-01-08T12_24_06.csv',index_col='Candidate Email')
pt1_3b = pd.read_csv('allResults/IC152_Jan_2022_Prog_Test_1_Q3B_Q4_report_2022-01-08T12_26_43.csv',index_col='Candidate Email')
# pt1 q4
pt1_4 = pd.read_csv('allResults/IC152_Jan_2022_Prog_Test_One_Q4_Q4_report_2022-01-08T12_28_30.csv',index_col='Candidate Email')

# prog test 2
pt2_1 = pd.read_csv('allResults/IC152_Feb_2022_Prog_Test_Two_Q1_Q2_report_2022-05-30T16_17_44.csv',index_col='Candidate Email')
pt2_2 = pd.read_csv('allResults/IC152_Feb_2022_Prog_Test_Two_Q2_Q2_report_2022-05-30T16_18_27.csv',index_col='Candidate Email')
# prog test 3
pt3_1 = pd.read_csv('allResults/IC152_Feb_2022_Prog_Test_3_Q1_Q2_report_2022-02-05T10_55_57.csv',index_col='Candidate Email')
pt3_2 = pd.read_csv('allResults/IC152_Feb_2022_Prog_Test_3_Q2_Q2_report_2022-02-05T10_56_13.csv',index_col='Candidate Email')
# re exam May 2022
re_b4 = pd.read_csv('allResults/IC152-Dec2021-Exams-Batch 4-grades.csv',index_col='Email address',na_values='-',skipfooter=1)
re_b3 = pd.read_csv('allResults/IC152-Dec2021-Exams-Batch 3-grades.csv',index_col='Email address',na_values='-',skipfooter=1)
re_b2 = pd.read_csv('allResults/IC152-Dec2021-Exams-Batch 2-grades.csv',index_col='Email address',na_values='-',skipfooter=1)
re_b1 = pd.read_csv('allResults/IC152-Dec2021-Exams-Batch 1-grades.csv',index_col='Email address',na_values='-',skipfooter=1)

# lab marks
lab = pd.read_csv('allResults/labMarks.csv',index_col='Candidate Email')


# replace all nans
sq1.fillna(0,inplace=True)
sq2.fillna(0,inplace=True)
re_b4.fillna(0,inplace=True)
re_b3.fillna(0,inplace=True)
re_b2.fillna(0,inplace=True)
re_b1.fillna(0,inplace=True)
pt1_1.fillna(0,inplace=True)
pt1_2a.fillna(0,inplace=True)
pt1_2b.fillna(0,inplace=True)
pt1_3a.fillna(0,inplace=True)
pt1_3b.fillna(0,inplace=True)
pt1_4.fillna(0,inplace=True)
pt2_1.fillna(0,inplace=True)
pt2_2.fillna(0,inplace=True)
pt3_1.fillna(0,inplace=True)
pt3_2.fillna(0,inplace=True)

# merge the batches of re-exam May 2022
re_all = pd.DataFrame() # empty dataframe
re_all = pd.concat([re_all,re_b1])
re_all = pd.concat([re_all,re_b2])
re_all = pd.concat([re_all,re_b3])
re_all = pd.concat([re_all,re_b4])

# merge the two batches of pt1, question 2
pt1_2 = pd.DataFrame() # empty dataframe
pt1_2 = pd.concat([pt1_2,pt1_2a])
pt1_2 = pd.concat([pt1_2,pt1_2b])

# merge the two batches of pt1, question 3
pt1_3 = pd.DataFrame() # empty dataframe
pt1_3 = pd.concat([pt1_3,pt1_3a])
pt1_3 = pd.concat([pt1_3,pt1_3b])

# merge into single df
#foo = pd.DataFrame()
foo = pd.read_csv('allResults/ic152_dec2021_emails.csv',header=None,index_col=0)
foo['Name'] =  pt1_1['Candidate Name']
print(foo.shape)
#foo['pt1'] =  (pt1_1['Score1'] + pt1_2['Score1'] + pt1_3['Score1'] + pt1_4['Score1'])/4 # made out of 100

foo['pt1'] =  pt1_1['Score1'] + pt1_2['Score1'] 
foo.fillna(0,inplace=True)
print('DEBUG1: ' + str(foo.shape))
foo['pt1'] =  foo['pt1'] + pt1_3['Score1']
foo.fillna(0,inplace=True)
print('DEBUG2: ' + str(foo.shape))
foo['pt1'] =  foo['pt1'] + pt1_4['Score1']
foo.fillna(0,inplace=True)
print('DEBUG3: ' + str(foo.shape))
foo['pt1'] =  foo['pt1']/4
print('DEBUG4: ' + str(foo.shape))


foo['pt2'] =  pt2_1['Score1'] + pt2_2['Score1'] # made out of 100
foo.fillna(0,inplace=True)
foo['pt2'] =  foo['pt2']/2
print('DEBUG5: ' + str(foo.shape))

foo['pt3'] =  pt3_1['Score1'] + pt3_2['Score1'] # made out of 100
foo.fillna(0,inplace=True)
foo['pt3'] =  foo['pt3']/2
print('DEBUG6: ' + str(foo.shape))

# the following line takes the top 2 prog test scores and gives it 20% weightage
foo['top2pt'] = (foo['pt1'] + foo['pt2'] + foo['pt3']-foo[['pt1','pt2','pt3']].min(axis=1))/10 # out of 20
foo.fillna(0,inplace=True)
print('DEBUG7: ' + str(foo.shape))

# two short quizzes of 5% weightage each
foo['sq1'] =  sq1['Grade'] # already out of 5
foo['sq2'] =  (sq2['Grade'])/2 # out of 5
print('DEBUG8: ' + str(foo.shape))

# the re-exam of 60% weightage
foo['reEx'] = re_all['Grade']*6
foo.fillna(0,inplace=True)
print('DEBUG9: ' + str(foo.shape))

# total without lab component, out of 90 marks
#foo['total90'] = foo[['top2pt','sq1','sq2','reEx']].sum(axis=1)

# lab marks
foo['lab'] = lab['Grade']
print('DEBUG10: ' + str(foo.shape))

# total 
foo['total'] = foo[['top2pt','sq1','sq2','reEx','lab']].sum(axis=1)
foo.fillna(0,inplace=True)
print('DEBUG11: ' + str(foo.shape))

# write required columns into csv
foo.to_csv('allData_2.csv')
foo.to_csv('ic152_2021_2.csv', columns=['Name','top2pt','sq1','sq2','reEx','lab','total'], header=['Name','top2pt(20)','sq1(5)','sq2(5)','reEx(60)','lab(10)','total'])




