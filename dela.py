import tkinter as tk
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_website():
    webbrowser.open_new("https://gilaxy04ytbcompte2.github.io/loowriters")

def open_website_new():
    webbrowser.open_new("https://gilaxy04ytbcompte2.github.io/loowriters/news")

def open_website_rule():
    webbrowser.open_new("https://gilaxy04ytbcompte2.github.io/loowriters/rules")

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*."), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"loowriter | not save - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

window = tk.Tk()
window.title("loowriter")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=5)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
btn_web = tk.Button(fr_buttons, text="website", command=open_website)
btn_web_new = tk.Button(fr_buttons, text="new", command=open_website_new)
btn_web_credit = tk.Button(fr_buttons, text="credit", command=open_website_rule)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
btn_web.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_web_new.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_web_credit.grid(row=4, column=0, sticky="ew", padx=5,pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

menu_bar = tk.Menu(window)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="website", command=open_website)
menu_file.add_command(label="save", command=save_file)
menu_file.add_command(label="new", command=open_website_new)
menu_file.add_command(label="credit", command=open_website_rule)
menu_file.add_command(label="open", command=open)
menu_bar.add_cascade(label="menu", menu=menu_file)

window.config(menu=menu_bar)
window.mainloop()
