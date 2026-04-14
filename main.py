import re
import csv
from datetime import datetime
import matplotlib.pyplot as plt

log_data = []
file_loaded = False

# Regex pattern
log_pattern = re.compile(
    r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})? ?(?P<level>ERROR|WARNING|INFO)? ?(?P<message>.*)',
    re.IGNORECASE
)

# Load file
def load_file():
    global log_data, file_loaded
    filename = input("Enter log file name: ")

    try:
        with open(filename, 'r') as file:
            log_data = file.readlines()
            if not log_data:
                print("⚠️ File is empty.")
                return
            file_loaded = True
            print("✅ File loaded successfully.")
    except FileNotFoundError:
        print("❌ File not found.")


# Analyze logs
def analyze_logs():
    if not file_loaded:
        print("⚠️ Load file first.")
        return None

    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    parsed_logs = []

    for line in log_data:
        match = log_pattern.match(line.strip())
        if match:
            level = match.group("level")
            timestamp = match.group("timestamp")
            message = match.group("message")

            if level:
                level = level.upper()
                if level in counts:
                    counts[level] += 1

            parsed_logs.append({
                "timestamp": timestamp,
                "level": level,
                "message": message
            })

    print("\n📊 Log Summary:")
    print(counts)

    return counts, parsed_logs


# Search logs
def search_logs():
    if not file_loaded:
        print("⚠️ Load file first.")
        return

    keyword = input("Enter keyword to search: ").lower()

    results = [line for line in log_data if keyword in line.lower()]

    print(f"\n🔍 Found {len(results)} results:")
    for r in results:
        print(r.strip())


# Filter logs
def filter_logs():
    if not file_loaded:
        print("⚠️ Load file first.")
        return

    level = input("Enter level (ERROR/WARNING/INFO or leave blank): ").upper()
    date = input("Enter date (YYYY-MM-DD or leave blank): ")

    filtered = []

    for line in log_data:
        if level and level not in line.upper():
            continue
        if date and date not in line:
            continue
        filtered.append(line)

    print(f"\n📂 Filtered Results ({len(filtered)}):")
    for f in filtered:
        print(f.strip())


# Generate report
def generate_report():
    result = analyze_logs()
    if not result:
        return

    counts, parsed_logs = result

    total_logs = len(log_data)

    # Save TXT report
    with open("report.txt", "w") as f:
        f.write("Log Analysis Report\n")
        f.write(f"Total Logs: {total_logs}\n")
        f.write(f"Errors: {counts['ERROR']}\n")
        f.write(f"Warnings: {counts['WARNING']}\n")
        f.write(f"Info: {counts['INFO']}\n")

    # Save CSV report
    with open("report.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Timestamp", "Level", "Message"])

        for log in parsed_logs:
            writer.writerow([log["timestamp"], log["level"], log["message"]])

    print("✅ Report generated (report.txt & report.csv)")

    # Bonus: Chart
    plot_chart(counts)


# Chart visualization
def plot_chart(counts):
    levels = list(counts.keys())
    values = list(counts.values())

    plt.bar(levels, values)
    plt.title("Log Level Distribution")
    plt.xlabel("Log Level")
    plt.ylabel("Count")
    plt.show()


# Menu system
def menu():
    while True:
        print("\n===== LOG ANALYZER MENU =====")
        print("1. Load Log File")
        print("2. Analyze Logs")
        print("3. Search Logs")
        print("4. Filter Logs")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            load_file()
        elif choice == "2":
            analyze_logs()
        elif choice == "3":
            search_logs()
        elif choice == "4":
            filter_logs()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    menu()