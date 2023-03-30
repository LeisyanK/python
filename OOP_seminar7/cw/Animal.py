class Animal():
    def __init__(self, nickname):
        self._nickname = nickname

    @property
    def nickname(self):         # геттер для nickname
        return self._nickname

    @nickname.setter
    def nickname(self, new_nickname):
        self._nickname = new_nickname

