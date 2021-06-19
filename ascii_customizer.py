# This script replaces the background of an ASCII image (consisting of "1"s as its
# background and "0"s as its foreground) with whitespace, uses 1s as foreground
# edges, and randomizing the inner foreground with "0"s and "1"s.

import random as rand

with open("imagetoascii.txt", "r") as f:
    txt = f.read()

output = []
text_list = list(txt)

# Replace background with whitespace
for i, el in enumerate(text_list):
    if el == "1":
        text_list[i] = " "

# Set foreground edges to "1" characters and fill the rest of the foreground with
# random "0" and "1" characters.
for i, el in enumerate(text_list):
    r_int_str = str(rand.randint(0,1))
    if i != 0:
        if el == "\n" or el == " ":
            output.append(el)
        else:
            if text_list[i - 1] != "0":
                output.append("1")
            elif i < (len(text_list) - 1):
                if text_list[i + 1] != "0":
                    output.append("1")
                else:
                    output.append(r_int_str)
            elif i == (len(text_list) - 1):
                output.append("1")
            else:
                output.append(r_int_str)
    else:
        output.append(" ")

with open("customized_ascii.txt", "w") as f:
    f.write("".join(output))
