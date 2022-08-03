from abc import ABC, abstractmethod
from enum import Enum
import random

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import Axes3D 
import mpl_toolkits.mplot3d.art3d as art3d

# (ℤз, +)
class ℤз:
    def __init__(self, instance : int):
        assert (instance > -1 and instance < 4) # {0, 1, 2}
        self.instance = instance

    def __add__(self, arg):
        self.instance = (self.instance + arg) % 3
        return self

    def value(self):
        return self.instance

# (G, *)
class G(ABC):
    def __init__(self):
        self.operations = [self.F, self.F_squared, self.F_inverse, \
            self.B, self.B_squared, self.B_inverse, \
            self.U, self.U_squared, self.U_inverse, \
            self.D, self.D_squared, self.D_inverse, \
            self.L, self.L_squared, self.L_inverse, \
            self.R, self.R_squared, self.R_inverse] 
        self.cube = np.arange(54) + 1

    def apply(self, instance, operation):
        self.operations[operation](instance)

    def calculate_coset(self, G, H):
        pass


    def scramble(self):
        for _ in range(1000):
            self.apply(self.cube, random.choice([i for i in range(len(self.operations))]))

    def __plot_element(self, dir, x, y, z, ax, color):
        side = Rectangle((x, y), 0.97, 0.97, color=color)
        ax.add_patch(side)
        art3d.pathpatch_2d_to_3d(side, z=z, zdir=dir)

    def show(self): 
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        x = ℤз(0)
        y = ℤз(0)

        directions = ['y', 'x', 'z', 'x', 'z', 'y']
        colors = ['g', 'orange', 'y', 'red', 'white', 'b']
        x_offsets = [-1, -1, -1, -1, -1, -1]
        y_offsets = [-1, -1, -1, -1, -1, -1]
        z_offsets = [-1, 2, 2, -1, -1, 2]

        cube_index = 0
        for dir, color, x_offset, y_offset, z_offset in zip(directions, colors, x_offsets, y_offsets, z_offsets):
            for _ in range(0, 3):
                for _ in range(0, 3):
                    color = colors[(self.cube[cube_index] - 1) // 9]
                    self.__plot_element(dir, x.value() + x_offset, y.value() + y_offset, z_offset, ax, color=color)
                    cube_index += 1
                    x += 1
                y += 1

        ax.grid(False)
        ax.axis('off')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        ax.margins(0.8, 0.8, 0.8) 
        plt.show()

    def __swap_4(self, instance, a, b, c, d):
        store_a = instance[a]
        instance[a] = instance[d]
        instance[d] = instance[c]
        instance[c] = instance[b]
        instance[b] = store_a

    def F(self, instance):
        self.__swap_4(instance, 0, 6, 8, 2)
        self.__swap_4(instance, 1, 3, 7, 5)
        self.__swap_4(instance, 18, 15, 38, 27)
        self.__swap_4(instance, 19, 12, 37, 30)
        self.__swap_4(instance, 20, 9, 36, 33)

    def F_squared(self, instance):
        self.F(instance)
        self.F(instance)

    def F_inverse(self, instance):
        self.F(instance)
        self.F(instance)
        self.F(instance)

    def B(self, instance):
        self.__swap_4(instance, 45, 51, 53, 47)
        self.__swap_4(instance, 46, 48, 52, 50)
        self.__swap_4(instance, 24, 17, 44, 29)
        self.__swap_4(instance, 25, 14, 43, 32)
        self.__swap_4(instance, 26, 11, 42, 35)

    def B_squared(self, instance):
        self.B(instance)
        self.B(instance)

    def B_inverse(self, instance):
        self.B(instance)
        self.B(instance)
        self.B(instance)

    def U(self, instance):
        self.__swap_4(instance, 6, 35, 53, 15)
        self.__swap_4(instance, 7, 34, 52, 16)
        self.__swap_4(instance, 8, 33, 51, 17)
        self.__swap_4(instance, 18, 24, 26, 20)
        self.__swap_4(instance, 19, 21, 25, 23)

    def U_squared(self, instance):
        self.U(instance)
        self.U(instance)

    def U_inverse(self, instance):
        self.U(instance)
        self.U(instance)
        self.U(instance)

    def D(self, instance):
        self.__swap_4(instance, 0, 9, 47, 29)
        self.__swap_4(instance, 1, 10, 46, 28)
        self.__swap_4(instance, 2, 11, 45, 27)
        self.__swap_4(instance, 36, 38, 44, 42)
        self.__swap_4(instance, 37, 41, 43, 39)

    def D_squared(self, instance):
        self.D(instance)
        self.D(instance)

    def D_inverse(self, instance):
        self.D(instance)
        self.D(instance)
        self.D(instance)

    def L(self, instance):
        self.__swap_4(instance, 6, 36, 45, 24)
        self.__swap_4(instance, 3, 39, 48, 21)
        self.__swap_4(instance, 0, 42, 51, 18)
        self.__swap_4(instance, 27, 29, 35, 33)
        self.__swap_4(instance, 28, 32, 34, 30)

    def L_squared(self, instance):
        self.L(instance)
        self.L(instance)

    def L_inverse(self, instance):
        self.L(instance)
        self.L(instance)
        self.L(instance)

    def R(self, instance):
        self.__swap_4(instance, 2, 20, 53, 44)
        self.__swap_4(instance, 5, 23, 50, 41)
        self.__swap_4(instance, 8, 26, 47, 38)
        self.__swap_4(instance, 9, 15, 17, 11)
        self.__swap_4(instance, 10, 12, 16, 14)

    def R_squared(self, instance):
        self.R(instance)
        self.R(instance)

    def R_inverse(self, instance):
        self.R(instance)
        self.R(instance)
        self.R(instance)

class G0(G):
    def __init__(self):
        super().__init__()
        self.operations = [self.F, self.B, self.U,  \
            self.D, self.L, self.R
        ] 
 

class G1(G):
    def __init__(self):
        super().__init__()
        self.operations = [self.F, self.B, self.U_squared,  \
            self.D_squared, self.L, self.R
        ] 
 
class G2(G):
    def __init__(self):
        super().__init__()
        self.operations = [self.F_squared, self.B_squared, self.U_squared,  \
            self.D_squared, self.L, self.R
        ] 

class G3(G):
    def __init__(self):
        super().__init__()
        self.operations = [self.F_squared, self.B_squared, self.U_squared,  \
            self.D_squared, self.L_squared, self.R_squared
        ] 
 
class G4(G):
    def __init__(self):
        super().__init__()
        self.operations = [] 