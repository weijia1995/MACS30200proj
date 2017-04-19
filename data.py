#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:29:41 2017

@author: wli
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os


cur_path = os.path.split(os.path.abspath(__file__))[0]
output_fldr = 'images'
output_dir = os.path.join(cur_path, output_fldr)
if not os.access(output_dir, os.F_OK):
    os.makedirs(output_dir)
    
# Income

df = pd.read_fwf('jan16pub.dat', header = None)
income = pd.DataFrame(df[2].apply(lambda x: x[1:3])).astype(int)
income.columns = ['income']
income[income==-1]=0
print('income data')
print(income.describe())


fig = plt.figure()
sns.countplot(income['income'])
#ax = sns.distplot(income, bins = 16)
#plt.xlim(0,17)
#plt.xlabel('income group')
#plt.ylabel('frequency')
plt.title('income distribution')
output_path = os.path.join(output_dir, "income.png")
plt.savefig(output_path, bbox_inches='tight')



# Race
race = df[13].apply(lambda x: x[25:27]).astype(int)
race[race==-1]=0
income['race'] = race
print('')      
print('race data')
print(income.race.describe())
r = sns.jointplot(x="race", y="income", data=income, color="m")
output_path = os.path.join(output_dir, "income-race.png")
plt.savefig(output_path, bbox_inches='tight')


# Household type
household = df[5]
income['household'] = household
print('')      
print('household type')
print(income.household.describe())
h = sns.jointplot(x="household", y="income", data=income, kind='reg', color = 'lightcoral')
output_path = os.path.join(output_dir, "income-houseshold.png")
plt.savefig(output_path, bbox_inches='tight')


# Employment
employment = df[13].apply(lambda x: x[68:70]).astype(int)
employment[employment==-1] = 0
employment[employment==-3]=0
employment[employment==-2]=0
income['employment'] = employment
print('')      
print('employment data')
print(income.employment.describe())
e = sns.jointplot(x="employment", y="race", data=income, color="m")
output_path = os.path.join(output_dir, "employment-race.png")
plt.savefig(output_path, bbox_inches='tight')


# Gender
gender = df[13].apply(lambda x: x[15:17]).astype(int)
gender[gender==-1]=0
income['gender'] = gender
print('')      
print('gender data')
print(income.gender.describe())

plt.figure()
ge = sns.barplot(x=income['gender'], y=income["employment"],palette="BuPu")
plt.title('Employment - Gender')
output_path = os.path.join(output_dir, "employment-gender.png")
plt.savefig(output_path, bbox_inches='tight')


#Education
edu = df[13].apply(lambda x: x[23:25]).astype(int)
edu[edu==-1]=0
income['edu'] = edu
print('')      
print('education data')
print(income.edu.describe())
ei = sns.barplot(x=income['edu'], y=income["income"],palette="coolwarm")
















