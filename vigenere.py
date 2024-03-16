import os
import random

class vigenere:
    def __init__(self, file_name_in, file_name_out):
        self.characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.sentences = []
        self.key = []
        self.vigenere_sentences = []

        self.sentences = self.FileRead(file_name_in)
        self.Menu()
        self.FileSave(file_name_out)

    def LetterMove(self, letter_1, letter_2, mode):
        letter_1, letter_2 = letter_1.lower(), letter_2.lower()
        index = self.characters.index(letter_1) + (mode * self.characters.index(letter_2))
        index = index % len(self.characters)
        letter_out = self.characters[index]
        return letter_out.upper()

    def Start(self, mode):
        index = 0
        vigenere_sentence_out = []
        for i in range(0, len(self.sentences)):
            vigenere_sentence = ''
            for j in range(0, len(self.sentences[i])):
                if self.sentences[i][j].lower() in self.characters:
                    vigenere_sentence += self.LetterMove(self.sentences[i][j], self.key[index % len(self.key)], mode)
                    index += 1
                else:
                    vigenere_sentence += self.sentences[i][j]
            vigenere_sentence_out.append(vigenere_sentence)
        return vigenere_sentence_out

    def FileSave(self, file_name_out):
        with open(file_name_out, 'w', encoding='utf-8') as f:
            for sentence in self.vigenere_sentences:
                f.write("%s\n" % sentence)

    def FileRead(self, file_name_in):
        file = []
        with open(file_name_in, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip() != "":
                    file.append(line.strip().upper())
        return file
    
    def SetKey(self):
        key = input("Insert the key (letters A-Z and numbers 0-10): ")
        return key.upper()

    def Menu(self):
        flaga = True
        self.cesar_sentences = []
        self.key = ''
        while flaga:
            mode = 0
            os.system('cls')
            print("--- Vigenere cipher ---")
            print("1. Encryption")
            print("2. Decryption") 
            print("3. Exit") 
            mode = int(input("Specify the operation of the programme (only number): "))
            match mode:
                case 1:
                    flaga = False
                    self.key = self.SetKey()
                    self.vigenere_sentences = self.Start(1)
                case 2:
                    flaga = False
                    self.key = self.SetKey()
                    self.vigenere_sentences = self.Start(-1)
                case 3:
                    os.system('cls')
                    flaga = False
                    print("Thank you for using my program!")
                case _:
                    flaga = True

        #print(self.sentences)
        #print(self.key)
        #print(self.vigenere_sentences)



def main():
    file1 = vigenere("input.txt", "output2.txt")
    file2 = vigenere("input.txt", "output5.txt")
    file3 = vigenere("input.txt", "output11.txt")

if __name__ == "__main__":
    main()