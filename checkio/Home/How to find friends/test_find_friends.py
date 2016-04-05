import unittest

from find_friends import check_connection


class Tests(unittest.TestCase):
    TESTS = {
        "Basics": [
            {
                "input": (("dr101-mr99", "mr99-out00", "dr101-out00",
                           "scout1-scout2", "scout3-scout1", "scout1-scout4",
                           "scout4-sscout", "sscout-super"),
                          "scout2", "scout3"),
                "answer": True,
                "explanation": ["dr101", "mr99", "out00", "scout1", "scout2",
                                "scout3", "scout4", "sscout", "super"]
            },
            {
                "input": (("dr101-mr99", "mr99-out00", "dr101-out00",
                           "scout1-scout2", "scout3-scout1", "scout1-scout4",
                           "scout4-sscout", "sscout-super"),
                          "super", "scout2"),
                "answer": True,
                "explanation": ["dr101", "mr99", "out00", "scout1", "scout2",
                                "scout3", "scout4", "sscout", "super"]
            },
            {
                "input": (("dr101-mr99", "mr99-out00", "dr101-out00",
                           "scout1-scout2", "scout3-scout1", "scout1-scout4",
                           "scout4-sscout", "sscout-super"),
                          "dr101", "sscout"),
                "answer": False,
                "explanation": ["dr101", "mr99", "out00", "scout1", "scout2",
                                "scout3", "scout4", "sscout", "super"]
            },
        ],
        "Edge": [
            {
                "input": (['night-nikola'],
                          "nikola", "night"),
                "answer": True,
                "explanation": None
            },
            {
                "input": (['nic-batman', 'cat-super'],
                          "batman", "cat"),
                "answer": False,
                "explanation": ['batman', 'cat', 'super', 'nic']
            },
            {
                "input": (['scout1-scout3', 'plane1-robin', 'scout3-sscout',
                           'scout1-base', 'pingin-scout1', 'sscout-base',
                           'scout3-plane1', 'scout3-robin', 'plane1-nikola',
                           'plane1-pingin', 'base-scout3', 'plane1-sobhia',
                           'base-pingin', 'scout3-sobhia', 'robin-stevan',
                           'robin-base', 'nikola-robin', 'sobhia-sscout',
                           'stevan-sscout', 'robin-sobhia', 'robin-sscout',
                           'pingin-sscout', 'scout3-nikola', 'nikola-base',
                           'plane1-scout1', 'plane1-base', 'sscout-plane1',
                           'sobhia-scout1', 'sscout-scout1', 'robin-pingin',
                           'pingin-stevan', 'pingin-sobhia', 'scout3-pingin',
                           'nikola-sscout', 'nikola-pingin', 'stevan-base',
                           'stevan-scout1', 'scout1-nikola', 'nikola-sobhia',
                           'stevan-sobhia', 'stevan-scout3', 'scout1-robin',
                           'nikola-stevan', 'sobhia-base', 'stevan-plane1'],
                          "pingin", "sobhia"),
                "answer": True,
                "explanation": ['pingin', 'sobhia', 'sscout', 'scout3',
                                'stevan', 'scout1', 'plane1', 'nikola', 'base',
                                'robin']
            },
            {
                "input": (['sscout-batman', 'plane1-scout3', 'stevan-batman',
                           'super-sscout', 'scout2-batman', 'scout2-sscout',
                           'doc-mega', 'night-batman', 'scout3-doc'],
                          "scout2", "plane1"),
                "answer": False,
                "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega',
                                'sscout', 'super', 'scout3', 'doc', 'batman']
            },
            {
                "input": (['scout2-plane1', 'plane1-stevan', 'stevan-night',
                           'night-mega', 'mega-sscout', 'sscout-super',
                           'super-scout3', 'scout3-doc', 'doc-batman'],
                          "scout2", "batman"),
                "answer": True,
                "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega',
                                'sscout', 'super', 'scout3', 'doc', 'batman']
            },
            {
                "input": (['scout2-plane1', 'plane1-stevan', 'stevan-night',
                           'night-mega', 'sscout-super', 'super-scout3',
                           'scout3-doc', 'doc-batman'],
                          "night", "batman"),
                "answer": False,
                "explanation": ['scout2', 'plane1', 'stevan', 'night', 'mega',
                                'sscout', 'super', 'scout3', 'doc', 'batman']
            },
            {
                "input": (['scout1-scout3', 'plane1-robin', 'scout3-sscout',
                           'pingin-scout1', 'scout3-plane1', 'scout3-robin',
                           'plane1-nikola', 'plane1-pingin', 'plane1-sobhia',
                           'scout3-sobhia', 'nikola-robin', 'sobhia-sscout',
                           'robin-sobhia', 'robin-sscout', 'pingin-sscout',
                           'scout3-nikola', 'plane1-scout1', 'sscout-plane1',
                           'sobhia-scout1', 'sscout-scout1', 'robin-pingin',
                           'pingin-sobhia', 'scout3-pingin', 'nikola-sscout',
                           'nikola-pingin', 'stevan-base', 'scout1-nikola',
                           'nikola-sobhia', 'scout1-robin', ],
                          "base", "nikola"),
                "answer": False,
                "explanation": ['pingin', 'sobhia', 'sscout', 'scout3',
                                'stevan', 'scout1', 'plane1', 'nikola', 'base',
                                'robin']
            },
        ],
        "Extra": [
            {"input": (['mr99-cat', 'mega-mr99'],
                       "cat", "mr99"),
             "answer": True,
             "explanation": ['cat', 'mr99', 'mega']},
            {"input": (['cat-super', 'cat-nikola', 'nikola-super'],
                       "nikola", "super"),
             "answer": True,
             "explanation": ['nikola', 'super', 'cat']},
            {"input": (['nikola-robin', 'batman-nwing', 'mr99-batman',
                        'mr99-robin', 'dr101-out00', 'out00-nwing'],
                       "dr101", "mr99"),
             "answer": True,
             "explanation": ['dr101', 'mr99', 'out00', 'nikola', 'robin',
                             'batman', 'nwing']},
            {"input": (['cat-robin', 'cat-base', 'out00-scout4',
                        'robin-scout4', 'cat-batman', 'batman-plane2',
                        'plane2-scout3', 'plane2-base', 'robin-batman',
                        'mr99-scout3'],
                       "base", "robin"),
             "answer": True,
             "explanation": ['base', 'robin', 'mr99', 'scout3', 'plane2',
                             'batman', 'cat', 'scout4', 'out00']},
            {"input": (['out00-scout3', 'mega-scout3', 'mega-robin'],
                       "robin", "out00"),
             "answer": True,
             "explanation": ['scout3', 'out00', 'mega', 'robin']},
            {"input": (['base-night', 'scout1-night', 'pingin-sscout',
                        'sscout-scout1', 'dr101-pingin', 'sscout-base',
                        'dr101-sscout', 'pingin-night', 'pingin-scout1',
                        'scout1-dr101', 'dr101-night'],
                       "pingin", "base"),
             "answer": True,
             "explanation": ['pingin', 'base', 'night', 'dr101', 'sscout',
                             'scout1']},
            {"input": (['base-nikola', 'scout1-nikola', 'nikola-nwing'],
                       "nwing", "base"),
             "answer": True,
             "explanation": ['nwing', 'base', 'scout1', 'nikola']},
            {"input": (['base-stevan', 'out00-stevan', 'dr101-nwing'],
                       "nwing", "out00"),
             "answer": False,
             "explanation": ['nwing', 'out00', 'dr101', 'base', 'stevan']},
            {"input": (['sobhia-mega', 'nwing-nikola'],
                       "nwing", "mega"),
             "answer": False,
             "explanation": ['nwing', 'mega', 'nikola', 'sobhia']},
            {"input": (['pingin-out00', 'night-plane2', 'pingin-scout3'],
                       "plane2", "out00"),
             "answer": False,
             "explanation": ['plane2', 'out00', 'night', 'scout3', 'pingin']},
            {"input": (['out00-nwing', 'scout1-night', 'out00-sscout',
                        'scout4-night', 'nwing-sscout', 'plane1-scout1'],
                       "nwing", "night"),
             "answer": False,
             "explanation": ['nwing', 'night', 'plane1', 'scout1', 'sscout',
                             'out00', 'scout4']},
        ]
    }

    def test_Basics(self):
        for i in self.TESTS['Basics']:
            assert check_connection(*i['input']) == i['answer'], i['input']

    def test_Edge(self):
        for i in self.TESTS['Edge']:
            assert check_connection(*i['input']) == i['answer'], i['input']

    def test_Extra(self):
        for i in self.TESTS['Extra']:
            assert check_connection(*i['input']) == i['answer'], i['input']


if __name__ == "__main__":  # pragma: no cover
    unittest.main()