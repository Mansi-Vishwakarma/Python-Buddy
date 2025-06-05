
import calendar
import tkinter as tk

def show_calendar(year):
    cal_text = calendar.TextCalendar(calendar.SUNDAY).formatyear(year, 2, 1, 1, 1)
    
    root = tk.Tk()
    root.title(f'Calendar for Year {year}')
    
    text = tk.Text(root, height=50, width=100)
    text.pack()
    text.insert(tk.END, cal_text)
    
    root.mainloop()

if _name_ == '_main_':
    year = 2023  # Change this to the desired year
    show_calendar(year)# import calendar
# import tkinter as tk
# from tkinter import ttk
# def show_calendar():
#     month = int(month_var.get())
#     year = int(year_var.get())
#     cal_content.delete(1.0, tk.END)
#     cal_text = calendar.month(year, month)
#     cal_content.insert(tk.END, cal_text)

# root = tk.Tk()
# root.title("Graphical Calendar")

# # Frame for selecting month and year
# frame = ttk.Frame(root)
# frame.pack(padx=10, pady=10)

# # Month selection
# month_label = ttk.Label(frame, text="Month:")
# month_label.grid(row=0, column=0)
# month_var = tk.StringVar()
# month_dropdown = ttk.Combobox(frame, textvariable=month_var, values=list(range(1, 13)))
# month_dropdown.grid(row=0, column=1)

# # Year selection
# year_label = ttk.Label(frame, text="Year:")
# year_label.grid(row=0, column=2)
# year_var = tk.StringVar()
# year_entry = ttk.Entry(frame, textvariable=year_var, width=6)
# year_entry.grid(row=0, column=3)

# # Show calendar button
# show_button = ttk.Button(frame, text="Show Calendar", command=show_calendar)
# show_button.grid(row=0, column=4)

# # Text widget to display the calendar
# cal_content = tk.Text(root, wrap=tk.WORD, width=25, height=10)
# cal_content.pack(padx=10, pady=10)

# root.mainloop()
