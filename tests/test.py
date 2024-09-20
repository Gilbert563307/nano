import tkinter as tk

# Function to switch between frames
def open_frame1():
    frame2.pack_forget()  # Hide frame2 if it's visible
    frame1.pack(fill="both", expand=True)  # Show frame1

def open_frame2():
    frame1.pack_forget()  # Hide frame1 if it's visible
    frame2.pack(fill="both", expand=True)  # Show frame2

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")  # Set the size of the main window

# Create two frames
frame1 = tk.Frame(root, bg="lightblue")
frame2 = tk.Frame(root, bg="lightgreen")

# Add content to frame 1
label1 = tk.Label(frame1, text="This is Frame 1", bg="lightblue")
label1.pack(pady=20)
button_to_frame2 = tk.Button(frame1, text="Go to Frame 2", command=open_frame2)
button_to_frame2.pack(pady=20)

# Add content to frame 2
label2 = tk.Label(frame2, text="This is Frame 2", bg="lightgreen")
label2.pack(pady=20)
button_to_frame1 = tk.Button(frame2, text="Go to Frame 1", command=open_frame1)
button_to_frame1.pack(pady=20)

# Start by showing frame 1
frame1.pack(fill="both", expand=True)

# Start the Tkinter event loop
root.mainloop()
