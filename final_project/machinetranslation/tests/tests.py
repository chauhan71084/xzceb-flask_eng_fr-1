import unittest
from translator import englishtofrench, frenchtoenglish
class testengtofren(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench(''),'')
        self.assertEqual(englishtofrench('Hello'),'Bonjour')
        self.assertNotEqual(englishtofrench('Bye'),'Bonjour')

class testfrentoeng(unittest.TestCase):
    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish(''), '')
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchtoenglish('Hola'), 'Hello')

if __name__ == '__main__':
    unittest.main()
