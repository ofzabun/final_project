import pynini
from pynini.lib import rewrite
from pynini.lib import pynutil
from pynini.export import export

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

consonants = (
    pynini.union(
        "b",
        "c",
        "ç",
        "d",
        "f",
        "g",
        "ğ",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "r",
        "s",
        "ş",
        "t",
        "u",
        "v",
        "y",
        "z"
    )
    .closure()
    .optimize()
)

vowels = (
    pynini.union(
        "a",
        "e",
        "ı",
        "i",
        "o",
        "ö",
        "u",
        "ü"
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

first_plural_suffix = (
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
    .optimize()
)

first_singular_suffix = (
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
    .optimize()
)

second_plural_suffix = (
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
    .optimize()
)

second_singular_suffix = (
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
    .optimize()
)

third_plural_suffix = (
    pynini.cdrewrite(
        pynutil.insert('ları'),
        pynini.union("a", "ı", "o", "u") + consonants,
        "[EOS]",
        SIGMA_STAR
    )
    @ pynini.cdrewrite(
        pynutil.insert('leri'),
        pynini.union("e", "i", "ö", "ü") + consonants,
        "[EOS]",
        SIGMA_STAR
    )
    .optimize()
)


third_singular_suffix = (
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
    .optimize()
)









if __name__ == "__main__":
    with pynini.Far("rules.far", "w") as far:
        far["first_plural_suffix"] = first_plural_suffix
        far["first_singular_suffix"] = first_singular_suffix
        far["second_plural_suffix"] = second_plural_suffix
        far["second_singular_suffix"] = second_singular_suffix
        far["third_plural_suffix"] = third_plural_suffix
        far["third_singular_suffix"] = third_singular_suffix
        
        
        

