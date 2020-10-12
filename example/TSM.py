import unittest


class TSM(unittest.TestCase):

    def test_upper(auto):
        auto.assertEqual("abc".upper(), "ABC")

    def test_isupper(auto):
        auto.assertTrue("ABC".isupper())
        auto.assertFalse("Abc".isupper())

    def test_split(auto):
        s = "hello world"
        auto.assertEqual(s.split(), ["This", "Is", "Python"])
        # check that given condition and s.split
        # fails when the separator is not a string
        with auto.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
