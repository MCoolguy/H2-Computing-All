def encoder(sentence):
    symbols = ["!", "?", ",", ".", " ", ";", '"', "'"]
    uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    newcode = ""
    mode = ""

    for index in range(0, len(sentence)):
        if sentence[index].isupper() == True:

            if mode == "punctuation":
                newcode += "0,"

            elif mode == "lower":
                newcode += "0,0,"

            newcode += str(uppercase.index(sentence[index]) + 1)
            mode = "upper"

            print(newcode)
        elif sentence[index].islower() == True:

            if mode == "upper":
                newcode += "0,"

            elif mode == "punctuation":
                newcode += "0,0,"

            newcode += str(lowercase.index(sentence[index]) + 1)
            mode = "lower"

            print(newcode)
        elif sentence[index].isalpha() == False:

            if mode == "lower":
                newcode += "0,"

            elif mode == "upper":
                newcode += "0,0,"

            newcode += str(symbols.index(sentence[index]) + 1)
            mode = "punctuation"

            print(newcode)
        newcode += ","

    return newcode[:-1]