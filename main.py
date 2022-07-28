import time
import tkinter as tk
import datetime
from dateutil.relativedelta import relativedelta
import customtkinter
from PIL import Image, ImageTk
import threading

customtkinter.set_appearance_mode("dark")
dt = datetime.datetime

# from_str = str(input("Enter a start date (format: yyyy-mm-dd hh:mm:ss): "))
# to = str(input("Enter a final date (format: yyyy-mm-dd hh:mm:ss): "))


def get_countdown(from_date, to_date):
    rdelta = relativedelta(to_date, from_date)
    result_list = [rdelta.years, rdelta.months, rdelta.days, rdelta.hours, rdelta.minutes, rdelta.seconds]
    print(f"[SUCCESS] Difference: {rdelta.years} years {rdelta.months} months {rdelta.days} days and {rdelta.hours} hours, {rdelta.minutes} minutes, {rdelta.seconds} seconds")
    show_result(result_list)

def convert_str_to_date(from_string,to_string):
    try:
        from_list = str(from_string).split(" ")
        from_date_list = str(from_list[0]).split("-")
        from_time_list = str(from_list[1]).split(":")
        from_time = datetime.datetime(year=int(from_date_list[0]),month=int(from_date_list[1]),day=int(from_date_list[2]),hour=int(from_time_list[0]),minute=int(from_time_list[1]),second=int(from_time_list[2]))
        print("[SUCCESS] Successfully transformed from_time", from_time)
        to_list = str(to_string).split(" ")
        to_date_list = str(to_list[0]).split("-")
        to_time_list = str(to_list[1]).split(":")
        to_time = datetime.datetime(year=int(to_date_list[0]),month=int(to_date_list[1]),day=int(to_date_list[2]),hour=int(to_time_list[0]),minute=int(to_time_list[1]),second=int(to_time_list[2]))
        print("[SUCCESS] Successfully transformed to_time", to_time)
        get_countdown(from_time, to_time)
    except Exception as e:
        calculation_error = customtkinter.CTkToplevel()
        calculation_error.geometry("350x100")
        calculation_error.resizable(False, False)
        calculation_error.title("Error")
        calculation_error.iconbitmap("./assets/error.ico")
        calculation_error.configure(background="#2B2B2B")
        calculation_error_label = customtkinter.CTkLabel(calculation_error, text="You did not entered at least one of the dates.", text_font=("Calibri Bold", 12))
        calculation_error_label.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    # return from_time, to_time

def close_program():
    window.destroy()
# from_t, to_t = convert_str_to_date(from_str, to)
# result = get_countdown(from_t, to_t)
# print(result)

window = customtkinter.CTk()
window.title("Countdown Calculator - Made by ARN0LD")
window.iconbitmap("./assets/calculator.ico")
window.configure(background="#2B2B2B")
window.geometry("800x500")

enter_from_date_label = customtkinter.CTkLabel(master=window, text='Enter "from" date:', text_font=("Calibri Bold", 12))
enter_from_date_label.configure(text_color="#FFFFFF")
enter_from_date_label.place(x=20, y=10)

entry_from_date = customtkinter.CTkEntry(master=window, placeholder_text="yyyy-mm-dd hh:mm:ss", width=170, height=30, text_font=("Calibri Bold", 12))
entry_from_date.configure(corner_radius=5)
entry_from_date.place(x=23, y=45)

def switch_event():
    current_time_thread = threading.Thread(target=switch_action, name="current_time")
    current_time_thread.start()
    if switch_1.get() == "on":
        print("_______Threads_______")
        for thread in threading.enumerate():
            print(thread.name)
    elif switch_1.get() == "off":
        entry_from_date.delete(0, tk.END)

def switch_action():
    while switch_1.get() == "on":
        x = datetime.datetime.now()
        entry_from_date.delete(0, tk.END)
        entry_from_date.insert(0, f"{x.year}-{x.month}-{x.day} {x.hour}:{x.minute}:{x.second}")
        time.sleep(1)

switch_var = customtkinter.StringVar(value="off")

switch_1 = customtkinter.CTkSwitch(master=window, text="Count from current time", command=switch_event,
                                   variable=switch_var, onvalue="on", offvalue="off", text_font=("Calibri Bold", 10))
switch_1.place(x=20, y=90)



enter_to_date_label = customtkinter.CTkLabel(master=window, text='Enter "to" date:', text_font=("Calibri Bold", 12))
enter_to_date_label.configure(text_color="#FFFFFF")
enter_to_date_label.place(x=230, y=10)

entry_to_date = customtkinter.CTkEntry(master=window, placeholder_text="yyyy-mm-dd hh:mm:ss", width=170, height=30, text_font=("Calibri Bold", 12))
entry_to_date.configure(corner_radius=5)
entry_to_date.place(x=243, y=45)

calculate_icon = ImageTk.PhotoImage(Image.open("./assets/calculate_icon.png").resize((17,17), Image.ANTIALIAS))
calculate_button = customtkinter.CTkButton(master=window, image=calculate_icon, text="Calculate", compound="left", command= lambda:convert_str_to_date(entry_from_date.get(), entry_to_date.get()), width=200, height=60, text_font=("Calibri Bold", 12))
calculate_button.configure(fg_color="#484848", corner_radius=14, hover_color="#515151")
calculate_button.pack(ipadx=5, ipady=5, expand=True)
calculate_button.place(x=520, y=20)

close_icon = ImageTk.PhotoImage(Image.open("./assets/close_icon.png").resize((17,17), Image.ANTIALIAS))
exit_button = customtkinter.CTkButton(master=window, image=close_icon, text="Exit", compound="left", command=close_program, width=100, height=35, text_font=("Calibri Bold", 12))
exit_button.configure(fg_color="#484848", corner_radius=14, hover_color="#515151")
exit_button.pack(ipadx=5, ipady=5, expand=True)
exit_button.place(x=690, y=450)

def show_result(result_dict):
    years_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[0]}", text_font=("Calibri Bold", 100), bg_color="#2B2B2B")
    years_count_label.configure(text_color="#FFFFFF")
    years_count_label.place(x=105, y=180)
    years_label = customtkinter.CTkLabel(master=window, text=f"year(s)", text_font=("Calibri Bold", 15), width=20, bg_color="#2B2B2B")
    years_label.configure(text_color="#FFFFFF")
    years_label.place(x=210, y=284)

    months_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[1]}", text_font=("Calibri Bold", 100), width=20)
    months_count_label.configure(text_color="#FFFFFF")
    months_count_label.place(x=300, y=180)
    months_label = customtkinter.CTkLabel(master=window, text=f"month(s)", text_font=("Calibri Bold", 15), width=20)
    months_label.configure(text_color="#FFFFFF")
    months_label.place(x=370, y=284)

    days_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[2]}", text_font=("Calibri Bold", 100), width=20)
    days_count_label.configure(text_color="#FFFFFF")
    days_count_label.place(x=475, y=180)
    days_label = customtkinter.CTkLabel(master=window, text=f"day(s)", text_font=("Calibri Bold", 15), width=20)
    days_label.configure(text_color="#FFFFFF")
    days_label.place(x=560, y=284)

    hours_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[3]}", text_font=("Calibri Bold", 15), width=20)
    hours_count_label.configure(text_color="#FFFFFF")
    hours_count_label.place(x=220, y=320)
    hours_label = customtkinter.CTkLabel(master=window, text=f"hour(s)", text_font=("Calibri Bold", 15), width=20)
    hours_label.configure(text_color="#FFFFFF")
    hours_label.place(x=245, y=320)

    minutes_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[4]}", text_font=("Calibri Bold", 15), width=20)
    minutes_count_label.configure(text_color="#FFFFFF")
    minutes_count_label.place(x=315, y=320)
    minutes_label = customtkinter.CTkLabel(master=window, text=f"minute(s)", text_font=("Calibri Bold", 15), width=20)
    minutes_label.configure(text_color="#FFFFFF")
    minutes_label.place(x=333, y=320)


    seconds_count_label = customtkinter.CTkLabel(master=window, text=f"{result_dict[5]}", text_font=("Calibri Bold", 15), width=20)
    seconds_count_label.configure(text_color="#FFFFFF")
    seconds_count_label.place(x=425, y=320)
    seconds_label = customtkinter.CTkLabel(master=window, text=f"second(s)", text_font=("Calibri Bold", 15), width=20)
    seconds_label.configure(text_color="#FFFFFF")
    seconds_label.place(x=450, y=320)

window.resizable(False,False)
window.mainloop()