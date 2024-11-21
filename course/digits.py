vals = ("038", "੦੩੮", "０３８",
        "⁰³⁸", "⒊⒏", "⓪③⑧",
        "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參",
        "38.0", "-38"
        )

for s in vals:
    print(s, s.isnumeric(), s.isdigit(), s.isdecimal())