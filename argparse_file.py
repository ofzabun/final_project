import pynini
from pynini.lib import rewrite
from pynini.lib import pynutil
import argparse

def main(args: argparse.Namespace) -> None:
    subject = args.suffix_subject
    text = str(args.word)

    with pynini.Far("rules.far", "r") as far:
        if subject == "first_singular":
            first_singular_suffix = far["first_singular_suffix"]
            output = pynini.compose(text, first_singular_suffix)
            print(text)
            print(output.string())

        elif subject == "second_singular":
            second_singular_suffix = far["second_singular_suffix"]
            output = pynini.compose(text, second_singular_suffix)
            print(text)
            print(output.string())

        elif subject == "third_singular":
            third_singular_suffix = far["third_singular_suffix"]
            output = pynini.compose(text, third_singular_suffix)
            print(text)
            print(output.string())

        elif subject == "first_plural":
            first_plural_suffix = far["first_plural_suffix"]
            output = pynini.compose(text, first_plural_suffix)
            print(text)
            print(output.string())

        elif subject == "second_plural":
            second_plural_suffix = far["second_plural_suffix"]
            output = pynini.compose(text, second_plural_suffix)
            print(text)
            print(output.string())

        elif subject == "third_plural":
            third_plural_suffix = far["third_plural_suffix"]
            output = pynini.compose(text, third_plural_suffix)
            print(text)
            print(output.string())
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "suffix_subject", 
        choices = ["first_singular",
        "second_singular",
        "third_singular", 
        "first_plural", 
        "second_plural", 
        "third_plural"], 
        help = "type one of the options"
    )
    parser.add_argument(
        "word", help = "type the word that you want to add the suffix to"
    )
    main(parser.parse_args())


