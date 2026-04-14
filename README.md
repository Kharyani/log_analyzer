# 🐍 System Log Analyzer & Report Generator

## 📌 Project Overview

This project is a Command Line Interface (CLI) based Python application designed to analyze system/application log files and generate meaningful reports. It simulates real-world debugging and monitoring tools used in software companies.

---

## 🎯 Features

* 📂 Load log files (.txt / .log)
* 🔍 Analyze logs (ERROR, WARNING, INFO)
* 📊 Count occurrences of log levels
* 🔎 Search logs (case-insensitive)
* 📁 Filter logs by:

  * Log level (ERROR / WARNING / INFO)
  * Date
* 📄 Generate reports:

  * TXT format
  * CSV format
* 📈 Visual chart using matplotlib (bonus feature)
* ⚠️ Error handling (file not found, empty file)
* 🧩 Modular code structure

---

## 🛠 Technologies Used

* Python 3
* Regular Expressions (re)
* CSV module
* Matplotlib (for visualization)

---

## 📂 Project Structure

log_analyzer/
│── main.py
│── sample.log
│── report.txt
│── report.csv
│── README.md

---

## ▶️ How to Run the Project

### Step 1: Download Project

Download or clone this repository to your system.

### Step 2: Install Required Library

```bash
pip install matplotlib
```

### Step 3: Run the Program

```bash
python main.py
```

---

## 📊 Sample Log Format

2026-04-14 10:00:00 INFO Application started
2026-04-14 10:05:23 WARNING Disk space low
2026-04-14 10:10:45 ERROR Failed to connect to database

---

## 📈 Output

### ✔ Console Output

* Displays summary of logs (ERROR, WARNING, INFO)

### ✔ Generated Files

* report.txt → Summary report
* report.csv → Detailed log data

### ✔ Chart

* Bar chart showing distribution of log levels

---

## 💡 Advanced Features Implemented

* Regex-based log parsing
* Case-insensitive search
* Efficient file handling
* Modular functions
* Exception handling

---

## 🌟 Future Improvements

* GUI version using Tkinter
* PDF report generation
* Real-time log monitoring
* Web-based dashboard

---

## 👨‍💻 Author

Kashish Haryani
Computer Science Student

---

## 🎥 Demo

A short demo video (1–2 minutes) demonstrating:

* File loading
* Log analysis
* Search and filtering
* Report generation

---

## 📌 Conclusion

This project demonstrates practical implementation of file handling, pattern matching, and data analysis in Python. It reflects real-world applications of log monitoring systems used in software development and DevOps.

⭐ If you like this project, consider giving it a star!
