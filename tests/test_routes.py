import unittest
import restsrv.routes as routes  # import add_entity, sum_entity, update_entity


class RoutesTest(unittest.TestCase):

    def setUp(self):
        self.app = routes.app.test_client()
        self.app.testing = True

    def test_simple_root(self):
        result = self.app.get('/')
        self.assertEqual(result.data, 'Entity Service',
                         msg="Incorrect response from '/' endpoint")

    def test_add_entity(self):
        expected_response = '{"permutations": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}'
        result = self.app.post('/addEntity',
                           data='{"entityID": 1, "data": [1, 2, 3]}',
                           headers={'content-type': 'application/json'})

        self.assertEqual(result.data, expected_response,
                         msg="Incorrect response from '/addEntity' endpoint")

    def test_sum_entity(self):
        expected_response = '{"sum": 36}'

        r0 = self.app.post('/addEntity',
                           data='{"entityID": 1, "data": [1, 2, 3]}',
                           headers={'content-type': 'application/json'})

        result = self.app.get('/sumEntity/entityID/1')

        self.assertEqual(result.data, expected_response,
                         msg="Incorrect response from '/sumEntity/entityID/1' endpoint")

    def test_update_entity(self):
        expected_response = '{"results": [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]}'

        r0 = self.app.post('/addEntity',
                            data='{"entityID": 1, "data": [1, 2, 3]}',
                            headers={'content-type': 'application/json'})

        result = self.app.post('/updateEntity',
                           data='{"entityID": 1, "add": -1}',
                           headers={'content-type': 'application/json'})

        self.assertEqual(result.data, expected_response,
                         msg="Incorrect response from '/updateEntity' endpoint")
