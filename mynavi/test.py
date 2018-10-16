#!python3

import tkinter as tk
import os

f = tk.Frame()
font = ('Arial', 14, 'bold')
for i in os.listdir('.'):
	label = tk.Label(text=i, font=font)
	label.pack(side=tk.LEFT)

f.pack()	
f.mainloop()
