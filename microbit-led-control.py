import tkinter as tk

import logging
import time

from kaspersmicrobit import KaspersMicrobit
from kaspersmicrobit.services.leddisplay import Image, LedDisplay

logging.basicConfig(level=logging.INFO)

class ClickPixel(tk.Button):
    def __init__(self, parent, default_colour='black', x=4, y=2, **kwargs):
        # tk.Label.__init__(self, parent, **kwargs)

        self.colours = ['black', 'red', 'blue', 'yellow', 'green', 'white']

        self.current_colour_index = 0

        self.default_colour = default_colour
        self.current_colour = default_colour
        self.active_colour = 'red'
        self.button_state = False

        self.active_function = 'toggle' # toggle or cycle colour for the moment

        self.pixel = tk.Button(parent, text='', bg=self.current_colour, justify='center', width=x, height=y, font=('bold'), command=self.click_function, highlightcolor='white', highlightbackground='white',highlightthickness=1)

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

    def click_function(self):
        if (self.active_function == 'toggle'):
            self.toggle_state()
        elif (self.active_function == 'cycle_colour'):
            self.cycle_colour()
        else: # default state
            self.toggle_state()
    
    def set_click_function(self,function):
        self.click_function = function

    def toggle_state(self):
        if self.button_state:
            self.button_state = False
            self.set_colour(self.default_colour)
        else:
            self.button_state = True
            self.set_colour(self.active_colour)

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

    def set_active_colour(self,colour):
        self.active_colour = colour

    def set_default_colour(self,colour):
        self.default_colour = colour
    
    def get_button_state(self):
        return self.button_state

    def reset(self):
        self.set_colour(self.default_colour)
        self.button_state = False

class PixelFrame(tk.Frame):
    pass

if __name__ == "__main__":

    def reset():
        for row in pixels:
            for pixel in row:
                pixel.reset()
        get_led_matrix()

    def get_state():
        out_string = ''
        for row in pixels:
            for pixel in row:
                out_string += f"{pixel.get_button_state()}\t"
            out_string += "\n"
        print(out_string)

    def get_led_matrix():
        out_string = ''
        for row in pixels:
            for pixel in row:
                if pixel.get_button_state():
                    out_string += '# '
                else:
                    out_string += '. '
            out_string += "\n"
        print(out_string)
        microbit.led.show(LedDisplay.image(out_string))        

    root = tk.Tk()

    num_cols = 5
    num_rows = 5

    num_pixels = num_cols * num_rows

    pixels = []

    for row in range(num_rows):
        this_row = []
        for col in range(num_cols):
            this_pixel = ClickPixel(root)
            this_pixel.grid(row=row ,column=col)
            this_pixel.set_active_colour('red')
            this_row.append(this_pixel)
        pixels.append(this_row)

    reset_button = tk.Button(root, text='reset', command=reset)
    reset_button.grid(row=num_rows+1, column=0)

    get_state_button = tk.Button(root, text='State', command=get_led_matrix)
    get_state_button.grid(row=num_rows+1, column=num_cols-1)

    with KaspersMicrobit.find_one_microbit(timeout=3600) as microbit:    
        root.mainloop()