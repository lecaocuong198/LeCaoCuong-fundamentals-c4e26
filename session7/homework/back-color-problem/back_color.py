from random import *
import check_color

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    c = choice(shapes)
    m = choice(shapes)
    meaning = c['text']
    color = m['color']
    return[meaning,color,randint(0,1)]
    

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:
        if text == 'blue':
            rect = [20, 60, 100, 100]
        if text == 'red':
            rect = [140, 60, 100, 100]
        if text == 'yellow':
            rect = [20, 180, 100, 100]
        if text == 'green':
            rect =[140, 180, 100, 100]
        check = check_color.is_inside(x,y,rect)
    else:
        if color == '#3F51B5':
            rect = [20, 60, 100, 100]
        if color == '#C62828':
            rect = [140, 60, 100, 100]
        if color == '#FFD600':
            rect = [20, 180, 100, 100]
        if color == '#4CAF50':
            rect =[140, 180, 100, 100]
        check = check_color.is_inside(x,y,rect)
    return check
