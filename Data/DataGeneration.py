# ****************************************************
# Author: @Adjprof
# ****************************************************

# The voter data attributes generation to support a model that allows
# for interactions between state, ethnicity, income, age, sex, education, marriage status and whether a person has children
# 
# the list of attributes: {state, zipcode, ethnicity, income, age, sex, education, marriage, children}
#
# state -> derive from US Census/PII and Voter database
# zipcode -> derive from US Census/PII and Voter database
# ethnicity -> synthetic data derive from US census/PII market
# income -> synthetic data derive from PII market
# age -> derive Voter database
# sex -> derive Voter database (of course, the real gender is subject to data mining from PII and Social Media)
# education -> synthetic data derive from PII market
# marriage -> derive from US Census and Voter database (This field might be outdated; should be pair with data from PII market)
# childen -> synthetic data derive from PII market
# party -> registered party from voter database

import pandas as pd
import csv
import numpy as np
from datetime import date
from random import randrange

# ****************************************************
# data section
# ****************************************************

vf_attributes = ["state_file_id", "dob", "sex", "party", "county__registered_address", "zip__registered_address", "state__registered_address", "federal_district"]
synthetic_data_attributes = ['state', 'zipcode', 'ethnicity', 'income', 'age', 'sex', 'education', 'marriage', 'children', 'party']

# var arrays for synthetic data generation
a_ethnicity = ['NA','White','Black','Mexican','Native Indian','Asian']
v_ethnicity = [0,1,2,3,4,5]
p_ethnicity = [0.1,0.5,0.1,0.05,0.02,0.23]
    
a_income = ['NA', '0-50000', '50001-100000', '100001-150000', '150001-200000', '200001-250000', '250000-']
v_income = [0,1,2,3,4,5,6]
p_income = [0.1,0.5,0.1,0.05,0.02,0.13,0.1]
    
a_education = ['NA','elementary','middle','high','associate','bachelor','master','phd']
v_education = [0,1,2,3,4,5,6,7]
p_education = [0.05,0.05,0.05,0.25,0.075,0.37,0.105,0.05]

a_marriage = ['NA','not married', 'married', 'divorced']
v_marriage = [0,1,2,3]
p_marriage = [0.1,0.5,0.1,0.3]
    
a_children = ['NA', 'one', 'two', 'three', 'four', 'five']
v_children = [0,1,2,3,4,5]
p_children = [0.1,0.4,0.3,0.15,0.04,0.01]
  
# ****************************************************
# code section
# ****************************************************

#
# Input: VF file from voter registration database;  For example, IA-Federal_District-1-VF.csv
# Output: Extracted voter data file based on vf_attributes 
#
def load_VF_data(data_file_name):
    vf_indices = []
    vf_output = []
    with open(data_file_name) as csv_file:
        data_file = csv.reader(csv_file)
        header_ = next(data_file)
        print(header_)
        for index, vf_a in enumerate(vf_attributes):
            vf_indices.append([i for i, elem in enumerate(header_) if vf_a in elem])
        print(vf_indices)

        for i, row_ in enumerate(data_file):
            vf_row = []
            for index, vf_v in enumerate(vf_indices):
                if vf_v[0]==(i for i, elem in enumerate(header_) if 'dob' in elem):
                    vf_row.append(row_[vf_v[0]])
                else:
                    vf_row.append(row_[vf_v[0]])
            vf_output.append(vf_row)
    return vf_output
  
#
# Input: birthday string in MM/DD/YYYY format in according to voter file
# Output: Age based on current time
#
def calc_age(bDay):
    data = bDay.split('/')
    born = date(int(data[2]), int(data[0]), int(data[1]))
    today = date.today()
    if ((today.month, today.day) < (born.month, born.day)):
        extra_year = 1
    else:
        extra_year = 0
    age = today.year - born.year - extra_year
    return age
    
#
# This is an utility function to verify p_* array
# Input: array contain numerical value
# Output: N/A
# Print the total value in percentage from input array
#
def check_percentage(p_arrary):
    _total = 0
    for v in range(len(p_arrary)):
        _total = _total + p_arrary[v]
    if (_total == 1):
        print ("100% met")
    else:
        _delta = 1 - _total
        print ("Delta: %f", _delta) 

# generating the ethnicity, NA|White|Black|Mexican|Indian|Asian to 0|1|2|3|4|5
def generateEthnicity(p_size):
    return np.random.choice(v_ethnicity, p_size, p=p_ethnicity)

# generating the income, NA|0-50000|50001-100000|100001-150000|150001-200000|200001-250000|250000- to 0|1|2|3|4|5|6
def generateIncome(p_size):
    return np.random.choice(v_income, p_size, p=p_income)

# generating the education, NA|elementary|middle|high|associate|bachelor|master|phd to 0|1|2|3|4|5|6|7
def generateEducation(p_size):
    return np.random.choice(v_education, p_size, p=p_education)

# generating the marriage, NA|notmarried|married|divoced to 0|1|2|3
def generateMarriage(p_size):
    return np.random.choice(v_marriage, p_size, p=p_marriage)

# generating the children, NA|one|two|three|four|five to 0|1|2|3|4|5
def generateChildren(p_size):
    return np.random.choice(v_children, p_size, p=p_children)

# convert function on |M|F  to 0|1|2
def convertSex(sex):
    iSex = 0
    if sex == 'M':
        iSex = 1
    if sex == 'F':
        iSex = 2
    return iSex

# convert function on |D|R  to 0|1|2
def convertParty(party):
    iParty = 0
    if party == 'D':
        iParty = 1
    if party == 'R':
        iParty = 2        
    return iParty

#
# This function generate the synthetic data combining the voter database and synthetic data attributes
# Input: vf_output which is the return from load_VF_data function
# Output: synthetic_data in according to synthetic_data_attributes
#
def generateSyntheticData(vf_output):
    synthetic_data = []

    vf_output_Ethnicity = generateEthnicity(len(vf_output))
    vf_output_Income = generateIncome(len(vf_output))
    vf_output_Education = generateEducation(len(vf_output))
    vf_output_Marriage = generateMarriage(len(vf_output))
    vf_output_Children = generateChildren(len(vf_output))

    for i, row_ in enumerate(vf_output):
        sd_row = []
        for index in range(0, 10):
            if index == 0: # state
                sd_row.append(row_[6])
            if index == 1: # zipcode
                sd_row.append(row_[5][:5])
            if index == 2: # ethnicity
                #sd_row.append(randrange(5))
                sd_row.append(vf_output_Ethnicity[i])
            if index == 3: # income
                #sd_row.append(randrange(6))
                sd_row.append(vf_output_Income[i])
            if index == 4: # age
                sd_row.append(calc_age(row_[1]))
            if index == 5: # sex
                sd_row.append(convertSex(row_[2]))
            if index == 6: # education
                #sd_row.append(randrange(5))
                sd_row.append(vf_output_Education[i])
            if index == 7: # marriage
                #sd_row.append(randrange(3))
                sd_row.append(vf_output_Marriage[i])
            if index == 8: # child
                #sd_row.append(randrange(5))
                sd_row.append(vf_output_Children[i])
            if index == 9: # party
                sd_row.append(convertParty(row_[3]))
        synthetic_data.append(sd_row)
    return synthetic_data

#
# Input: sample data output file For example, IA_synthetic_full_data_Output.csv
# Output: The sample data file generated in the file system
#
def output_synthetic_data(data_file_name, synthetic_data):
    with open(data_file_name, mode='w') as csv_file:
        csvWriter = csv.writer(csv_file)
        csvWriter.writerow(synthetic_data_attributes)
        for i, vf_r in enumerate(synthetic_data):
            csvWriter.writerow(vf_r)
        

