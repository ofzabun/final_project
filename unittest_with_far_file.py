import unittest
import pynini

class Suffix_Test(unittest.TestCase):
     
    def test_first_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule1 = suffix_rules["rule1"]
        output = pynini.compose("kitap", rule1)
        output2 = output.string()
        self.assertEqual(output2, "kitabım")
    
    def test_second_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule2 = suffix_rules["rule2"]
        output = pynini.compose("kitap", rule2)
        output2 = output.string()
        self.assertEqual(output2, "kitabın")
    
    def test_third_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule3 = suffix_rules["rule3"]
        output = pynini.compose("kitap", rule3)
        output2 = output.string()
        self.assertEqual(output2, "kitabı")
    
    def test_first_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule4 = suffix_rules["rule4"]
        output = pynini.compose("kitap", rule4)
        output2 = output.string()
        self.assertEqual(output2, "kitabımız")

    def test_second_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule5 = suffix_rules["rule5"]
        output = pynini.compose("kitap", rule5)
        output2 = output.string()
        self.assertEqual(output2, "kitabınız")
    
    def test_third_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule6 = suffix_rules["rule6"]
        output = pynini.compose("kitap", rule6)
        output2 = output.string()
        self.assertEqual(output2, "kitapları")

    def test_first_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule1 = suffix_rules["rule1"]
        output = pynini.compose("gelir", rule1)
        output2 = output.string()
        self.assertEqual(output2, "gelirim")
    
    def test_second_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule2 = suffix_rules["rule2"]
        output = pynini.compose("gelir", rule2)
        output2 = output.string()
        self.assertEqual(output2, "gelirin")
    
    def test_third_singular(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule3 = suffix_rules["rule3"]
        output = pynini.compose("gelir", rule3)
        output2 = output.string()
        self.assertEqual(output2, "geliri")
    
    def test_first_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule4 = suffix_rules["rule4"]
        output = pynini.compose("gelir", rule4)
        output2 = output.string()
        self.assertEqual(output2, "gelirimiz")

    def test_second_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule5 = suffix_rules["rule5"]
        output = pynini.compose("gelir", rule5)
        output2 = output.string()
        self.assertEqual(output2, "geliriniz")
    
    def test_third_plural(self):
        suffix_rules = pynini.Far("/Users/ofz/Final Project/hw4-ofzabun-master/rules.far")
        rule6 = suffix_rules["rule6"]
        output = pynini.compose("gelir", rule6)
        output2 = output.string()
        self.assertEqual(output2, "gelirleri")

    


if __name__ == "__main__":
    unittest.main()