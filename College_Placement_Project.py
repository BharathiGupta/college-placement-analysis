#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[19]:


data = pd.read_csv(r"C:\Users\Bharati Gupta\OneDrive\Desktop\CLG_P_DA\Placement_Data_Full_Class.csv")
data.head()


# In[20]:


data.info()


# In[22]:


data.isnull().sum()


# In[23]:


data = data.drop_duplicates()


# In[25]:


data.columns = ['SlNo','Gender','SSC_P','SSC_B','HSC_P','HSC_B','HSC_S','Degree_P','Degree_T','WorkEx','ETest_P','Specialisation','MBA_P','Status','Salary']


# In[27]:


placement_counts = data['Status'].value_counts()
print(placement_counts)


# In[28]:


# Pie chart of placement status
plt.figure(figsize=(6,6))
placement_counts.plot.pie(autopct='%1.1f%%', colors=['lightgreen','salmon'])
plt.title('Placement Status Distribution')
plt.ylabel('')
plt.show()


# In[29]:


# Count of placements by gender
gender_placement = data.groupby(['Gender','Status']).size().unstack()
print(gender_placement)


# In[30]:


# Bar chart: Gender vs Placement
gender_placement.plot(kind='bar', figsize=(7,5), color=['salmon','lightgreen'])
plt.title('Placement Status by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()


# In[31]:


# Average percentages by placement status
avg_marks = data[['SSC_P','HSC_P','Degree_P','MBA_P','Status']].groupby('Status').mean()
print(avg_marks)


# In[32]:


# Bar chart for average marks by placement
avg_marks.plot(kind='bar', figsize=(8,6), color=['skyblue','orange'])
plt.title('Average Marks by Placement Status')
plt.ylabel('Percentage')
plt.show()


# In[33]:


# Count of placements by work experience
workex_placement = data.groupby(['WorkEx','Status']).size().unstack()
print(workex_placement)


# In[34]:


# Bar chart: Work Experience vs Placement
workex_placement.plot(kind='bar', figsize=(6,5), color=['salmon','lightgreen'])
plt.title('Placement Status by Work Experience')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()


# In[35]:


# Count of placements by MBA Specialisation
spec_placement = data.groupby(['Specialisation','Status']).size().unstack()
print(spec_placement)


# In[36]:


# Bar chart: Specialisation vs Placement
spec_placement.plot(kind='bar', figsize=(6,5), color=['salmon','lightgreen'])
plt.title('Placement Status by MBA Specialisation')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()


# In[37]:


# Count of placements by 10th board
ssc_board_placement = data.groupby(['SSC_B','Status']).size().unstack()
print(ssc_board_placement)


# In[39]:


# Bar chart: SSC Board vs Placement
ssc_board_placement.plot(kind='bar', figsize=(6,5), color=['salmon','lightgreen'])
plt.title('Placement Status by 10th Board')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()


# In[40]:


hsc_board_placement = data.groupby(['HSC_B','Status']).size().unstack()
print(hsc_board_placement)


# In[41]:


hsc_board_placement.plot(kind='bar', figsize=(6,5), color=['salmon','lightgreen'])
plt.title('Placement Status by 12th Board')
plt.ylabel('Number of Students')
plt.xticks(rotation=0)
plt.show()


# In[43]:


# Filter only placed students
placed_students = data[data['Status'] == 'Placed']

# Basic salary stats
salary_stats = placed_students['Salary'].describe()
print(salary_stats)


# In[46]:


# Histogram of salary
plt.figure(figsize=(7,5))
plt.hist(placed_students['Salary'], bins=10, color='cyan', edgecolor='black')
plt.title('Salary Distribution of Placed Students')
plt.xlabel('Salary')
plt.ylabel('Number of Students')
plt.show()


# In[50]:


# 1) Column names clean (remove extra spaces)
data.columns = data.columns.str.strip()

# 2) Print columns to confirm exact names
print(list(data.columns))


# In[52]:


print(data.columns)


# In[53]:


cols = ['SSC_P','HSC_P','Degree_P','ETest_P','MBA_P','Salary']

for c in cols:
    data[c] = pd.to_numeric(data[c], errors='coerce')

print(data[cols].isnull().sum())


# In[54]:


numeric_data = data[cols].dropna()   # drop rows where any of these are missing
correlation_matrix = numeric_data.corr()
correlation_matrix


# In[55]:


print(data.columns)


# In[56]:


import seaborn as sns

plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Between Academic Scores and Salary')
plt.show()


# In[ ]:




