import tkinter as tk

window = tk.Tk()
window.title("Test Button")
window.geometry("300x200")


def say_hello():
    print("✅ Button works")


tk.Button(window, text="TEST SPEAK", command=say_hello).pack(pady=20)

window.mainloop()
