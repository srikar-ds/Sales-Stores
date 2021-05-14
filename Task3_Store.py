import pandas as pd
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

# TASK 1 :PERFROM EDA for given data set

store = pd.read_csv("C:/The Sparks Foundation/SampleSuperstore.csv")
# in the big picture, we know its the sales that drives the Profits.
# say the clients requirment to deal
# with worst performing areas.

store.head()
# gives the top 5 values from dataset 


# cleanse data set, inorder 
store.isnull()

# check biz moment, gives weightage of data
store.describe()
store.shape

store.drop_duplicates()

store=store.drop('Country',axis = 1)
store['Category'].unique()
store['Category'].value_counts()
store['Sub-Category'].value_counts()
store['Segment'].value_cou
# Data Visulisation 
store.plot() # crude idea 

sns.pairplot(store, height=2.0,diag_kind="kde",x_vars= None, y_vars= None )
# or diag_kind =None, only a diff representation of the pairwise graphs
sns.heatmap(correlation, xticklabels = correlation.columns, yticklabels = correlation.columns, annot = True)


# correlation matrix
correlation= store.corr()





###################
# Numerical data & Categorical data 
numerical_data = store.select_dtypes(include = [np.number]) #select_dtypes func. used for separation columns either inclusing/excluding them

categorical_data = store.select_dtypes(exclude = [np.number])
categorical_data

## UNIVARIENT ANALYSIS OF IMPORTANT FACTORS DRIVING PROFITS,
## SO BREAK DOWN IN THIS CASE, CHECK FOR CATOGORY,REGION & SEGMENTS

#Shipping Mode Countplot and Pie-chart

plt.figure(figsize = (7,5))
sns.countplot(store["Ship Mode"])
plt.show()

plt.figure(figsize = (5,5))
plt.pie(store["Ship Mode"].value_counts(), labels = store["Ship Mode"].value_counts().index, autopct = "%.2f%%", 
        explode = [0.1,0,0,0])
plt.show()

plt.figure(figsize = (7,5))
sns.countplot(store["Segment"])
plt.show()

plt.figure(figsize = (5,5))
plt.pie(store["Segment"].value_counts(), labels = store["Segment"].value_counts().index, autopct = "%.2f%%", 
        explode = [0.1,0,0])
plt.show()


## thereby we know store delivery traffic is most via Standard Class

plt.figure(figsize = (7,5))
sns.countplot(store["Category"])
plt.show()


plt.figure(figsize = (5,5))
plt.pie(store["Category"].value_counts(), labels = store["Category"].value_counts().index, autopct = "%.2f%%", 
        explode = [0.1,0,0])
plt.show()

##### END OF UNIVARIENT ANALSYSIS,
 #KEY NOTE POINTS: MAJOR products fall under Consumer segment, 
 # most delivered address fall under USA
 # Furniture, Tech  & Office supplies lead the charts under catogory section


# by far we have only drawn insights from important column dataset, now we see relation with each other
##############################################################################################################################


 # BI-VARIANTE ANALYSIS 



#Boxplot_ Category vs sales
sns.boxplot( x="Category",y="Sales",data=store)
plt.show()

#Category vs Profit
sns.boxplot( x="Category",y="Profit",data=store)
plt.show()


#Category wise profit of the product

plt.figure(figsize = (5,5))
plt.title("Category wise profit of the product")
plt.pie(store["Profit"].groupby(by = store["Category"]).sum(), 
        labels = store["Profit"].groupby(by = store["Category"]).sum().index, autopct = "%.2f%%", 
        explode = [0,0,0.1])
plt.show()



#Segment vs Sales

plt.figure(figsize = (7,5))
plt.title("Segment vs Sales")
sns.barplot(x = store["Segment"], y = store["Sales"])
plt.show()

#Segment wise profit of the product

plt.figure(figsize = (5,5))
plt.title("Segment wise profit of the product")
plt.pie(store["Profit"].groupby(by = store["Segment"]).sum(), 
        labels = store["Profit"].groupby(by = store["Segment"]).sum().index, autopct = "%.2f%%", 
        explode = [0.1,0,0])
plt.show()





#Region wise sales of the product

plt.figure(figsize = (5,5))
plt.title("Region wise sales of the product")
plt.pie(store["Sales"].groupby(by = store["Region"]).sum(), 
        labels = store["Sales"].groupby(by = store["Region"]).sum().index, autopct = "%.2f%%", 
        explode = [0,0,0,0.1])
plt.show()


#Region wise profit of the product

plt.figure(figsize = (5,5))
plt.title("Region wise profit of the product")
plt.pie(store["Profit"].groupby(by = store["Region"]).sum(), 
        labels = store["Profit"].groupby(by = store["Region"]).sum().index, autopct = "%.2f%%", 
        explode = [0,0,0,0.1])
plt.show()




#Category vs Discount

plt.figure(figsize = (5,5))
plt.title("Category vs Discount")
sns.barplot(x = store["Category"], y = store["Discount"])

#Category wise discount of the product

plt.figure(figsize = (7,5))
plt.title("Category wise discount of the product")
plt.pie(store["Discount"].groupby(by = store["Category"]).sum(), 
        labels = store["Discount"].groupby(by = store["Category"]).sum().index, autopct = "%.2f%%", 
        explode = [0,0.1,0])

plt.show()




# statewise v/s Profits

top_states_Profits = store.groupby("State")["Profit"].sum().sort_values (by ="Profit", descending=True)

# State vs Sales

top_states_Sales = store.groupby("State")["Sales"].sum().reset_index().sort_values(by ="Sales", ascending = False)
                                                                                                       
top_states_Sales.head(10)

# likewise we could perfrom MULI-VARIENT ANALSYSIS FOR FURTHER INSIGHTS TO HELP CAPITALISE ON YOUR LOSSES BY REGION, CATOGORY, SEGMENT, DISCOUNT,
 # in the process aided us to work on areas we could cover losses.
 # Calfornia, NY , Washinton D.C. shares highest profits
 