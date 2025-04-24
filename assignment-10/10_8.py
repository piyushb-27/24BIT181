'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Delete a/the/an from text file
with open("input.txt", "w") as f:
    f.write("This is a test of the text. An apple a day keeps the doctor away.")

with open("input.txt", "r") as f1, open("output.txt", "w") as f2:
    text = f1.read()
    for word in [" a ", " an ", " the "]:
        text = text.replace(word, " ")
    f2.write(text)
