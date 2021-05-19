import unittest
import pynini
from pynini.lib import rewrite 

class SuffixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far", "r")
    
    def test_first_singular(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", first_singular_suffix), "kitabım")

    def test_second_singular(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", second_singular_suffix), "kitabın")

    def test_third_singular(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", third_singular_suffix), "kitabı")
    
    def test_first_plural(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", first_plural_suffix), "kitabımız")

    def test_second_plural(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", second_plural_suffix), "kitabınız")
 
    def test_third_plural(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", third_plural_suffix), "kitapları")

    def test_first_singular(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", first_singular_suffix), "gelirim")
 
    def test_second_singular(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", second_singular_suffix), "gelirin")

    def test_third_singular(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", third_singular_suffix), "geliri")
 
    def test_first_plural(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", first_plural_suffix), "gelirimiz")

    def test_second_plural(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", second_plural_suffix), "geliriniz")
 
    def test_third_plural(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("gelir", third_plural_suffix), "gelirleri")


if __name__ == "__main__":
    unittest.main()