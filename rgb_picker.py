import tkinter as tk
import tkinter.ttk as ttk
from tkinter import font

def update_output_color(event=None):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()

    RGB = (red << 16) + (green << 8) + (blue)
    opposite_RGB = 0xFFFFFF - RGB
    
    RGB_text = f'#{red:0>2X}{green:0>2X}{blue:0>2X}'
    opposite_RGB_text = f'#{opposite_RGB:0>6X}'

    colour_output['bg'] = RGB_text
    colour_output['text'] = RGB_text
    colour_output['fg'] = opposite_RGB_text

def update_wheel_output_color(event=None):
    wheel_val = wheel_slider.get()

    rgb_vals = wheel(wheel_val)
    # print(rgb_vals)
    # try:
    red_val['text'] = rgb_vals[0]
    green_val['text'] = rgb_vals[1]
    blue_val['text'] = rgb_vals[2]

    RGB = (rgb_vals[0] << 16) + (rgb_vals[1] << 8) + (rgb_vals[2])

    red = f"#{rgb_vals[0]:0>2X}0000"
    green = f"#00{rgb_vals[1]:0>2X}00"
    blue = f"#0000{rgb_vals[2]:0>2X}"

    print(f"{red} {green} {blue}")

    red_val['bg'] = red
    green_val['bg'] = green
    blue_val['bg'] = blue

    opposite_RGB = 0xFFFFFF - RGB 
    RGB_text = f'#{RGB:0>6X}'
    opposite_RGB_text = f'#{opposite_RGB:0>6X}'

    colour_output['bg'] = RGB_text
    colour_output['text'] = RGB_text
    colour_output['fg'] = opposite_RGB_text
    # except:
    #     print('EXCEPTION')
    
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))

def wheel(WheelPos_in):
    WheelPos = (255 - WheelPos_in) % 256
    # if ((255 - WheelPos_in) > 0):
    #     WheelPos = 255 - WheelPos
    #     print(f"Wheel in: {WheelPos_in}, Wheel: {WheelPos} - pos")
    # else:
    #     WheelPos = 255 + (255 - WheelPos_in)
    #     print(f"Wheel in: {WheelPos_in}, Wheel: {WheelPos} - neg")
    # # WheelPos = constrain(WheelPos,0,255)
    r=0
    g=0
    b=0

    if (WheelPos < 85):
        r = 255 - (WheelPos * 3)
        g = 0
        b = WheelPos * 3
    elif (WheelPos < 170):
        WheelPos -= 85
        r = 0
        g = WheelPos * 3
        b = 255 - (WheelPos * 3)
    else:
        WheelPos -= 170
        r = WheelPos * 3
        g = 255 - (WheelPos * 3)
        b = 0

    # print(f"Wheel: {WheelPos}, R: {r}, G: {g}, B: {b}")
    r = r % 256
    g = g % 256
    b = b % 256
    print(f"Wheel In: {WheelPos_in},Wheel: {WheelPos}, R: {r}, G: {g}, B: {b}")
    rgb_vals = [r, g, b]
    # print(rgb_vals)

    return rgb_vals


root = tk.Tk()

thisFont = font.nametofont('TkHeadingFont')

output_frame = tk.Frame(root, border=3)
colour_output = tk.Label(output_frame, bg='grey', height=10, width=20, font=thisFont)
colour_output.pack(fill='both')
output_frame.pack()

rgb_readout_frame = tk.Frame(root)
red_val = tk.Label(rgb_readout_frame,text='---',width=6)
green_val = tk.Label(rgb_readout_frame,text='---',width=6)
blue_val = tk.Label(rgb_readout_frame,text='---',width=6)
red_val.pack(side='left',fill='x')
green_val.pack(side='left',fill='x')
blue_val.pack(side='left',fill='x')
rgb_readout_frame.pack()


slider_frame = tk.Frame(root)
red_slider = tk.Scale(slider_frame, orient='horizontal', background='red', from_=0, to=255, command=update_output_color)
green_slider = tk.Scale(slider_frame, orient='horizontal', background='green', from_=0, to=255, command=update_output_color)
blue_slider = tk.Scale(slider_frame, orient='horizontal', background='blue', from_=0, to=255, command=update_output_color)
red_slider.pack(fill='x')
green_slider.pack(fill='x')
blue_slider.pack(fill='x')
slider_frame.pack(fill='x')

wheel_slider_frame = tk.Frame(root)
wheel_slider = tk.Scale(wheel_slider_frame, orient='horizontal', from_=0, to=255, command=update_wheel_output_color)
wheel_slider.pack(fill='x')
wheel_slider_frame.pack(fill='x')

root.mainloop()