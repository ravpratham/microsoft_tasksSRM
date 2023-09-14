import pandas as pd
import numpy as np
#Q1
employee = pd.read_csv(r"C:\Users\ravpr\DownloadsEmployee_HR.csv")
print(employee)
print(employee["Department"])
x=employee.loc[((employee["Department"]=="hr") | (employee["Department"]=="marketing")),"Salary_INR"]
print(x)
print(x.var())
print(x.std())
Q3 = np.quantile(x, 0.75)
Q1 = np.quantile(x, 0.25)
IQR = Q3 - Q1
print("IQR",IQR)
#Q2
y=employee.loc[employee["Department"]=="hr",'time_spent_company']
print("range")
print(y.min(),y.max())

#Q3

employee.boxplot(by ='Department', column =['time_spent_company'],grid = False,figsize=(10,10))

#Q4
for i in employee.columns:
    if employee[i].dtype !='O':
        if employee[i].std()==max(employee.std()):
            print("highest standard deviation",i)
