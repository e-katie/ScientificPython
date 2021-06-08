from os import listdir
inputs = [f for f in listdir('input')]

rule all:
    input:
        expand("output/{file}", file=inputs)

rule countLetters:
    input:
        "input/{file}"
    output:
        "output/{file}"
    run:
        count = {}
        with open(input[0], "r") as infile:
            string = infile.readline()
            for letter in string:
                if letter.isalpha():
                    letter = letter.lower()
                    if letter not in count: 
                        count[letter] = 0
                    count[letter] += 1
            outfileName = infile.name.replace("input", "output")
            outfile = open(outfileName, "w")
            sortedLetters = sorted(count.keys())
            for letter in sortedLetters:
                outfile.write("%s: %d\n" % (letter, count[letter]))
