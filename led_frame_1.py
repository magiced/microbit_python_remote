import tkinter as tk

# change to button
# add list of colours to cycle through
# function to get colour



class ClickPixel(tk.Button):
    def __init__(self, parent, default_colour='black', x=4, y=2, **kwargs):
        # tk.Label.__init__(self, parent, **kwargs)

        self.colours = ['black', 'red', 'blue', 'yellow', 'green', 'white']

        self.current_colour_index = 0

        self.current_colour = default_colour

        self.pixel = tk.Button(parent, text='', bg=self.current_colour, justify='center', width=x, height=y, font=('bold'), command=self.cycle_colour, highlightcolor='white', highlightbackground='white',highlightthickness=1)

        # colour_now = self.get_colour()
        # # print(state_now)
        # self.set_colour(colour_now)

    """ set background colour """
    def set_bg_colour(self, colour):
        self.pixel['bg'] = colour

    """ Tkinter layout methods """    
    def grid(self, **kwargs):#row, column):
        self.pixel.grid(kwargs)#row=row,column=column)#, side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def pack(self, **kwargs):
        self.pixel.pack(kwargs)#(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    def lift(self, target):
        self.pixel.lift(target)
    
    """ Methods """
    
    def cycle_colour(self):
    # on each click cycle through list of colours
        self.current_colour_index += 1
        if (self.current_colour_index >= len(self.colours)):
            self.current_colour_index = 0
        self.set_colour(self.colours[self.current_colour_index])

    def get_colour(self):
        pass

    def set_colour(self,colour):
        self.pixel['bg'] = colour

    def reset_colour(self):
        self.current_colour_index = 0
        self.set_colour(self.colours[self.current_colour_index])

if __name__ == "__main__":

    def reset():
        for pixel in pixels:
            pixel.reset_colour()

    root = tk.Tk()

    num_cols = 5
    num_rows = 5

    num_pixels = num_cols * num_rows

    columns = []

    pixels = []

    for col in range(num_cols):
        for row in range(num_rows):
            this_pixel = ClickPixel(root)
            this_pixel.grid(row=row ,column=col)
            pixels.append(this_pixel)

    reset_button = tk.Button(root, text='reset', command=reset)
    reset_button.grid(row=num_rows+1, column=0)

    root.mainloop()