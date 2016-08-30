import unittest
from restsrv.models.entities import Entity


class EntityTest(unittest.TestCase):

    def setUp(self):
        entity_id = 1
        data = [1, 2, 3]
        self.t_entity = Entity(entity_id, data)

    def test_get_permutations(self):
        expected_permutation = [(1, 2, 3), (1, 3, 2), (2, 1, 3),
                                (2, 3, 1), (3, 1, 2), (3, 2, 1)]
        self.assertListEqual(sorted(self.t_entity.get_permutations()),
                             sorted(expected_permutation),
                             msg="Entity permutations are not correct")

    def test_sum(self):
        expected_sum = 36
        self.assertEqual(self.t_entity.sum(), expected_sum,
                         msg="Sum of the entity permutation \
                              elements is not correct")

    def test_add(self):
        modified_elements = [0, 1, 2]
        self.t_entity.add(-1)
        self.assertListEqual(self.t_entity.data,
                             modified_elements,
                             msg="Modified entity is not correct")
