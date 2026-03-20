# def mul(a,b):
#     return print("The multiplication of ",a,"and",b,":",a*b)

# a = int(input("Enter the first number = "))
# b = int(input("Enter the second number = "))
# mul(a,b)


import pandas as pd

# df = pd.DataFrame([11,22,33],columns= ['col_Name'])
# print(df)



data = {
    'Name' : ['Madhav','Vishakha','Lalita','Rishabh'],
    'Age' : [16,17,18,19],
    "Salary" : [9000,7000,5000,3000]
}
df = pd.DataFrame(data)
# print(df)


# data = {
#     'Name' : ['Madhav','Vishakha'],
#     'Age' : [16,17],
#     "Salary" : [9000,7000]
# }
# df = pd.DataFrame(data)
# print(df)


# print(df.shape)


# print(df.columns)

df.rename(columns={'Salary':'Monthly_Salary'},inplace=True)
# print(df)


# df.info()


# df.describe()


# df.to_csv('Test_data.scv',index=False)

# load_df= pd.read_csv('Test_data.csv')
# load_df


#df.loc:[df.Name=='Madhav'] # type: ignore

# df[['Name','Monthly_salary']]


# df_age_filter = df[df['Age']>=18] 
# print(df_age_filter)


#print(df.where(df['Age']>=18))


#print(df.where(df['Age']>=18,other='Not Eligible'))


# df['Team'] = ['CEO','HR','CTO','DA']
# print(df)

# df['Bonus'] = df['Monthly_Salary']*0.20
# print(df)

#df.loc[len(df)]=['Yash',21,2100,'IT',2000]
# print(df)


# df.loc[0,'Monthly_Salary'=100000]
# print(df)


# df = df.drop(df[df.Name == 'Yash'].index)
# df.drop(1,axis=5)
#print(df)


# df = df.drop(df[df.Name == 'ABC'].index)
# print(df)

# df.drop('Bonus',axis=1,inplace=True)
# print(df)


df.rename(columns={'Monthly_Salary':'Salary'},inplace=True)
# df.sort_values('Salary')
# print(df)


#df['DOJ'] = ['2024-02-02','2024-02-24','2024-03-28','2024-02-03']
# print(df)
# print(df['DOJ'].dtype)


#df['DOJ']=pd.to_datetime(df['DOJ'])
#print(df)
#print(df['DOJ'].dtype)

#df['DOJ']+pd.Timedelta(Days=90)


#df.isnull()
#print(df)


import numpy as np
#df.loc[df.Name=='Rishabh','Salary'] = np.nan

#df.isnull().sum()


#df['Month'].value_counts()
#print(df)



