class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        return f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"'


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)
        print(self.draw())


class Pencil(Stationery):

    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки\n{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')


class Handle(Stationery):

    def __init__(self, title: str):
        super().__init__(title)
        print(self.draw())


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """
