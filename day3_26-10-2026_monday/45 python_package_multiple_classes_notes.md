# Python: Create a Package with Multiple Classes

> **Goal:** Learn how to organize Python code into a package containing
> multiple modules and classes, then import and use those classes from
> another file.

## 1. What is a package in Python?

A **module** is a Python file (`.py`) that contains code such as
functions, variables, or classes.

A **package** is a directory used to organize related Python modules. A
package commonly contains an `__init__.py` file, which can be empty. In
modern Python, namespace packages can work without it, but including it
is a clear, beginner-friendly convention.

A **class** is a blueprint for creating objects. For example, `Student`
can describe student objects, while `Teacher` can describe teacher
objects.

### How the parts fit together

-   **Package:** `school`
-   **Modules:** `student.py`, `teacher.py`, `classroom.py`
-   **Classes:** `Student`, `Teacher`, `Classroom`
-   **Main program:** `main.py`, which imports and uses the classes

## 2. Why use a package with multiple classes?

Packages help you:

1.  **Organize code:** Keep related classes together.
2.  **Reuse code:** Import a class instead of rewriting it.
3.  **Maintain projects:** Update one module without making one giant
    file.
4.  **Collaborate:** Different developers can work on separate modules.
5.  **Avoid clutter:** Separate responsibilities into clear files.
6.  **Scale projects:** Add more modules as the project grows.

For example, a school-management application might keep student details
in `student.py`, teacher details in `teacher.py`, and classroom
information in `classroom.py`.

## 3. Example project structure

Create this structure:

``` text
python_package_demo/
├── main.py
└── school/
    ├── __init__.py
    ├── student.py
    ├── teacher.py
    └── classroom.py
```

What each file does:

  -----------------------------------------------------------------------
  File                                Responsibility
  ----------------------------------- -----------------------------------
  `main.py`                           Starts the example and uses the
                                      classes

  `school/__init__.py`                Marks/initializes the package; it
                                      can be empty

  `school/student.py`                 Defines the `Student` class

  `school/teacher.py`                 Defines the `Teacher` class

  `school/classroom.py`               Defines the `Classroom` class
  -----------------------------------------------------------------------

## 4. Create the classes

### `school/student.py`

``` python
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

    def display_details(self):
        print("Student name:", self.name)
        print("Roll number:", self.roll_number)
```

Explanation:

-   `class Student:` defines a class named `Student`.
-   `__init__` runs when a `Student` object is created.
-   `self.name` and `self.roll_number` store data on that object.
-   `display_details()` is an instance method that displays the
    student's details.

### `school/teacher.py`

``` python
class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_details(self):
        print("Teacher name:", self.name)
        print("Subject:", self.subject)
```

This module defines a separate `Teacher` class. Keeping it in its own
file makes the project easier to understand and maintain.

### `school/classroom.py`

``` python
class Classroom:
    def __init__(self, room_number):
        self.room_number = room_number
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print("Classroom:", self.room_number)

        for student in self.students:
            print(student.name)
```

This class stores a list of student objects. The `add_student()` method
receives a `Student` object and adds it to the list. This illustrates
how classes defined in different modules can work together.

## 5. Make the package importable

For this beginner example, leave `school/__init__.py` empty:

``` python
# This file can be empty.
```

You can also expose selected classes from the package in `__init__.py`,
but that is optional. Beginners can first learn explicit imports from
the individual modules.

## 6. Use the classes from `main.py`

``` python
from school.student import Student
from school.teacher import Teacher
from school.classroom import Classroom

student1 = Student("Ravi", 101)
teacher1 = Teacher("Anita", "Python")
classroom1 = Classroom("A-101")

classroom1.add_student(student1)

print("STUDENT DETAILS")
student1.display_details()

print("\nTEACHER DETAILS")
teacher1.display_details()

print("\nCLASSROOM DETAILS")
classroom1.display_students()
```

### Expected output

``` text
STUDENT DETAILS
Student name: Ravi
Roll number: 101

TEACHER DETAILS
Teacher name: Anita
Subject: Python

CLASSROOM DETAILS
Classroom: A-101
Ravi
```

## 7. Understand the import statements

``` python
from school.student import Student
```

Read this from right to left:

-   `school` is the package.
-   `student` is the module (`student.py`) inside the package.
-   `Student` is the class defined in that module.

Likewise:

``` python
from school.teacher import Teacher
from school.classroom import Classroom
```

These import the other classes. After importing them, `main.py` can
create objects and call their methods.

## 8. How to run the project

1.  Open a terminal in the `python_package_demo` directory---the
    directory containing `main.py`.
2.  Run:

``` bash
python main.py
```

If your system uses `python3` to launch Python, run:

``` bash
python3 main.py
```

Run the program from the project root so Python can find the `school`
package.

## 9. Important concepts

### Module vs package vs class vs object

  Term      Meaning                          Example
  --------- -------------------------------- --------------
  Module    A Python file                    `student.py`
  Package   A directory organizing modules   `school/`
  Class     A blueprint for objects          `Student`
  Object    An instance of a class           `student1`

### `__init__.py`

-   It can be an empty file.
-   It is commonly used to identify and initialize a regular Python
    package.
-   It can contain package initialization code or selected imports.
-   Some namespace packages work without it, so it is not mandatory in
    every possible package design.

### `self`

`self` refers to the current instance of a class. It lets an instance
method access that object's attributes and other methods. It is the
conventional name used in Python.

### Composition: a class using another class

In this example, `Classroom` stores `Student` objects. This is a simple
example of **composition/has-a relationship**: a classroom has students.
Passing a `Student` object to `add_student()` is different from passing
only a student's name.

## 10. Common mistakes and how to avoid them

1.  **Wrong folder name in an import:** Check that the package folder is
    named `school` if you import from `school`.
2.  **Wrong module or class spelling:** `student.py` and `Student` are
    different names with different roles; match the spelling exactly.
3.  **Running from the wrong directory:** Run `main.py` from the project
    root for this layout.
4.  **Forgetting to create the file:** Ensure every imported `.py` file
    exists in the expected folder.
5.  **Naming your file after a standard-library module:** Avoid names
    such as `random.py`, `json.py`, or `email.py` for unrelated project
    files because they can interfere with imports.
6.  **Putting everything into one file:** That works for small examples,
    but separating related classes into modules is the point of this
    exercise.
7.  **Confusing a class with an object:** `Student` is the class;
    `student1 = Student(...)` creates an object.

## 11. How this applies to a real project

For a library-management project, a package might look like:

``` text
library/
├── __init__.py
├── book.py
├── member.py
└── librarian.py
```

-   `Book` could store a title, author, and book ID.
-   `Member` could store member details.
-   `Librarian` could manage issuing and returning books.

For a larger project, organize modules by responsibility and import only
what is needed. Avoid creating a separate file for every tiny class
unless it improves clarity.

## 12. Quick revision

-   A package organizes related Python modules.
-   A module is a `.py` file.
-   A class defines the attributes and behavior of objects.
-   Multiple classes can be kept in different modules within the same
    package.
-   Import a class using `from package.module import ClassName`.
-   `__init__.py` can be empty and is a useful convention for a regular
    package.
-   Run the main program from the project root in this example.

## 13. Interview-ready answer

**Question: How do you create a package with multiple classes in
Python?**

A Python package is a directory used to organize related modules. I
create a package directory, commonly add an `__init__.py` file, and
place related classes in separate Python modules. For example, a
`school` package can contain `student.py` with a `Student` class,
`teacher.py` with a `Teacher` class, and `classroom.py` with a
`Classroom` class. A main program can import these classes using
statements such as `from school.student import Student`. This structure
improves organization, reuse, readability, and maintainability.

## 14. Practice tasks

Try these yourself after running the example:

1.  Add an `email` attribute to `Student` and display it.
2.  Add a `department` attribute to `Teacher`.
3.  Add a method to `Classroom` that returns the number of students.
4.  Create a second `Student` object and add both students to the
    classroom.
5.  Create another module named `subject.py` with a `Subject` class,
    then import it in `main.py`.

## References

-   Python tutorial --- Modules:
    https://docs.python.org/3/tutorial/modules.html
-   Python tutorial --- Classes:
    https://docs.python.org/3/tutorial/classes.html
-   Python language reference --- Import system:
    https://docs.python.org/3/reference/import.html
