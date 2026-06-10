import tkinter as tk
from tkinter import filedialog, messagebox
from tidy_folder import organise_folder, undo_moves

title_colour = "#000000" # Hex colour of the 'Tidy Folder' title
bg_colour = "#AAB9DA" # Hex background colour of root and widgets

last_move = [] # Tracks the most recent move
session_moves = [] # Tracks all moves during the GUI session


def browse_folder():
    chosen_path = filedialog.askdirectory()
    if chosen_path:
        folder_path.set(chosen_path)


def organise():
    global last_move
    global session_moves

    path = folder_path.get().strip()
    if not path:
        messagebox.showerror(
            "Error",
            "Please select a folder first."
        )
        return
    
    try:
        moved_files = organise_folder(path)

        if moved_files:
            last_move = moved_files # For undo last move
            session_moves.extend(moved_files) # For undo all moves

            status_label.config(
                text=f"Folder organised successfully! Moved {len(moved_files)} file(s)."
            )
            messagebox.showinfo(
                "Success",
                "Folder organised successfully!"
            )
        else:
            messagebox.showinfo(
                "No Files Found",
                "No files were found to organise."
            )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


def undo_last():
    global last_move

    if not last_move:
        messagebox.showinfo(
            "Undo",
            "Nothing to undo."
        )
        return
    try:
        undo_moves(last_move)

        for move in last_move: # Remove individual moves from session history
            if move in session_moves:
                session_moves.remove(move)
        last_move = []

        status_label.config(
            text="Undo completed."
        )
        messagebox.showinfo(
            "Success",
            "Undo completed."
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


def undo_all():
    global session_moves
    global last_move

    if not session_moves:
        messagebox.showinfo(
            "Undo All",
            "Nothing to undo."
        )
        return

    confirm = messagebox.askyesno(
        "Confirm Undo",
        "Are you sure you want to undo ALL moves this session?"
    )
    if not confirm:
        return

    try:
        undo_moves(session_moves.copy()) # Prevents list being affected during undo
        session_moves.clear()
        last_move = []

        status_label.config(
            text="All session moves undone."
        )
        messagebox.showinfo(
            "Success",
            "All session moves have been undone."
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


# GUI SETUP ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = tk.Tk()
root.title("Tidy Folder")
root.geometry("650x250")
root.resizable(False, False)
root.config(bg=bg_colour)


# GUI sections are ordered as viewed from top to bottom
# TITLE LABEL
title_label = tk.Label(
    root,
    text="Tidy Folder",
    font=("Segoe Script", 16, "bold"),
    fg=title_colour,
    bg=bg_colour
)
title_label.pack(pady=(20,10)) # Pad 20 pixels above, 10 pixels below


# FOLDER FRAME
folder_frame = tk.Frame(root, bg=bg_colour) # Frames are containers used to group widgets together
folder_frame.pack(pady=10)

folder_path = tk.StringVar()

folder_entry = tk.Entry(
    folder_frame,
    textvariable=folder_path,
    width=60
)
folder_entry.pack(side="left", padx=5)

browse_button = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder
)
browse_button.pack(side="left")


# BUTTON FRAME
button_frame = tk.Frame(root, bg=bg_colour)
button_frame.pack(pady=(15,5)) # Pad 15 above, 5 below (incase status_label gets long and takes many lines)

organise_button = tk.Button(
    button_frame,
    text="Organise Folder",
    width=18,
    command=organise
)
organise_button.grid(row=0, column=0, padx=5)

undo_button = tk.Button(
    button_frame,
    text="Undo Last Move",
    width=18,
    command=undo_last
)
undo_button.grid(row=0, column=1, padx=5)

undo_all_button = tk.Button(
    button_frame,
    text="Undo All Moves",
    width=18,
    command=undo_all
)
undo_all_button.grid(row=0, column=2, padx=5)


# STATUS LABEL
status_label = tk.Label(
    root,
    text="Select a folder to organise.",
    bg=bg_colour,
    wraplength=600 # Maximum number of pixels for each line
)

status_label.pack(pady=15)

root.mainloop()