import tkinter as tk

#Transitions from welcome screen to calculator screen
def go_to_gpa_calc():
    gpa_frame.pack()
    welcome_frame.pack_forget()

#Calculates weighted and unweighted GPA    
def calculate_gpa():
    # Get inputs from entry fields
    semesters_completed = int(sem_num_field.get())
    total_classes = int(class_num_field.get())
    weighted_classes = int(weighted_num_field.get())
    grade_a = int(grade_a_num.get()) * 4
    grade_b = int(grade_b_num.get()) * 3
    grade_c = int(grade_c_num.get()) * 2
    grade_d = int(grade_d_num.get()) * 1
    grade_f = int(grade_f_num.get()) * 0
    
    # Calculate unweighted GPA
    total_grades = grade_a + grade_b + grade_c + grade_d + grade_f
    unweighted_gpa = total_grades / total_classes
    
    # Calculate weighted GPA
    weighted_gpa = (weighted_classes / (semesters_completed * 7)) + unweighted_gpa
    
    # Display the calculated GPAs
    unweighted_gpa_label.config(text=f"Unweighted GPA: {unweighted_gpa:.2f}")
    weighted_gpa_label.config(text=f"Weighted GPA: {weighted_gpa:.2f}")

#Ends program    
def close_out():
    root.destroy()
    
# Welcome screen window
root = tk.Tk()
root.title("Welcome to GPA Calculator")
root.geometry('750x750')
root.configure(bg="#E6D4FF")

# Welcome frame
welcome_frame = tk.Frame(root)
welcome_frame.configure(bg="#E6D4FF")

# Welcome message label
welcome_message = tk.Label(welcome_frame, text="Welcome to GPA Calculator", font=("Helvetica", 18), bg="#B47EFF")
welcome_message.pack(pady=(200, 10))

# Instruction label
instructions = tk.Label(welcome_frame, text="Answer questions about your classes and grades \n to find your weighted and unweighted GPA!", font=("Helvetica", 14), bg="#B47EFF")
instructions.pack(pady=(10, 10))

# Get Started button
get_started = tk.Button(welcome_frame, text="Get Started", command=go_to_gpa_calc, bg="#B47EFF", activebackground="#C79FFF", bd=0, font=("Helvetica", 14))
get_started.pack(pady=10)

# Close Out of Program button
close = tk.Button(welcome_frame, text="Close", command=close_out, bg="#B47EFF", activebackground="#C79FFF", bd=0, font=("Helvetica", 14))
close.pack(pady=7.5)

# GPA frame
gpa_frame = tk.Frame(root)
gpa_title = tk.Label(gpa_frame, text = "GPA Calculator", font=("Helvetica", 18), bg="#E6D4FF")
gpa_title.pack(pady = (5, 5))
gpa_frame.configure(bg="#E6D4FF")

gpa_subtitle = tk.Label(gpa_frame, text = "Fill in the text fields below.", font=("Helvetica", 14), bg="#E6D4FF")
gpa_subtitle.pack(pady = (5, 5))

# Text Fields
# Input field for number of semesters
sem_num_question = tk.Label(gpa_frame, text = "Type the number of semesters you completed", font=("Helvetiva", 12), bg="#E6D4FF")
sem_num_question.pack(pady=(2.5, 2.5))

sem_num_field = tk.Entry(gpa_frame, width = 50)
sem_num_field.focus_set()
sem_num_field.pack(pady=(2.5, 2.5))
sem_num_field.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of total classes
class_num_question = tk.Label(gpa_frame, text = "Type the total number of classes you completed", font=("Helvetiva", 12), bg="#E6D4FF")
class_num_question.pack(pady=(2.5, 2.5))

class_num_field = tk.Entry(gpa_frame, width = 50)
class_num_field.focus_set()
class_num_field.pack(pady=(2.5, 2.5))
class_num_field.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of weighted classes
weighted_class_question = tk.Label(gpa_frame, text = "Type the number of weighted classes you completed", font=("Helvetiva", 12), bg="#E6D4FF")
weighted_class_question.pack(pady=(2.5, 2.5))

weighted_num_field = tk.Entry(gpa_frame, width = 50)
weighted_num_field.focus_set()
weighted_num_field.pack(pady=(2.5, 2.5))
weighted_num_field.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of classes with a grade A
grade_a_question = tk.Label(gpa_frame, text = "Type the number of classes you received an A in", font=("Helvetiva", 12), bg="#E6D4FF")
grade_a_question.pack(pady=(2.5, 2.5))

grade_a_num = tk.Entry(gpa_frame, width = 50)
grade_a_num.focus_set()
grade_a_num.pack(pady=(2.5, 2.5))
grade_a_num.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of classes with a grade B
grade_b_question = tk.Label(gpa_frame, text = "Type the number of classes you received a B in", font=("Helvetiva", 12), bg="#E6D4FF")
grade_b_question.pack(pady=(2.5, 2.5))

grade_b_num = tk.Entry(gpa_frame, width = 50)
grade_b_num.focus_set()
grade_b_num.pack(pady=(2.5, 2.5))
grade_b_num.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of classes with a grade C
grade_c_question = tk.Label(gpa_frame, text = "Type the number of classes you received a C in", font=("Helvetiva", 12), bg="#E6D4FF")
grade_c_question.pack(pady=(2.5, 2.5))

grade_c_num = tk.Entry(gpa_frame, width = 50)
grade_c_num.focus_set()
grade_c_num.pack(pady=(2.5, 2.5))
grade_c_num.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of classes with a grade D
grade_d_question = tk.Label(gpa_frame, text = "Type the number of classes you received a D in", font=("Helvetiva", 12), bg="#E6D4FF")
grade_d_question.pack(pady=(2.5, 2.5))

grade_d_num = tk.Entry(gpa_frame, width = 50)
grade_d_num.focus_set()
grade_d_num.pack(pady=(2.5, 2.5))
grade_d_num.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Input field for number of classes with a grade F
grade_f_question = tk.Label(gpa_frame, text = "Type the number of classes you received a F in", font=("Helvetiva", 12), bg="#E6D4FF")
grade_f_question.pack(pady=(2.5, 2.5))

grade_f_num = tk.Entry(gpa_frame, width = 50)
grade_f_num.focus_set()
grade_f_num.pack(pady=(2.5, 2.5))
grade_f_num.configure(bd=0, highlightbackground = "#B47EFF", highlightcolor= "#B47EFF")

# Submit Button
submit = tk.Button(gpa_frame, text="Submit", command=calculate_gpa, bg="#B47EFF", activebackground="#C79FFF", bd=0, font=("Helvetica", 14))
submit.pack(pady=2.5)

# Close Out of Program Button
close = tk.Button(gpa_frame, text="Close", command=close_out, bg="#B47EFF", activebackground="#C79FFF", bd=0, font=("Helvetica", 14))
close.pack(pady=5)

# Labels for displaying calculated GPAs
unweighted_gpa_label = tk.Label(gpa_frame, text="", bg="#E6D4FF")
unweighted_gpa_label.pack(pady=(10, 5))

weighted_gpa_label = tk.Label(gpa_frame, text="", bg="#E6D4FF")
weighted_gpa_label.pack(pady=(5, 10))

# Runs the frames main loop
welcome_frame.pack()
root.mainloop()