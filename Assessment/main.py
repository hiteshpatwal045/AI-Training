import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


students_data = {
    'StudentID': [201, 202, 203, 204, 205, 206, 207, 208],
    'Name': ['Aarav', 'Diya', 'Kabir', 'Riya','Ishaan', 'Ananya', 'Vivaan', 'Myra'],
    'CourseID': ['C01', 'C02', 'C01', 'C03','C02', 'C01', 'C03', 'C02'],
    'Marks': [85, 72, 91, np.nan, 66, 88, 54, np.nan],
    'Attendance': [92, 80, 95, 75, 70, 90, 65, 85]
}

students_df = pd.DataFrame(students_data)

print(students_df)


courses_data = {
    'CourseID': ['C01', 'C02', 'C03'],
    'CourseName': ['Python', 'Data Analytics', 'Machine Learning'],
    'Faculty': ['Sharma', 'Verma', 'Gupta']
}

courses_df = pd.DataFrame(courses_data)

print(courses_df)


print("\n========== FIRST FIVE STUDENT RECORDS ==========")
print(students_df.head())



print("\n========== DATAFRAME SHAPE ==========")
print(students_df.shape)

print("\n========== COLUMN NAMES ==========")
print(students_df.columns)


print(students_df.dtypes)


print("\n========== DESCRIPTIVE STATISTICS ==========")
print(students_df[['Marks', 'Attendance']].describe())


print("\n========== MISSING MARKS ==========")
print(students_df['Marks'].isna())



print("\n========== MISSING VALUES IN EVERY COLUMN ==========")
print(students_df.isna().sum())


print("\n========== COURSE-WISE AVERAGE MARKS ==========")
course_avg = students_df.groupby('CourseID')['Marks'].mean()
print(course_avg)


print("\n========== REPLACING MISSING MARKS ==========")
students_df['Marks'] = students_df['Marks'].fillna(
    students_df['CourseID'].map(course_avg)
)
print(students_df)

print("\n========== STUDENTS SCORING MORE THAN 75 ==========")
high_scorers = students_df[students_df['Marks'] > 75]
print(high_scorers)

print("\n========== STUDENTS WITH ATTENDANCE BELOW 75% ==========")
low_attendance = students_df[students_df['Attendance'] < 75]
print(low_attendance)


print("\n========== STUDENTS SORTED BY MARKS ==========")
sorted_students = students_df.sort_values(
    by='Marks',
    ascending=False
)
print(sorted_students)


print("\n========== ADDING RESULT COLUMN ==========")
students_df['Result'] = np.where(
    students_df['Marks'] >= 40,
    'Pass',
    'Fail'
)
print(students_df)

print("\n========== MERGED STUDENT AND COURSE DATA ==========")
merged_df = pd.merge(
    students_df,
    courses_df,
    on='CourseID',
    how='inner'
)
print(merged_df)

print("\n========== COURSE-WISE AVERAGE MARKS ==========")
course_wise_avg = students_df.groupby('CourseID')['Marks'].mean()
print(course_wise_avg)



print("\n========== COURSE-WISE MIN, MAX AND AVG MARKS ==========")
course_statistics = students_df.groupby('CourseID')['Marks'].agg(
    ['min', 'max', 'mean']
)
print(course_statistics)

print("\n========== STUDENTS ENROLLED IN EACH COURSE ==========")
course_count = students_df.groupby('CourseID')['StudentID'].count()
print(course_count)

print("\n========== BAR CHART: COURSE-WISE AVERAGE MARKS ==========")
plt.figure(figsize=(8, 5))
course_wise_avg.plot(
    kind='bar',
    title='Course-wise Average Marks',
    xlabel='Course ID',
    ylabel='Average Marks'
)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


print("\n========== PIE CHART: STUDENT DISTRIBUTION ==========")
course_count = students_df['CourseID'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    course_count,
    labels=course_count.index,
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Student Distribution Across Courses')
plt.show()


print("\n========== LINE CHART: ATTENDANCE VS MARKS ==========")

attendance_sorted = students_df.sort_values(
    by='Attendance',
    ascending=True
)

plt.figure(figsize=(10, 5))

plt.plot(
    attendance_sorted['Name'],
    attendance_sorted['Attendance'],
    marker='o',
    label='Attendance'
)

plt.plot(
    attendance_sorted['Name'],
    attendance_sorted['Marks'],
    marker='o',
    label='Marks'
)

plt.xlabel('Students')
plt.ylabel('Marks / Attendance')
plt.title('Student Attendance vs Marks')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


print("\n========== HISTOGRAM: MARKS DISTRIBUTION ==========")
plt.figure(figsize=(8, 5))
plt.hist(
    students_df['Marks'],
    bins=5,
    edgecolor='black'
)

plt.xlabel('Marks')
plt.ylabel('Number of Students')
plt.title('Distribution of Student Marks')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


print("\n========== FINAL CLEANED STUDENT DATAFRAME ==========")

print(students_df)

print("\n========== FINAL COURSE PERFORMANCE REPORT ==========")
print(merged_df)


