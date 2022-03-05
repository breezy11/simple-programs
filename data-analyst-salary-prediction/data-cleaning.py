# Imports
import pandas as pd
import numpy as np

# import data
df = pd.read_csv("data/old-data.csv")

# disable the 'A value is trying to be set on a copy of a slice from a DataFrame' warning
pd.options.mode.chained_assignment = None

# salary parsing (avg salary values left)
df = df[df["Salary Estimate"] != '-1']
salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$', '')).values
df["avg salary"] = np.zeros(df.shape[0])

for i in range(df.shape[0]):
    min_max = minus_Kd[i].split('-')
    df["avg salary"].iloc[i] = (float(min_max[0]) + float(min_max[1])) / 2

# print(df["avg salary"].to_string())

df.drop("Salary Estimate", inplace=True, axis=1)

# dropped the columns that do not have a rating
df = df[df["Rating"] != -1.0]

# company name text only

df["Company Name"] = df["Company Name"].apply(lambda x: x[:-5])
# print(df["Company Name"].to_string())

# state column, city column
df["state"] = df['Location'].apply(lambda x: x.split(',')[1])
df["city"] = df['Location'].apply(lambda x: x.split(',')[0])

df.drop('Location', inplace=True, axis=1)

# rename columns so it's consistent
df.rename(columns={'Rating': 'rating', 'Company Name': 'company'}, inplace=True)

# drop headquarters column
df.drop("Headquarters", inplace=True, axis=1)

# company age
df['age'] = df["Founded"].apply(lambda x: x if x <1 else 2020 - x)
df.drop("Founded", inplace=True, axis=1)

# job description parsing

# SAS
df["sas_yn"] = df["Job Description"].apply(lambda x: 1 if 'sas' in x.lower() else 0)
# spark
df["spark_yn"] = df["Job Description"].apply(lambda x: 1 if 'spark' in x.lower() else 0)
# python
df["python_yn"] = df["Job Description"].apply(lambda x: 1 if 'python' in x.lower() else 0)
# matlab
df["matlab_yn"] = df["Job Description"].apply(lambda x: 1 if 'matlab' in x.lower() else 0)
# excel
df["excel_yn"] = df["Job Description"].apply(lambda x: 1 if 'excel' in x.lower() else 0)
# jupyter
df["jupyter_yn"] = df["Job Description"].apply(lambda x: 1 if 'jupyter' in x.lower() else 0)
# sql
df["sql_yn"] = df["Job Description"].apply(lambda x: 1 if 'sql' in x.lower() else 0)
# spss
df["spss_yn"] = df["Job Description"].apply(lambda x: 1 if 'spss' in x.lower() else 0)

# drop first unnamed column
df.drop("Unnamed: 0", inplace=True, axis=1)

# print(df.columns)

# job titles are mostly the same, there are some differences between industries but mostly the same, so just differentiate sr. jr.

def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
            return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower():
        return 'jr'
    else:
        return 'na'

# seniority category
df['seniority'] = df['Job Title'].apply(seniority)

# job description length
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))

##  Competitor count
df['comp_num'] = df['Competitors'].apply(lambda x: len(x.split(',')) if x != '-1' else 0)

# export cleaned data
df.to_csv("data/data.csv", index=False)