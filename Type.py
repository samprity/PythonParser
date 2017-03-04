class Activity:
    def add_element(self, element):
        self.component.append(element)

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.component = []


class Element:
    def set_callback(self, callback):
        self.callback = callback

    def __init__(self, name, id):
        self.id = id
        self.name = name
        self.callback = None
