import time


class TrafficLight:
    """Имитация светофора: из словаря приватного атрибута метод формирует цвет и длительность отображения в stdout"""
    __color = {'red': 4, 'yellow': 2, 'green': 3}

    def running(self):
        for color, sec in self.__color.items():
            while sec:
                print(f'{color} {sec}')
                time.sleep(1)
                sec -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
