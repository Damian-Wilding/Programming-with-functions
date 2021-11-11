import tkinter as tk
import math
from PIL import *
from PIL.ImageTk import PhotoImage #Image, ImageTk

def main():
    # The width and height of the scene window.
    width = 805
    height = 505

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    draw_background(canvas, width, height)
    draw_clouds(canvas, 1, 100, 10, 4)
    draw_clouds(canvas, 300, 2, 5, 8)
    draw_ground(canvas, 35)
    draw_sun(canvas, 300, 100, 0.5)
    draw_question_block(canvas, 400, 250)
    draw_brick_block(canvas, 450, 250)
    draw_question_block(canvas, 500, 250)
    draw_question_block(canvas, 450, 50)
    draw_question_block(canvas, 150, 250)
    draw_brick_block(canvas, 350, 250)
    draw_brick_block(canvas, 550, 250)


    root.mainloop()


    #import mario
    #itsame = Image.open("mario.jpg")
    #mario = PhotoImage(file="mario.jpg")
    #canvas.create_image(400, 400, image = mario)

def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.

# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_background(canvas, width, height):
    canvas.create_rectangle(0, 0, width, height, fill="#3366CC")

def draw_clouds(canvas, x_start, y_start, amount_of_top_poofs, amount_of_bottom_poofs):
    x_spacing = 25
    y_spacing = 10
    height = 20
    width = 40
    total = 1
    for poofs in range(1, amount_of_top_poofs + 1):
        canvas.create_oval(x_start + total * x_spacing, y_start, x_start + total * x_spacing + width, y_start + height, outline="#ffffff", fill="#ffffff")
        total += 1
    total = 1
    for poofs in range(1, amount_of_bottom_poofs + 1):
        canvas.create_oval((x_start + total * x_spacing) + 0.5 * width, y_start + y_spacing, (x_start + total * x_spacing + 0.5 * width) + width, y_start + y_spacing + height, outline="#ffffff", fill="#ffffff")
        total += 1

def draw_ground(canvas, brick_width):
    ground_level = 450
    first_layer = 50 * 0.33333 + 450
    second_layer = 50 * 0.66666 +450
    rock_bottom = 505
    offset = brick_width * 0.5
    canvas.create_rectangle(0, 450, 800, 500, outline="#000000", fill="#800000", width="5")
    canvas.create_line(0, first_layer, 800, first_layer, width="4")
    canvas.create_line(0, second_layer, 800, second_layer, width="4")
    brick_number = 0
    for lines in range(0, 800, brick_width):
        canvas.create_line(brick_number * brick_width, ground_level, brick_width * brick_number, first_layer, width="4")
        brick_number += 1
    brick_number = 0
    for lines in range(0, 800, brick_width):
        canvas.create_line(brick_width * brick_number, second_layer, brick_number * brick_width, rock_bottom, width="4")
        brick_number += 1
    brick_number = 0
    for lines in range(0, 800, brick_width):
        canvas.create_line(brick_width * brick_number + offset, first_layer, brick_width * brick_number + offset, second_layer, width="4")
        brick_number += 1

def draw_sun(canvas, x_start, y_start, size):
    standard_sun_size = 100 * size
    eye_1_x = x_start + standard_sun_size * 1/6
    eye_1_y = y_start + standard_sun_size * 1/4
    eye_2_x = x_start + standard_sun_size * 4/6
    eye_2_y = y_start + standard_sun_size * 1/4
    eye_size = 0.25 * standard_sun_size
    x_crotch = x_start + standard_sun_size * 0.5
    y_crotch = y_start + standard_sun_size + standard_sun_size * 0.75
    canvas.create_oval(x_start, y_start, x_start + standard_sun_size, y_start + standard_sun_size, fill="#FFDB1A", width = 2)
    canvas.create_arc(eye_1_x, eye_1_y, eye_1_x + eye_size, eye_1_y + eye_size, start=180, extent=180, fill="#000000")
    canvas.create_arc(eye_2_x, eye_2_y, eye_2_x + eye_size, eye_2_y + eye_size, start=180, extent=180, fill="#000000")
    canvas.create_line(x_start, eye_1_y + 0.5 * eye_size, x_start + standard_sun_size, eye_1_y + 0.5 * eye_size, width="4")
    canvas.create_line(eye_1_x + 0.5 * eye_size, y_start + 0.75 * standard_sun_size, eye_2_x + 0.5 * eye_size, y_start + 0.75 * standard_sun_size, width="4")
    canvas.create_line(eye_2_x + 0.5 * eye_size, y_start + 0.75 * standard_sun_size, eye_2_x + 0.5 * eye_size, y_start + 0.75 * standard_sun_size - standard_sun_size * 0.1, width="4")
    canvas.create_rectangle(x_start, eye_1_y + 0.5 * eye_size - standard_sun_size * 0.1 - 8, x_start + standard_sun_size + 15, eye_1_y + 0.5 * eye_size - standard_sun_size * 0.1, fill = 'red', outline = 'red')
    canvas.create_rectangle(x_start + standard_sun_size * 0.15, y_start, x_start + standard_sun_size , eye_1_y + 0.5 * eye_size - standard_sun_size * 0.1 - 8, fill = 'red', outline = 'red')
    canvas.create_oval(x_start + 0.5 * standard_sun_size, y_start + standard_sun_size * 0.05, x_start + 0.5 * standard_sun_size + standard_sun_size * 0.15, y_start + standard_sun_size * 0.1 + standard_sun_size * 0.15, outline = 'white', fill = 'white')
    canvas.create_line(x_start + standard_sun_size * 0.5, y_start + standard_sun_size, x_start + standard_sun_size * 0.5, y_start + standard_sun_size + standard_sun_size * 0.75, width = 4)
    canvas.create_line(x_start, y_start + standard_sun_size + standard_sun_size * 0.75 * 0.5, x_start + standard_sun_size, y_start + standard_sun_size + standard_sun_size * 0.75 * 0.5, width = 4)
    canvas.create_line(x_start, y_crotch + standard_sun_size * 0.65, x_crotch, y_crotch, x_start + standard_sun_size, y_crotch + standard_sun_size * 0.65, width = 4)



def draw_question_block(canvas, x_start, y_start):
    x_end = x_start + 50
    y_end = y_start + 50
    x_middle = x_start + (0.5 * (x_end - x_start))
    y_middle = y_start + (0.5 * (y_end - y_start))
    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline = "#000000", width = "4", fill = '#FFD966')
    #canvas.create_text(x_start + 20, y_start + 20, text = "?", width = x_end - x_start - 10, fill = 'black')
    canvas.create_line(x_start + 10, y_start + 15, x_start + 10, y_start + 10, x_end - 10, y_start + 10, x_end - 10, y_start + 20, x_middle, y_start + 20, x_middle, y_start + 30, width = 3)
    canvas.create_line(x_middle, y_start + 35, x_middle, y_start + 38, width = 3)

def draw_brick_block(canvas, x_start, y_start):
    x_end = x_start + 50
    y_end = y_start + 50
    second_line = y_start + 0.3333 * 50
    third_line = y_start + 0.6666 * 50
    x_middle = x_start + (0.5 * (x_end - x_start))
    x_first_line = x_middle - (third_line - second_line)
    x_second_line = x_middle + (third_line - second_line)
    canvas.create_rectangle(x_start, y_start, x_end, y_end, outline = '#000000', width = 4, fill = '#800000')
    canvas.create_line(x_start, second_line, x_end, second_line, width = 4)
    canvas.create_line(x_start, third_line, x_end, third_line, width = 4)
    canvas.create_line(x_middle, second_line, x_middle, third_line, width = 4)
    canvas.create_line(x_first_line, y_start, x_first_line, second_line, width = 4)
    canvas.create_line(x_first_line, third_line, x_first_line, y_end, width = 4)
    canvas.create_line(x_second_line, y_start, x_second_line, second_line, width = 4)
    canvas.create_line(x_second_line, third_line, x_second_line, y_end, width = 4)


# Call the main function so that
# this program will start executing.
main() 