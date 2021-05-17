import pynini
from pynini.lib import rewrite
from pynini.lib import pynutil
import argparse

def main(args: argparse.Namespace) -> None:
    subject = args.suffix_subject
    text = str(args.word)

    SIGMA_STAR = (
        pynini.union(
            "a",
            "b",
            "c",
            "ç",
            "d",
            "e",
            "f",
            "g",
            "ğ",
            "h",
            "ı",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "ö",
            "p",
            "r",
            "s",
            "ş",
            "t",
            "u",
            "ü",
            "v",
            "y",
            "z"
        )
        .closure()
        .optimize()
    )

    consonants_except_pçtk = (
        pynini.union(
            "b",
            "c",
            "d",
            "f",
            "g",
            "ğ",
            "h",
            "j",
            "l",
            "m",
            "n",
            "r",
            "s",
            "ş",
            "u",
            "v",
            "y",
            "z"
        )
        .closure()
        .optimize()
    )

    vowel_deletion = (
        pynini.union(
            "akıl",
            "şehir",
            "nehir",
            "beyin",
            "göğüs",
            "boyun",
            "burun",
            "devir",
            "zehir",
            "kayıp",
            "hapis",
            "şükür",
            "zulüm",
            "ağız",
            "koyun",
            "alın",
            "oğul",
            "gönül",
            "ömür",
            "hüküm",
            "fikir",
            "cisim",   
        )
        .closure()
        .optimize()
    )


    if subject == "first_singular":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ım'),
                pynini.union("a", "ı") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('im'),
                pynini.union("e", "i") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('um'),
                pynini.union("o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('üm'),
                pynini.union("ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bım"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cım"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dım"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğım"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bim"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cim"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dim"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğim"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bum"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cum"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dum"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğum"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "büm"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cüm"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "düm"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğüm"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
        )

    elif subject == "second_singular":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ın'),
                pynini.union("a", "ı") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('in'),
                pynini.union("e", "i") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('un'),
                pynini.union("o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('ün'),
                pynini.union("ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bın"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cın"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dın"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğın"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bin"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cin"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "din"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğin"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bun"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cun"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dun"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğun"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bün"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cün"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dün"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğün"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
        )

    elif subject == "third_singular":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ı'),
                pynini.union("a", "ı") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('i'),
                pynini.union("e", "i") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('u'),
                pynini.union("o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('ü'),
                pynini.union("ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bı"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cı"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dı"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğı"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bi"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "ci"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "di"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ği"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bu"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cu"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "du"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğu"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bü"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cü"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dü"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğü"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
        )

    elif subject == "first_plural":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ımız'),
                pynini.union("a", "ı") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('imiz'),
                pynini.union("e", "i") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('umuz'),
                pynini.union("o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('ümüz'),
                pynini.union("ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bımız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cımız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dımız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğımız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bimiz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cimiz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dimiz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğimiz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bumuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cumuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dumuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğumuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bümüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cümüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dümüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğümüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
        )

    elif subject == "second_plural":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ınız'),
                pynini.union("a", "ı") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('iniz'),
                pynini.union("e", "i") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('unuz'),
                pynini.union("o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynutil.insert('ünüz'),
                pynini.union("ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bınız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cınız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dınız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğınız"), 
                pynini.union("a", "ı"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "biniz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "ciniz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "diniz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğiniz"), 
                pynini.union("e", "i"),
                "[EOS]",
                SIGMA_STAR
            )
            @
            pynini.cdrewrite(
                pynini.cross("p", "bunuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cunuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dunuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğunuz"), 
                pynini.union("o", "u"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("p", "bünüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("ç", "cünüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("t", "dünüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynini.cross("k", "ğünüz"), 
                pynini.union("ö", "ü"),
                "[EOS]",
                SIGMA_STAR
            )
        )

    elif subject == "third_plural":
        rule = (
            pynini.cdrewrite(
                pynutil.insert('ları'),
                pynini.union("a", "ı", "o", "u") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
            @ pynini.cdrewrite(
                pynutil.insert('leri'),
                pynini.union("e", "i", "ö", "ü") + consonants_except_pçtk,
                "[EOS]",
                SIGMA_STAR
            )
        )
   
    output = pynini.compose(text, rule)
    print(text)
    print(output.string())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "suffix_subject", help = "type one of the options: first_singular, second_singular, third_singular, first_plural, second_plural, third_plural"
    )
    parser.add_argument(
        "word", help = "type the word that you want to add the suffix to"
    )
    main(parser.parse_args())


