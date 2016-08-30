import itertools


class Entity:
    def __init__(self, entity_id, data):
        self.entity_id = entity_id
        self.data = data

    def get_permutations(self):
        return list(itertools.permutations(self.data))

    def sum(self):
        return sum([sum(x) for x in self.get_permutations()])

    def add(self, val):
        for i in range(len(self.data)):
            self.data[i] += val
