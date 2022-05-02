import animal
import unittest


# test case
#  - Individual unit of testing
#  - Each unit = method/function

# test suite
#  - Collection of test cases, or test suites, or both

# test fixture
#  - Represent the preparatiion needed to perform one or more tests

# test runner
#  - Orchestrates the execution of tests and provides the outcome to the user

class TestAnimal(unittest.TestCase):
    def test_init(self):
        a1 = animal.Animal("Fred", 7)
        self.assertEqual(a1.name, "Fred")
        self.assertEqual(a1.age, 7)
        self.assertTrue(a1.isAlive)
        self.assertEqual(a1.type, "Generic")

    def test_sleep(self):
        a1 = animal.Animal("Fred", 7)
        c1 = animal.Cat("Stacy", 8)
        d1 = animal.Dog("Fido", 12)
        self.assertEqual(a1.sleep(), "*zzz*")
        self.assertEqual(c1.sleep(), "*purr*")
        self.assertEqual(d1.sleep(), "*snore*")

    def test_move(self):
        a1 = animal.Animal("Fred", "7")
        c1 = animal.Cat("Stacy", "8")
        d1 = animal.Dog("Fred", "2")
        self.assertEqual(a1.move(), " has moved.")
        self.assertEqual(c1.move(), " has walked.")
        self.assertEqual(d1.move(), " has run.")

    def test_eat(self):
        a1 = animal.Animal("Fred", 7)
        c1 = animal.Cat('Stacy', 8)
        d1 = animal.Dog("Fido", 12)
        self.assertEqual(a1.eat(), " Fred has gained energy.")
        self.assertEqual(c1.eat(), " Stacy has gained energy.")
        self.assertEqual(d1.eat(), " Fido has gained energy.")

if __name__ == '__main__':
    unittest.main()


'''
Common assert methods in unittest.TestCase:

assertEqual(a, b)
assertNotEqual(a, b)
assertTrue(a)
assertFalse(a)
assertIs(a, b)
assertIsNot(a, b)
assertIsNone(a)
assertIsNotNone(a)
assertIn(a, b)
assertNotIn(a, b)
assertIsInstance(a, b)
assertIsNotInstance

'''
    

