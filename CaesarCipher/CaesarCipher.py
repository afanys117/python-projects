import art


def caesar(startText, shiftAmount, directionAlgorithm):
    outputText = ""
    if directionAlgorithm == "encode":
        outputText = ""
        for char in startText:
            if char in alphabet:
                index = alphabet.index(char)
                outputText += alphabet[(index + shiftAmount) % 26]
            else:
                outputText += char
        print(outputText)
    elif directionAlgorithm == "decode":
        outputText = ""
        for char in startText:
            if char in alphabet:
                index = alphabet.index(char)
                outputText += alphabet[(index - shiftAmount + 26) % 26]
            else:
                outputText += char
        print(outputText)
    else:
        print(f"Invalid input : {directionAlgorithm}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

choice = "yes"

print(art.logo)

while choice == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(startText=text, shiftAmount=shift, directionAlgorithm=direction)
    print("Do you want to continue")
    choice = input("enter yes to continue else no\n").lower()
