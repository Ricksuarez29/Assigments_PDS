# Python Exercises for Session 3

## Table of Contents
- [Introduction](#introduction)
- [Exercise 1: Course Class](#exercise-1-course-class)
- [Exercise 2: Student Class](#exercise-2-student-class)
- [Exercise 3: Registration Class](#exercise-3-registration-class)
- [Exercise 4: Grades Management](#exercise-4-grades-management)

## Introduction
<div style="background-color: #f0f8ff; padding: 10px;">
This project implements a course and student management system in Python. The system allows adding and removing students and courses, as well as managing student enrollments in courses, dropping enrollments, and viewing enrolled students and courses.
</div>

## Exercise 1: Course Class
<div style="background-color: #ffe4e1; padding: 10px;">
The `Course` class represents a course with a name, a description, and a list of enrolled students.

### Methods
- **`add_student(student)`**: Adds a student to the course.
- **`remove_student(student)`**: Removes a student from the course.
- **`show_students()`**: Shows all students enrolled in the course.
</div>

## Exercise 2: Student Class
<div style="background-color: #e6e6fa; padding: 10px;">
The `Student` class represents a student with a name, an ID number, an address, and a list of enrolled courses.

### Methods
- **`enroll_in_course(course)`**: Enrolls the student in a course.
- **`drop_course(course)`**: Drops the student from a course.
- **`show_courses()`**: Shows all courses the student is enrolled in.
</div>

## Exercise 3: Registration Class
<div style="background-color: #f5f5dc; padding: 10px;">
The `Registration` class manages the list of students and courses. It provides methods for enrolling students in courses, dropping enrollments, and showing lists of students and courses.

### Methods
- **`add_student(student)`**: Adds a student to the list of students.
- **`add_course(course)`**: Adds a course to the list of courses.
- **`enroll_student_in_course(student, course)`**: Enrolls a student in a course.
- **`drop_student_from_course(student, course)`**: Drops a student from a course.
- **`show_all_enrolled_courses(student)`**: Shows all courses a student is enrolled in.
- **`show_all_students(course)`**: Shows all students enrolled in a course.
</div>

## Exercise 4: Grades Management
<div style="background-color: #fffacd; padding: 10px;">
Each student has a list of courses with grades. The `Student` class includes a method to calculate the GPA (Grade Point Average) of the student given their name or ID.

### Method
- **`calculate_gpa()`**: Calculates the student's GPA based on their grades in courses.
</div>

## Contributions
<div style="background-color: #d3ffd3; padding: 10px;">
Contributions are welcome. Please open an issue or a pull request to discuss any changes.
</div>

## License
<div style="background-color: #e0ffff; padding: 10px;">
This project is licensed under the MIT License. See the LICENSE file for more details.
</div>



