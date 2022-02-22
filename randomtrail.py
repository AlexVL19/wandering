import imp
from turtle import title
from wandering import commonWandering, wandering
from trail import trail
from location import location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    begin = location.get_location(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)

        return begin.distance(location.get_location(wandering))

def simulate_walk(steps, atts, type_wandering):
    wandering = type_wandering(name='Alirio')
    origin = location(0,0)
    distances = []

    for _ in range(atts):
        trail = trail()
        trail.add_wandering(wandering, origin)
        sim_walk = walking(trail, wandering, steps)
        distances.append(round(sim_walk,1))
    
    return distances

def graph(x, y):
    grph = figure(title='Camino del errante', x_axis_label='Pasos', y_axis_label='Distancia')
    grph.line(x, y, legend='Distancia')
    show(grph)