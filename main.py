from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
MARK = "✔"

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_mark.config(text="")
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_sek = WORK_MIN * 60
    short_break_sek = SHORT_BREAK_MIN * 60
    long_break_sek = LONG_BREAK_MIN * 60

    reps += 1

    if reps in [1, 3, 5, 7]:
        count_down(work_sek)
        timer_label.config(text="Work", fg=GREEN)

    elif reps in [2, 4, 6]:
        count_down(short_break_sek)
        timer_label.config(text="Break", fg=PINK)

    elif reps == 8:
        count_down(long_break_sek)
        timer_label.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global mark
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            mark = mark + MARK
            check_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodorg")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# TIMER
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

# BUTTON START
button_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), command=start_timer)
button_start.grid(column=0, row=2)

# BUTTON RESET
button_reset = Button(text="Reset", font=(FONT_NAME, 10, "bold"), command=reset_timer)
button_reset.grid(column=2, row=2)

# CHECK MARK
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
