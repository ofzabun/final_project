import unittest
import pynini
from pynini.lib import rewrite 

class SuffixTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.suffix_rules = pynini.Far("rules.far", "r")
    
    def test_first_singular_kitap(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", first_singular_suffix), "kitabım ")

    def test_second_singular_kitap(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", second_singular_suffix), "kitabın ")

    def test_third_singular_kitap(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", third_singular_suffix), "kitabı ")
    
    def test_first_plural_kitap(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", first_plural_suffix), "kitabımız ")

    def test_second_plural_kitap(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", second_plural_suffix), "kitabınız ")
 
    def test_third_plural_kitap(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("kitap", third_plural_suffix), "kitapları ")

    def test_first_singular_melek(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", first_singular_suffix), "meleğim ")
 
    def test_second_singular_melek(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", second_singular_suffix), "meleğin ")

    def test_third_singular_melek(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", third_singular_suffix), "meleği ")
 
    def test_first_plural_melek(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", first_plural_suffix), "meleğimiz ")

    def test_second_plural_melek(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", second_plural_suffix), "meleğiniz ")
 
    def test_third_plural_melek(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("melek", third_plural_suffix), "melekleri ")

    def test_first_singular_masa(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", first_singular_suffix), "masam ")
 
    def test_second_singular_masa(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", second_singular_suffix), "masan ")

    def test_third_singular_masa(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", third_singular_suffix), "masası ")
 
    def test_first_plural_masa(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", first_plural_suffix), "masamız ")

    def test_second_plural_masa(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", second_plural_suffix), "masanız ")
 
    def test_third_plural_masa(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("masa", third_plural_suffix), "masaları ")

    def test_first_singular_bere(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", first_singular_suffix), "berem ")
 
    def test_second_singular_bere(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", second_singular_suffix), "beren ")

    def test_third_singular_bere(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", third_singular_suffix), "beresi ")
 
    def test_first_plural_bere(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", first_plural_suffix), "beremiz ")

    def test_second_plural_bere(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", second_plural_suffix), "bereniz ")
 
    def test_third_plural_bere(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("bere", third_plural_suffix), "bereleri ")

    def test_first_singular_nüfus(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", first_singular_suffix), "nüfusum ")
 
    def test_second_singular_nüfus(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", second_singular_suffix), "nüfusun ")

    def test_third_singular_nüfus(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", third_singular_suffix), "nüfusu ")
 
    def test_first_plural_nüfus(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", first_plural_suffix), "nüfusumuz ")

    def test_second_plural_nüfus(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", second_plural_suffix), "nüfusunuz ")
 
    def test_third_plural_nüfus(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nüfus", third_plural_suffix), "nüfusları ")

    def test_first_singular_nefes(self):
        first_singular_suffix = self.suffix_rules["first_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", first_singular_suffix), "nefesim ")
 
    def test_second_singular_nefes(self):
        second_singular_suffix = self.suffix_rules["second_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", second_singular_suffix), "nefesin ")

    def test_third_singular_nefes(self):
        third_singular_suffix = self.suffix_rules["third_singular_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", third_singular_suffix), "nefesi ")
 
    def test_first_plural_nefes(self):
        first_plural_suffix = self.suffix_rules["first_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", first_plural_suffix), "nefesimiz ")

    def test_second_plural_nefes(self):
        second_plural_suffix = self.suffix_rules["second_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", second_plural_suffix), "nefesiniz ")
 
    def test_third_plural_nefes(self):
        third_plural_suffix = self.suffix_rules["third_plural_suffix"]
        self.assertEqual(rewrite.one_top_rewrite("nefes", third_plural_suffix), "nefesleri ")


if __name__ == "__main__":
    unittest.main()