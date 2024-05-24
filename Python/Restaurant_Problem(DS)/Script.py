# importing pandas
import pandas as pd

# loading in data
data_week1 = pd.read_csv("Data_Week1.csv")
data_week2 = pd.read_csv("Data_Week2.csv")
#data_week3 = pd.read_csv("Data_Week3.csv")
#data_week4 = pd.read_csv("Data_Week4.csv")
days_of_week = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

# Start of week 1
week1_meat_each_day = []
week1_total_meat = 0
week1_fish_each_day = []
week1_total_fish = 0
week1_chicken_each_day = []
week1_total_chicken = 0

for column_index1 in range(0, 3):
    if column_index1 == 0:
        for data in data_week1.Meat:
            week1_meat_each_day.append(int(data))
            week1_total_meat += int(data)
    elif column_index1 == 1:
        for data in data_week1.Fish:
            week1_fish_each_day.append(int(data))
            week1_total_fish += int(data)
    elif column_index1 == 2:
        for data in data_week1.Chicken:
            week1_chicken_each_day.append(int(data))
            week1_total_chicken += int(data)

# Start of week 2
week2_meat_each_day = []
week2_total_meat = 0
week2_fish_each_day = []
week2_total_fish = 0
week2_chicken_each_day = []
week2_total_chicken = 0

for column_index2 in range(0, 3):
    if column_index2 == 0:
        for data in data_week2.Meat:
            week2_meat_each_day.append(int(data))
            week2_total_meat += int(data)
    elif column_index2 == 1:
        for data in data_week2.Fish:
            week2_fish_each_day.append(int(data))
            week2_total_fish += int(data)
    elif column_index2 == 2:
        for data in data_week2.Chicken:
            week2_chicken_each_day.append(int(data))
            week2_total_chicken += int(data)

print(week1_total_meat, week1_total_fish, week1_total_chicken)
print(week2_total_meat, week2_total_fish, week2_total_chicken)