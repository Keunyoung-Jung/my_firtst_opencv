import matplotlib.pyplot as plt
import csv

f = open('train.csv')
data = csv.reader(f)

header = next(data)

sex_sur_arr = []
sex_dea_arr = []

for row in data :
    if row[1] == '1':
            sex_sur_arr.append(row[4])
            print(sex_sur_arr)
        
    elif row[1] == '0' :
            sex_dea_arr.append(row[4])
        
male_sur = sex_sur_arr.count('male')
female_sur = sex_sur_arr.count('female')
male_dea = sex_dea_arr.count('male')
female_dea = sex_dea_arr.count('female')

plt.title('Sex - Survived')
plt.ylabel('Sex')
plt.pie([female_sur,male_sur],autopct='%1.1f%%',labels=['female','male'],shadow = True)

plt.figure()
plt.title('Sex - Dead')
plt.ylabel('Sex')
plt.pie([male_dea,female_dea],autopct='%1.1f%%',labels=['male','female'],shadow = True)
plt.show()