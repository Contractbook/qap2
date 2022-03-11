class Buffer:
    data = []

    @classmethod
    def load(cls, data):
        cls.data.extend(data)

    @classmethod
    def clear(cls):
        cls.data = []
