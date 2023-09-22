import tkinter as tk

"""
# TODO
- [x] gamepad
    - seperate frame
    - 3x3 grid 
    - buttons in correct places
- [x] tie buttons to arrow keys
- [ ] turn into slice in tk library
- [ ] other command buttons
    - [ ] a b x y 
    - [ ] link to keys
    - [ ] create slice 

"""

def up_btn_pressed(event=None):
    # when this is called from the root.bind() function, it passes an event as a parameter
    # i don't need this, but if you don't account for it you get an error!
    print('up button pressed')

def down_btn_pressed(event=None):
    print('down button pressed')

def left_btn_pressed(event=None):
    print('left button pressed')

def right_btn_pressed(event=None):
    print('right button pressed')

root = tk.Tk()

dpad_frame = tk.Frame(root,bg='#000000')
# gamepad frame will be 3x3
d_btn_width = 10
d_btn_height = 5

arrow_size = 100
up_btn = tk.Button(dpad_frame, text='⇧', width=d_btn_width, height=d_btn_height, command=up_btn_pressed, font={'size':arrow_size})
down_btn = tk.Button(dpad_frame,text='⇩', width=d_btn_width, height=d_btn_height, command=down_btn_pressed, font={'size':arrow_size})
left_btn = tk.Button(dpad_frame,text='⇦', width=d_btn_width, height=d_btn_height, command=left_btn_pressed, font={'size':arrow_size})
right_btn = tk.Button(dpad_frame,text='⇨ ', width=d_btn_width, height=d_btn_height, command=right_btn_pressed, font={'size':arrow_size})

root.bind('<Up>',up_btn_pressed)
root.bind('<Down>',down_btn_pressed)
root.bind('<Left>',left_btn_pressed)
root.bind('<Right>',right_btn_pressed)

up_btn.grid(row=0,column=1)
down_btn.grid(row=2,column=1)
left_btn.grid(row=1,column=0)
right_btn.grid(row=1,column=2)

dpad_frame.pack()
root.mainloop()

