rule all:
    input:
        "output/output"

rule countWords:
    input:
        "input/input"
    output:
        "output/output"
    run:
        count = {}
        with open(input[0], "r") as infile:
            text = infile.read().replace("\n", " ")
            words = text.split()
            outfile = open(output[0], "w")
            outfile.write(str(len(words)))
            outfile.close()
