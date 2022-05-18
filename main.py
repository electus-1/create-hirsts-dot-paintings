import colorgram
import random
import turtle

"""There are external dependencies in this programme. 
Both colorgram and turtle modules must be installed in order for the programme to work."""


def extract_palette(filename, num_of_colors):
    """Extracts the color palette of the given file. Uses colorgram module. The colormode of the turtle must be 255. Takes two inputs:
    filename: Full name of the file(with it's extension).
    num_of_colors: Number of colors that you want to extract from the palette.
    Returns a list of rgb colors which are represented as tuples."""
    colors = colorgram.extract(filename, num_of_colors)
    list_of_rgb = []
    for color in colors:
        red = color.rgb[0]
        green = color.rgb[1]
        blue = color.rgb[2]
        list_of_rgb.append((red, green, blue))
    list_of_whitish_colors = [
        (255, 255, 255),
        (248, 248, 255),
        (255, 250, 250),
        (245, 255, 250),
        (240, 248, 255),
        (240, 255, 240),
        (240, 255, 255),
        (255, 240, 245),
        (255, 245, 238),
        (255, 250, 240),
        (255, 255, 240),
        (245, 245, 245),
        (253, 245, 230),
        (250, 240, 230),
        (245, 245, 220),
        (250, 235, 215),
    ]
    for color in list_of_rgb:
        if color in list_of_whitish_colors:
            list_of_rgb.remove(color)
    return list_of_rgb


def make_hirst_painting(any_turtle, color_list, horizontal, vertical):
    """Makes the painting in the turtle screen. Takes 4 arguments:
    any_turtle: A Turtle object.
    color_list: A list of colors which are represented as tuples.
    horizontal: Number of spots that are paralel to x-axis.
    vertical: Number of spots that are paralel to y-axis.
    Returns none.
    Note: You should instantiate a Screen object and modify it to exit on click so that the method would work efficiently. Otherwise the
    screen would shut down in mere milliseconds."""
    was_pen_down = any_turtle.isdown()
    was_turtle_visible = any_turtle.isvisible()
    any_turtle.hideturtle()
    any_turtle.penup()
    any_turtle.goto(-300, -300)
    for _ in range(horizontal):
        for _ in range(vertical):
            random_color = random.choice(color_list)
            any_turtle.color(random_color)
            any_turtle.begin_fill()
            any_turtle.circle(20)
            any_turtle.end_fill()
            any_turtle.fd(70)

        any_turtle.backward(700)
        any_turtle.left(90)
        any_turtle.fd(60)
        any_turtle.right(90)
    any_turtle.home()
    if was_pen_down:
        any_turtle.pendown()
    if was_turtle_visible:
        any_turtle.showturtle()


ferhat = turtle.Turtle()
ferhat.speed(0)
ferhat.hideturtle()
screen = turtle.Screen()
turtle.colormode(255)


make_hirst_painting(ferhat, extract_palette("hirst-spot-painting.jpg", 100), 10, 10)
screen.exitonclick()
