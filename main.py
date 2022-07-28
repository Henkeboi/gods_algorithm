from matplotlib import projections
import numpy as np
from enum import Enum

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d


class Z3:
    def __init__(self, instance : int):
        assert (instance > -1 and instance < 4)
        self.instance = instance
    def __add__(self, arg):
        self.instance = (self.instance + arg) % 3
        return self
    def value(self):
        return self.instance

class Mappings(Enum):
    F = 1

class Map: # f : G -> G
    def apply(self, instance, operation : Mappings):
        if operation == Mappings.F:
            self.F(instance)
    
    def swap(self, instance, a, b, c, d):
        store_a = instance[a]
        instance[a] = instance[d]
        instance[d] = instance[c]
        instance[c] = instance[b]
        instance[b] = store_a

    def F(self, instance):
        # Face 1
        self.swap(instance, 0, 5, 7, 2)
        self.swap(instance, 1, 3, 6, 4)
        # Face 2
        

# (G, *)
class G:
    def __init__(self):
        self.set = np.arange(48) + 1
        self.operation = Map()
    
    def scramble(self):
        self.operation.apply(self.set, Mappings.F)

    def plot_element(self, dir, x, y, z, ax, color):
        side = Rectangle((x, y), 0.97, 0.97, color=color)
        ax.add_patch(side)
        art3d.pathpatch_2d_to_3d(side, z=z, zdir=dir)

    def show(self): 
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        x = Z3(0)
        y = Z3(0)

        directions = ['y', 'x', 'z', 'x', 'z', 'y']
        colors = ['g', 'orange', 'y', 'red', 'white', 'b']
        x_offsets = [-1, 0, -1, 0, -1, -1]
        y_offsets = [-1, -1, 0, -1, 0, -1]
        z_offsets = [0, 2, 2, -1, -1, 3]

        for dir, color, x_offset, y_offset, z_offset in zip(directions, colors, x_offsets, y_offsets, z_offsets):
            for _ in range(0, 3):
                for _ in range(0, 3):
                    self.plot_element(dir, x.value() + x_offset, y.value() + y_offset, z_offset, ax, color=color)
                    y += 1
                x += 1

        ax.grid(False)
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.margins(0.8, 0.8, 0.8) 
        plt.show()


def main():
    cube = G()
    cube.scramble()
    cube.show()


if __name__ == '__main__':
    main()