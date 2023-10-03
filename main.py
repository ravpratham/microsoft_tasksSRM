import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Q1
employee = pd.read_csv(r"Employee_HR.csv")
print(employee.info())
print(employee["Department"])
x=employee.loc[((employee["Department"]=="hr") | (employee["Department"]=="marketing")),"Salary_INR"]
print(x)
print(x.var())
print(x.std())
Q3 = np.quantile(x, 0.75)
Q1 = np.quantile(x, 0.25)
IQR = Q3 - Q1
print("Ans 1. IQR",IQR)
#Q2
y=employee.loc[employee["Department"]=="hr",'time_spent_company']
print("Ans 2. Range", y.min(), y.max())

#Q3
employee.boxplot(by ='Department', column =['time_spent_company'],grid = False,figsize=(10,10))
plt.show()

#Q4
df = employee.loc[:, employee.columns != 'Department']

maxStd = max(df.std())
for i in employee.columns:
    if employee[i].dtype !='O':
        if (employee[i].std()==maxStd):
            print("Ans 4. highest standard deviation",i)
