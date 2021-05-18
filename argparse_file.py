import pynini
from pynini.lib import rewrite
from pynini.lib import pynutil
import argparse


def main(args: argparse.Namespace) -> None:
    subject = args.suffix_subject
    text = str(args.word)
    with pynini.Far("rules.far", "r") as far:
        if subject == "first_singular":
            rule1 = far["rule1"]
            output = pynini.compose(text, rule1)
            print(text)
            print(output.string())
        elif subject == "second_singular":
            rule2 = far["rule2"]
            output = pynini.compose(text, rule2)
            print(text)
            print(output.string())
        elif subject == "third_singular":
            rule3 = far["rule3"]
            output = pynini.compose(text, rule3)
            print(text)
            print(output.string())
        elif subject == "first_plural":
            rule4 = far["rule4"]
            output = pynini.compose(text, rule4)
            print(text)
            print(output.string())
        elif subject == "second_plural":
            rule5 = far["rule5"]
            output = pynini.compose(text, rule5)
            print(text)
            print(output.string())
        elif subject == "third_plural":
            rule6 = far["rule6"]
            output = pynini.compose(text, rule6)
            print(text)
            print(output.string())
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "suffix_subject", choices = ["first_singular", "second_singular", "third_singular", "first_plural", "second_plural", "third_plural"], help = "type one of the options: first_singular, second_singular, third_singular, first_plural, second_plural, third_plural"
    )
    parser.add_argument(
        "word", help = "type the word that you want to add the suffix to"
    )
    main(parser.parse_args())


