
import tkinter
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = ("Courier", 24, "bold")
SECONDS = 0
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 4 == 1 or 3:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)
        reps += 1
    elif reps % 4 == 2:
        countdown(short_break_sec)
        timer.config(text="Break", fg=PINK)
        reps += 1
    elif reps % 4 == 0:
        countdown(long_break_sec)
        timer.config(text="Break", fg=RED)
        reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_secs = count % 60
    if count_secs < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")
    if count != 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            mark = ""
            for _ in range(math.floor(reps/2)):
                mark += "✔"
                checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Labels
timer = tkinter.Label(text="Timer", font=FONT, bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)

#Buttons
# TODO:Create start Time Function
start_button = tkinter.Button(text="Start", bg=YELLOW, font=("Courier", 10, "bold"), command=start_timer)
start_button.grid(column=0, row=3)
# TODO:Create Reset Time function
reset_button = tkinter.Button(text="Reset", bg=YELLOW, font=("Courier", 10, "bold"), command=reset_timer)
reset_button.grid(column=3, row=3)
# Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo)
timer_text = canvas.create_text(100, 130, text="00:00", font=FONT)
canvas.grid(column=1, row=1)

checkmark = tkinter.Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)
window.mainloop()
