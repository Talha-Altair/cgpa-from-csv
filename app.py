import pandas as pd

df = pd.read_csv('grades.csv').fillna(0)

num_of_sems = int(len(df.columns)/2)

cols = df.columns

numerator_list = []

cred_list = []

grade_cols = [col for col in cols if 'grade' in col]

cred_cols = [col for col in cols if 'cred' in col]

for i in range(num_of_sems):

    for grade,cred in zip(df[grade_cols[i]],df[cred_cols[i]]):

        current_offset = grade * cred

        numerator_list.append(current_offset)

        cred_list.append(cred)

cgpa = sum(numerator_list)/sum(cred_list)

print(cgpa)



