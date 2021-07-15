from time import perf_counter

class TrafficLight:

    color = 'Красный'

    def running(self):
        print(TrafficLight.color)
        while perf_counter() <= 7:
            pass
        TrafficLight.color = 'Желтый'
        print(TrafficLight.color)
        while perf_counter() <= 9:
            pass
        TrafficLight.color = 'Зеленый'
        print(TrafficLight.color)


a = TrafficLight()
a.running()


