import tkinter as tk
root = tk.Tk()
root.title('Zoom Mic Control')

frame = tk.Frame(root)
frame.pack(padx=15)

tk.Label(frame, text="Zoom Status").pack(side=tk.LEFT)
tk.Label(frame, text="RPi Status").pack(side=tk.RIGHT)

frame=tk.Frame(root)
frame.pack(padx=15)

tk.Button(frame, text="On Air").pack(fill=tk.X)
tk.Label(frame, text="Mic Status").pack(side=tk.LEFT)
tk.Label(frame, text="Light Status").pack(side=tk.RIGHT)

root.mainloop()