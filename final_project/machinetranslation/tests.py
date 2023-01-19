import unittest
from translator import englishtofrench, frenchtoenglish
class testengtofren(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench(null),null)
        self.assertEqual(englishtofrench('Hello'),'Bonjour')

class testfrentoeng(unittest.TestCase):
    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish(null), null)
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
