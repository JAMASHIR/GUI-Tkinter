import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter.ttk as ttk


def on_button_click():
    print("Button clicked!")


window = ctk.CTk()

ctk.set_appearance_mode("dark")

window.title("Care IUB")
window.geometry("800x600")
window.resizable(width=False, height=False)

top_frame = ctk.CTkFrame(window, width=800, height=50)
top_frame.pack()

bottom_frame = ctk.CTkFrame(window, width=800, height=500)
bottom_frame.place(x=0, y=100)

middle_frame = ctk.CTkFrame(window, width=800, height=75)
middle_frame.place(x=0, y=150)

label = ctk.CTkLabel(middle_frame, text="Object Lot No:", font=("Arial", 15))
label.place(x=30, y=1)

tb1 = ctk.CTkEntry(middle_frame)
tb1.place(x=25, y=20)

label = ctk.CTkLabel(middle_frame, text="Object Name:", font=("Arial", 15))
label.place(x=230, y=1)

label = ctk.CTkLabel(window, text="Test Log", font=("Arial", 20))
label.place(x=340, y=115)

label = ctk.CTkLabel(window, text="select options", font=("Arial", 20))
label.place(x=200, y=250)

label = ctk.CTkLabel(window, text="Actions", font=("Arial", 15))
label.place(x=585, y=235)

tb1 = ctk.CTkEntry(middle_frame)
tb1.place(x=230, y=20)

label = ctk.CTkLabel(middle_frame, text="Object Class:", font=("Arial", 15))
label.place(x=400, y=1)

tb1 = ctk.CTkEntry(middle_frame)
tb1.place(x=400, y=20)

label = ctk.CTkLabel(middle_frame, text="Object Client:", font=("Arial", 15))
label.place(x=600, y=1)

tb1 = ctk.CTkEntry(middle_frame)
tb1.place(x=600, y=20)

# top_left_frame = ctk.CTkFrame(top_frame, width=100, height=150)
# top_left_frame.place(x=0, y=0)

# top_right_frame = ctk.CTkFrame(top_frame, width=800, height=50)
# top_right_frame.place(x=0, y=0)

bottom_left_frame = ctk.CTkFrame(bottom_frame, width=490, height=490)
bottom_left_frame.place(x=100, y=200)

bottom_right_frame = ctk.CTkFrame(bottom_frame, width=350, height=490)
bottom_right_frame.place(x=500, y=175)

# Bottom Left: Dropdown Menu

dropdown_label1 = ctk.CTkLabel(bottom_left_frame, text="Select Object Size:")
dropdown_label1.grid(row=0, column=1, padx=10, pady=10)

selected_option = ctk.StringVar()
dropdown = ttk.Combobox(bottom_left_frame, textvariable=selected_option)
dropdown['values'] = ('36 in , 7.3 in', '30 in , 6.6 in', '24 in , 6 in','18 in , 5 in','12 in , 4 in')
dropdown.current(0)  # Set default selection
dropdown.grid(row=1, column=1, padx=10, pady=10)

dropdown_label2 = ctk.CTkLabel(bottom_left_frame, text="Scan Type:")
dropdown_label2.grid(row=0, column=2, padx=10, pady=10)

selected_option = ctk.StringVar()
dropdown = ttk.Combobox(bottom_left_frame, textvariable=selected_option)
dropdown['values'] = ('video', 'Image')
dropdown.current(0)  # Set default selection
dropdown.grid(row=1, column=2, padx=10, pady=10)

dropdown_label2 = ctk.CTkLabel(bottom_left_frame, text="Scan Quality:")
dropdown_label2.grid(row=2, column=2, padx=10, pady=10)

selected_option = ctk.StringVar()
dropdown = ttk.Combobox(bottom_left_frame, textvariable=selected_option)
dropdown['values'] = ('Complete', 'One Sample')
dropdown.current(0)  # Set default selection
dropdown.grid(row=3, column=1, padx=10, pady=10)

dropdown_label2 = ctk.CTkLabel(bottom_left_frame, text="Scan Area:")
dropdown_label2.grid(row=2, column=1, padx=10, pady=10)


selected_option = ctk.StringVar()
dropdown = ttk.Combobox(bottom_left_frame, textvariable=selected_option)
dropdown['values'] = ('Complete', 'One Sample')
dropdown.current(0)  # Set default selection
dropdown.grid(row=3, column=2, padx=10, pady=10)

# Top Right: Label
label = ctk.CTkLabel(top_frame, text="XYZ-Object Scan", font=("Arial", 30))
label.pack(padx=1, pady=1)

# Bottom Right: Button
button = ctk.CTkButton(bottom_right_frame, text="operate", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack( padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Pause", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack( padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Fetch Video/Image", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack( padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Perform Analysis", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack( padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Show Results", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack(padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Generate Report", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack(padx=10, pady=5)

button = ctk.CTkButton(bottom_right_frame, text="Go To Test Repository", width=200, height=30, command=on_button_click, corner_radius=10,border_width=5)
button.pack( padx=10, pady=5)

window.mainloop()