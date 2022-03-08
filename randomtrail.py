
from turtle import distance, title
from wandering import commonWandering, wandering
from trail import Trail
from location import Location

from bokeh.plotting import figure, output_file, show

def walking(location, wandering, steps):
    begin = location.get_location(wandering)

    for _ in range(steps):
        location.move_wandering(wandering)

    return begin.distance(location.get_location(wandering))

def simulate_walk(steps, atts, type_wandering):
    wandering = type_wandering(name='Alirio')
    origin = Trail(0,0)
    distances = []

    for _ in range(atts):
        location = Location()
        location.add_wandering(wandering, origin)
        sim_walk = walking(location, wandering, steps)
        distances.append(round(sim_walk,1))
    return distances

def graph(x, y):
    grph = figure(title='Camino del errante', x_axis_label='Pasos', y_axis_label='Distancia')
    grph.line(x, y, legend='Distancia')
    show(grph)

def main(walk_dist, atts, type_wandering):
    avgwalk_dist = []

    for steps in walk_dist:
        distances = simulate_walk(steps, atts, type_wandering)
        avgdist = round(sum(distances) / len(distances), 4)
        maxdist = max(distances)
        mindist = min(distances)
        avgwalk_dist.append(avgdist)
        print(f'{type_wandering.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {avgdist}')
        print(f'Max = {maxdist}')
        print(f'Min = {mindist}')
    
    graph(walk_dist, avgwalk_dist)

if __name__ == '__main__':

    walk_dist = [10, 100, 1000, 10000]
    atts = 100
    main(walk_dist, atts, commonWandering)