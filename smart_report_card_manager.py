import tkinter as tk
from tkinter import messagebox
import csv

SUBJECTS = [
    ("Maths", "maths"), 
    ("Science", "science"), 
    ("SST", "sst"), 
    ("Computer", "computer"), 
    ("English", "english")
]

def save_data():
    student_data = {
        'name': entry_name.get(),
        'rollno': entry_roll.get(),
        'class': entry_class.get(),
    }
    
    try:
        student_data.update({
            'maths_h': entry_maths_h.get(),
            'maths_a': entry_maths_a.get(),
            'science_h': entry_science_h.get(),
            'science_a': entry_science_a.get(),
            'sst_h': entry_sst_h.get(),
            'sst_a': entry_sst_a.get(),
            'computer_h': entry_computer_h.get(),
            'computer_a': entry_computer_a.get(),
            'english_h': entry_english_h.get(),
            'english_a': entry_english_a.get()
        })
    except NameError as e:
        messagebox.showerror("Internal Error", f"Missing field definition: {e}. Please restart the application.")
        return

    if not (student_data['name'] and student_data['rollno'] and student_data['class']):
        messagebox.showwarning("Input Error", "Please fill in student name, roll number, and class.")
        return

    file_exists = False
    try:
        with open('report_card.csv', 'r', newline='') as f:
            if f.read(1):
                file_exists = True
    except FileNotFoundError:
        file_exists = False

    try:
        with open('report_card.csv', 'a', newline='') as csvfile:
            fieldnames = list(student_data.keys())
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(student_data)
        
        messagebox.showinfo("Success", "Student data saved successfully to report_card.csv!")
    except Exception as e:
        messagebox.showerror("File Error", f"Could not save data: {e}")

root = tk.Tk()
root.title("School Report Card Manager")
root.geometry("700x550")
# root.maxsize(888,999)
# root.minsize(222,444)
root.config(bg="lightblue")   
# root.resizable(True,True)

center_frame = tk.Frame(root, bg="lightblue")
center_frame.pack(expand=True)


title_label = tk.Label(center_frame, text="School Report Card Manager", 
                       font=("Arial", 20, "bold"), 
                       bg="deepskyblue",  
                       fg="white",
                       relief="raised",
                       bd=3,
                       padx=20,
                       pady=10)
title_label.pack(pady=(0, 20), fill='x')


form_frame = tk.Frame(center_frame, bg="white", padx=30, pady=30, relief="groove", bd=5)
form_frame.pack(padx=20, pady=10)


student_frame = tk.LabelFrame(form_frame, text="Student Details", bg="white", fg="navy", font=("Arial", 12, "bold"), padx=10, pady=10)
student_frame.pack(fill='x', pady=10)

tk.Label(student_frame, text="Student Name:", bg="white", font=("Arial", 10)).grid(row=0, column=0, sticky='w', padx=5, pady=5)
entry_name = tk.Entry(student_frame, width=25, relief="solid", bd=1)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(student_frame, text="Roll No:", bg="white", font=("Arial", 10)).grid(row=1, column=0, sticky='w', padx=5, pady=5)
entry_roll = tk.Entry(student_frame, width=25, relief="solid", bd=1)
entry_roll.grid(row=1, column=1, padx=5, pady=5)

tk.Label(student_frame, text="Class:", bg="white", font=("Arial", 10)).grid(row=2, column=0, sticky='w', padx=5, pady=5)
entry_class = tk.Entry(student_frame, width=25, relief="solid", bd=1)
entry_class.grid(row=2, column=1, padx=5, pady=5)

# Marks Section
marks_frame = tk.LabelFrame(form_frame, text="Subject (Marks) (Half-Yearly / Annual)", bg="white", fg="navy", font=("Arial", 12, "bold"), padx=10, pady=10)
marks_frame.pack(fill='x', pady=15)

tk.Label(marks_frame, text="Subject", bg="white", font=("Arial", 10, "underline")).grid(row=0, column=0, sticky='w', padx=5, pady=2)
tk.Label(marks_frame, text="Half-Yearly", bg="white", font=("Arial", 10, "underline")).grid(row=0, column=1, padx=5, pady=2)
tk.Label(marks_frame, text="Annual", bg="white", font=("Arial", 10, "underline")).grid(row=0, column=2, padx=5, pady=2)

entries = {}
for i, (subject_display, subject_key) in enumerate(SUBJECTS):
    row_index = i + 1
    tk.Label(marks_frame, text=f"{subject_display}", bg="white", font=("Arial", 10)).grid(row=row_index, column=0, sticky='w', padx=5, pady=3)
    h_key = f'{subject_key}_h'
    entries[h_key] = tk.Entry(marks_frame, width=8, relief="solid", bd=1, bg="aliceblue")
    entries[h_key].grid(row=row_index, column=1, padx=10, pady=3)
    a_key = f'{subject_key}_a'
    entries[a_key] = tk.Entry(marks_frame, width=8, relief="solid", bd=1, bg="aliceblue")
    entries[a_key].grid(row=row_index, column=2, padx=10, pady=3)

# Assign global variables
entry_maths_h = entries['maths_h']
entry_maths_a = entries['maths_a']
entry_science_h = entries['science_h'] 
entry_science_a = entries['science_a']
entry_sst_h = entries['sst_h']
entry_sst_a = entries['sst_a']
entry_computer_h = entries['computer_h'] 
entry_computer_a = entries['computer_a']
entry_english_h = entries['english_h']
entry_english_a = entries['english_a']

# Save Button
save_btn = tk.Button(form_frame, text="Save Data", command=save_data, 
                     bg="navy", fg="white", font=("Arial", 12, "bold"), 
                     relief="raised", padx=15, pady=8, bd=3)
save_btn.pack(pady=(20, 0), anchor='e')

root.mainloop()