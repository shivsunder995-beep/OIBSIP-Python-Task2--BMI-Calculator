import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

from database import create_table, save_record, get_records

create_table()

window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x400")

# Labels

tk.Label(window, text="Name").pack()

name_entry = tk.Entry(window)
name_entry.pack()

tk.Label(window, text="Weight (kg)").pack()

weight_entry = tk.Entry(window)
weight_entry.pack()

tk.Label(window, text="Height (m)").pack()

height_entry = tk.Entry(window)
height_entry.pack()

result = tk.Label(window, text="", font=("Arial",14))
result.pack(pady=20)


def calculate():

    try:

        name = name_entry.get()

        weight = float(weight_entry.get())

        height = float(height_entry.get())

        if weight<=0 or height<=0:
            messagebox.showerror("Error","Enter positive values")
            return

        bmi = weight/(height**2)

        if bmi<18.5:
            category="Underweight"
            color="blue"

        elif bmi<25:
            category="Normal"
            color="green"

        elif bmi<30:
            category="Overweight"
            color="orange"

        else:
            category="Obese"
            color="red"

        result.config(
            text=f"BMI = {bmi:.2f}\n{category}",
            fg=color
        )

        save_record(name,weight,height,bmi,category)

    except ValueError:
        messagebox.showerror("Error","Please enter valid numbers")

    except Exception as e:
        messagebox.showerror("Database Error",str(e))


def show_graph():

    name=name_entry.get()

    data=get_records(name)

    if len(data)==0:
        messagebox.showinfo("Info","No records found")
        return

    bmi=[]

    dates=[]

    for record in data:
        bmi.append(record[0])
        dates.append(record[1])

    plt.figure(figsize=(6,4))
    plt.plot(dates,bmi,marker='o')
    plt.title(name+"'s BMI Trend")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


tk.Button(window,text="Calculate BMI",command=calculate).pack()

tk.Button(window,text="Show BMI Trend",command=show_graph).pack(pady=10)

window.mainloop()