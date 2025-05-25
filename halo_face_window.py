import tkinter as tk
from PIL import Image, ImageTk, ImageSequence


class HaloFaceWindow:
    def __init__(self, parent, gif_path):
        self.root = tk.Toplevel(parent)
        self.root.title("Halo's Face")
        self.root.resizable(False, False)

        # Wait until the main window is fully rendered
        parent.update_idletasks()

        # try to calculate position next to main window
        x = parent.winfo_x() + parent.winfo_width() + 20
        y = parent.winfo_y()
        self.root.geometry(f"300x300+{x}+{y}")

        self.label = tk.Label(self.root)
        self.label.pack()

        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0

        self.update_frame()


    def update_frame(self):
        frame = self.frames[self.frame_index]
        self.label.configure(image=frame)
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.root.after(100, self.update_frame)  # adjust for speed


def show_halo_face(parent):
    HaloFaceWindow(parent, "halo_face.gif")



# Test
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide main window
    show_halo_face()
    root.mainloop()
