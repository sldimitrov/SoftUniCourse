
class NextIdMixin:
    id = -1

    @classmethod
    def next_id(cls):
        return cls.id

    @classmethod
    def increment_id(cls):
        cls.id += 1
