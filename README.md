# 📋 Attendance Management System

A **Command-Line Interface (CLI) based Attendance Management System** built with **Python**. The project provides a simple and efficient way to manage student records, mark attendance, view attendance history, and calculate attendance percentages directly from the terminal.

## 🚀 Features

* 👨‍🎓 Add and manage student records
* ✅ Mark students as Present or Absent
* 📅 Record attendance date-wise
* 📊 Calculate attendance percentage
* 🔎 View individual student attendance
* 📋 Display complete attendance records
* 💾 Store attendance data using CSV files
* 🔄 Update and manage existing records
* 🖥️ Simple and interactive command-line interface

## 🛠️ Technologies Used

* **Python 3**
* **CSV Module**
* **OS Module**
* **Datetime Module**

## 📂 Project Structure

```text
Attendance-Management-System/
│
├── attendance.py
├── students.csv
├── attendance.csv
└── README.md
```

> File names may vary depending on your implementation.

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/attendance-management-system.git
```

### 2. Navigate to the Project

```bash
cd attendance-management-system
```

### 3. Run the Program

```bash
python attendance.py
```

If your system uses `python3`:

```bash
python3 attendance.py
```

## 💻 How It Works

When the program starts, it provides a menu-driven CLI through which the user can perform different operations.

```text
========================================
     ATTENDANCE MANAGEMENT SYSTEM
========================================

1. Add Student
2. View Students
3. Mark Attendance
4. View Attendance
5. Calculate Attendance
6. Exit

Enter your choice:
```

The user can select an option and follow the instructions displayed in the terminal.

## 📊 Attendance Calculation

The attendance percentage is calculated using:

```text
Attendance % = (Days Present / Total Working Days) × 100
```

For example:

```text
Days Present = 18
Total Days   = 20

Attendance = (18 / 20) × 100
           = 90%
```

## 🎯 Project Objectives

The main objectives of this project are:

* To digitize the traditional attendance-recording process.
* To reduce manual record-keeping.
* To make attendance tracking simple and efficient.
* To practice Python file handling and data management.
* To implement a real-world problem using a CLI application.

## 📚 Concepts Practiced

This project demonstrates practical usage of:

* Variables and data types
* Conditional statements
* Loops
* Functions
* Lists and dictionaries
* File handling
* CSV file operations
* Date and time handling
* Exception handling
* Menu-driven programming
* Basic data management

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] GUI-based version
* [ ] Database integration using SQLite/MySQL
* [ ] Student login system
* [ ] Teacher/admin authentication
* [ ] Monthly and semester-wise reports
* [ ] Attendance report export
* [ ] Low-attendance alerts
* [ ] Web-based version
* [ ] Dashboard with attendance statistics

## 👨‍💻 Author

**Yatharth Kaushik**

Developed as a Python project to practice programming fundamentals and build a practical real-world application.

---

⭐ If you find this project useful, consider giving the repository a **star**!
