import unittest
import pynini

with pynini.Far("rules.far", "r") as rules:
    class Suffix_Test1(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule1(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitabım")

    class Suffix_Test2(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule2(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitabın")

    class Suffix_Test3(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule3(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitabı")

    class Suffix_Test4(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule4(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitabımız")

    class Suffix_Test5(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule5(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitabınız")

    class Suffix_Test6(unittest.TestCase):
        def rewrites(self, istring: str, expected_ostring: str) -> None:
            ostring = rules.rule6(istring)
            self.assertEqual(ostring, expected_ostring)
        
        def test_kitap(self):
            self.rewrites("kitap", "kitapları")


if __name__ == "__main__":
    unittest.main()