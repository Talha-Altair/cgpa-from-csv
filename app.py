import pandas as pd

df = pd.read_csv('talha.csv').fillna(0)

num_of_sems = int(len(df.columns)/2)

cols = df.columns

numerator_list = []

cred_list = []

grade_cols = [col for col in cols if 'grade' in col]

cred_cols = [col for col in cols if 'cred' in col]

for i in range(num_of_sems):

    current_numerator = []

    current_cred_list = []

    for grade,cred in zip(df[grade_cols[i]],df[cred_cols[i]]):

        current_offset = grade * cred

        current_numerator.append(current_offset)

        current_cred_list.append(cred)

    numerator_list.extend(current_numerator)

    cred_list.extend(current_cred_list)

    current_gpa = sum(current_numerator)/sum(current_cred_list)

    print(f"Sem {i+1} GPA : {current_gpa}")

cgpa = sum(numerator_list)/sum(cred_list)

print(f"cgpa:{cgpa}")



