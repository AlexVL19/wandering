from turtle import distance, title
from typing import final
from wandering import commonWandering, wandering
from trail import Trail
from location import Location

from bokeh.plotting import figure, output_file, show

def typewanderingNow(type_wandering):
    if type_wandering.__name__ == "commonWandering":
        return "Errante común"
    elif type_wandering.__name__ == "wanderingRight":
        return "Errante derechista"
    else:
        return "Errante izquierdista"

def walking(wandering, steps, type_wandering):
    begin = [wandering.position()]

    x_grph = [0]
    y_grph = [0]

    for _ in range(steps-1):
        wandering.walk()
        x, y = wandering.position()
        x_grph.append(x)
        y_grph.append(y)

    typeNow = typewanderingNow(type_wandering)
    graph_steps(x_grph, y_grph, typeNow, steps)
    return wandering.dist_origin()

def simulate_walk(steps, atts, type_wandering):
    wandering = []
    distances = []

    for i in range(atts):
        wandering.append(type_wandering(name=f'Rasputin {i}'))
        sim_walk = walking(wandering[i], steps, type_wandering)
        distances.append(round(sim_walk,1))
    return distances

def graph_steps(x_graph, y_graph, type_wandering, steps):
    grph = figure(title=type_wandering, x_axis_label='Pasos', y_axis_label='Distancia')
    grph.line(x_graph, y_graph, legend_label=str(steps)+' pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    grph.diamond_cross(0, 0, fill_color="green", line_color="green", size=18)
    grph.diamond_cross(final_x, final_y, fill_color="red", line_color="red", size=18)
    str_finalx = [0, final_x]
    str_finaly = [0, final_y]
    grph.line(str_finalx, str_finaly, line_width=2, color="blue")
    show(grph)

def main(walk_dist, atts, type_wandering):

    for steps in walk_dist:
        distances = simulate_walk(steps, atts, type_wandering)
        avgdist = round(sum(distances) / len(distances), 4)
        maxdist = max(distances)
        mindist = min(distances)
        print(f'{type_wandering.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {avgdist}')
        print(f'Max = {maxdist}')
        print(f'Min = {mindist}')

if __name__ == '__main__':

    walk_dist = [10000]
    atts = 1
    main(walk_dist, atts, commonWandering)
