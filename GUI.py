import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext 

def gui_init(parse_event_log):
    window = Tk()
    window.title("Event Log Incident of Fault Sequence Counter")
    window.geometry('500x475')
    window.resizable(False, False)
    # If I had more time I'd make it resizable but it adds considerable UI complexity 

    create_intro_lable(window)
    results_display, results_frame = create_result_display(window)

    create_open_file_button(window, parse_event_log, results_display)
    results_frame.pack()
    create_clear_window_button(window, results_display)

    window.mainloop()

def open_file():
    try:
        log_name = filedialog.askopenfilename(title="Open CSV File", 
                                              filetypes=[("CSV Files", ".csv"),
                                                         ("Text Files", ".txt")])
        if(log_name==""):
            raise ValueError("file selection empty")
    except:
        raise ValueError("file selection failed")
    return log_name

def display_results(incident_count, incident_details, time_array, text_error_count, log_name):
    string_text = "File Name: " + log_name + "\n"
    string_text =  string_text + "Incident Count :  " + str(incident_count) + "\n"
    string_text =  string_text + "Incidents Details \n"
    count = 1
    for error in incident_details:
        string_text = string_text + "Incident - " + str(count) + "\n"
        string_text = string_text + "Time Start: " + str(time_array[error[0]]) + "\n"
        string_text = string_text + "Time End: " + str(time_array[error[1]]) + "\n"
        string_text = string_text + "Line Start: " + str(error[0]) + "\n"
        string_text = string_text + "Line End: " + str(error[1]) + "\n" + "\n"
        count = count + 1
    text_error_count.config(state=NORMAL)
    text_error_count.insert(INSERT, string_text)
    text_error_count.config(state=DISABLED) 

# Helpers
def create_intro_lable(window):
    frame = tk.Frame(window, height=100, pady=10)
    text_intro = "Event Log Incident of Fault Sequence Counter \n \n"
    text_intro = text_intro + "This program can read through a log file to find incidents"
    text_intro = text_intro + " of a design flaw. \n"
    text_intro = text_intro + "Select a file to parse and the program will return the number \n"
    text_intro = text_intro + " of incidents and the details for each incident."
    label_intro = Label(frame, text = text_intro)
    label_intro.grid(row=0)
    frame.pack()

def create_result_display(window):
    frame = tk.Frame(window, height=100, pady= 10)    
    results_display = scrolledtext.ScrolledText(frame, height= 15, width= 50)
    results_display.config(state=tk.DISABLED)
    results_display.pack()
    return results_display, frame

def create_open_file_button(window, parse_event_log, results_display):
    frame = tk.Frame(window, height=100)
    button_open_file_lable = Label(frame, text = "Open File to Scan for Flaw Incidents \n")
    button_open_file = Button(frame, text = "Open File" ,
             fg = "black", command= lambda:parse_event_log(results_display))
    button_open_file_lable.grid(column=1, row=0)
    button_open_file.grid(column=1, row=1)
    frame.pack()

def create_clear_window_button(window, results_display):
    frame = tk.Frame(window, pady=10)
    button_clear_window = Button(frame, text = "Clear" ,
             fg = "black", command= lambda:clear_text_window(results_display))
    button_clear_window.pack()
    frame.pack(side=tk.RIGHT, padx=50)

def clear_text_window(window):
    window.config(state=NORMAL)
    window.delete(1.0,END)
    window.config(state=DISABLED) 