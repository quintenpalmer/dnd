import unittest
import util


class EvenTest(unittest.TestCase):
    def test_is_even(self):
        self.assertEqual(util.is_even(0), True)
        self.assertEqual(util.is_even(1), False)
        self.assertEqual(util.is_even(2), True)
        self.assertEqual(util.is_even(3), False)
        self.assertEqual(util.is_even(100), True)
        self.assertEqual(util.is_even(101), False)


class RoundedDownTest(unittest.TestCase):
    def test_rounded_down_even(self):
        self.assertEqual(util.rounded_lower_even(0), 0)
        self.assertEqual(util.rounded_lower_even(1), 0)
        self.assertEqual(util.rounded_lower_even(2), 2)
        self.assertEqual(util.rounded_lower_even(3), 2)
        self.assertEqual(util.rounded_lower_even(100), 100)
        self.assertEqual(util.rounded_lower_even(101), 100)


class GetHalfLevelTest(unittest.TestCase):
    def test_get_half_level(self):
        self.assertEqual(util.get_half_level(1), 0)
        self.assertEqual(util.get_half_level(2), 1)
        self.assertEqual(util.get_half_level(3), 1)
        self.assertEqual(util.get_half_level(4), 2)
        self.assertEqual(util.get_half_level(5), 2)
        self.assertEqual(util.get_half_level(6), 3)
        self.assertEqual(util.get_half_level(7), 3)
        self.assertEqual(util.get_half_level(8), 4)
        self.assertEqual(util.get_half_level(9), 4)


class GetAbilModTest(unittest.TestCase):
    def test_get_abil_mode(self):
        self.assertEqual(util.get_abil_mod(0), -5)
        self.assertEqual(util.get_abil_mod(1), -5)
        self.assertEqual(util.get_abil_mod(2), -4)
        self.assertEqual(util.get_abil_mod(3), -4)
        self.assertEqual(util.get_abil_mod(4), -3)
        self.assertEqual(util.get_abil_mod(5), -3)
        self.assertEqual(util.get_abil_mod(6), -2)
        self.assertEqual(util.get_abil_mod(7), -2)
        self.assertEqual(util.get_abil_mod(8), -1)
        self.assertEqual(util.get_abil_mod(9), -1)
        self.assertEqual(util.get_abil_mod(10), 0)
        self.assertEqual(util.get_abil_mod(11), 0)
        self.assertEqual(util.get_abil_mod(12), 1)
        self.assertEqual(util.get_abil_mod(13), 1)
        self.assertEqual(util.get_abil_mod(14), 2)
        self.assertEqual(util.get_abil_mod(15), 2)
        self.assertEqual(util.get_abil_mod(16), 3)
        self.assertEqual(util.get_abil_mod(17), 3)
        self.assertEqual(util.get_abil_mod(18), 4)
        self.assertEqual(util.get_abil_mod(19), 4)
        self.assertEqual(util.get_abil_mod(20), 5)
        self.assertEqual(util.get_abil_mod(21), 5)
        self.assertEqual(util.get_abil_mod(22), 6)
        self.assertEqual(util.get_abil_mod(23), 6)
        self.assertEqual(util.get_abil_mod(24), 7)
        self.assertEqual(util.get_abil_mod(25), 7)
        self.assertEqual(util.get_abil_mod(26), 8)
        self.assertEqual(util.get_abil_mod(27), 8)
        self.assertEqual(util.get_abil_mod(28), 9)
        self.assertEqual(util.get_abil_mod(29), 9)
        self.assertEqual(util.get_abil_mod(30), 10)
        self.assertEqual(util.get_abil_mod(31), 10)
        self.assertEqual(util.get_abil_mod(32), 11)
        self.assertEqual(util.get_abil_mod(33), 11)
        self.assertEqual(util.get_abil_mod(34), 12)
        self.assertEqual(util.get_abil_mod(35), 12)

if __name__ == '__main__':
    unittest.main()
