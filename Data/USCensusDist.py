# var arrays for data generation
# Karel Reference: https://docs.google.com/spreadsheets/d/1Gb38KrcM2-jBIe5gM4trRERyqQC2IQ19giuB2weadUc/edit?usp=sharing

# based on US Census summary by Karel
a_ethnicity = ['NA','White','Black','Mexican','Native Indian','Asian']
v_ethnicity = [0,1,2,3,4,5]
p_ethnicity = [0.0,0.92,0.05,0.005,0.005,0.02]
    
# based on US Census summary by Karel
a_income = ['0-14999', '15000-34999', '35000-49999', '50000-74900', '75000-99999', '100000-149000', '150000-']
v_income = [0,1,2,3,4,5,6]
p_income = [0.11,0.2,0.13,0.2,0.14,0.12,0.1]
    
# based on US Census summary by Karel
a_education = ['NA','elementary','middle','high','associate','bachelor','master','phd']
v_education = [0,1,2,3,4,5,6,7]
p_education = [0,0.03,0.05,0.33,0.32,0.19,0.07,0.01]

# based on US Census summary by Karel
a_marriage = ['widowed','not married', 'married', 'divorced']
v_marriage = [0,1,2,3]
p_marriage = [0.08,0.3,0.5,0.12]
    
a_children = ['NA', 'one', 'two', 'three', 'four', 'five']
v_children = [0,1,2,3,4,5]
p_children = [0.7,0.2,0.07,0.01,0.01,0.01]
    
