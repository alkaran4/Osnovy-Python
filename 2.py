class Road:

    density = 25
    thickness = 0.07

    def weight(self, length, width):
        return f'{int((length * width * Road.density * Road.thickness))/1000} тонн'

a = Road()
print(a.weight(25, 1000))