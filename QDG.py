import random
import quantumrandom
from graphics import *
from button import Button

word_dict = {}
with open('./word_list.txt') as f:
    for line in f.readlines():
        index, word = line.strip().split('\t')
        word_dict[int(index)] = word

class Passphrase:
    #TODO Copy passphrase to clipboard by clicking on the label

    def __init__(self, canvas, point, word_count=6):
        self.label = Text(point, "Generating Passphrase...")    #constructor statement that instantiates a text label object as 'label'
        self.label.setFill('blue')
        self.label.setStyle('bold')
        self.label.setSize(18)
        self.label.draw(canvas)
        self.generate()

    def generate(self):
        '''
        Calls the method to generate a Diceware passphrase and
        displays the result by changing the test of the label.
        '''
        self.label.setText("Generating Passphrase...")
        self.label.setText(self.__generate_passphrase(word_count=6))

    def __generate_passphrase(self, word_count=6):
        '''
        Generates a Diceware passphrase using either quantum or
        locally generated random data, depending on the settings.
        '''
        passphrase = []

        if quantum:
            if verbose:
                print("|Gathering quantum data...".ljust(38) + "|")
            data_count = word_count * 5
            quantum_data = quantumrandom.uint16(data_count)
            dice = (int("".join([str(y) for y in (quantum_data % 6) + 1])))
            roll = [str(dice)[i:i+5] for i in range(0, len(str(dice)), 5)]
            if verbose:
                print("|" + str(dice).ljust(37) + "|")
            for i in roll:
                passphrase.append(word_dict[int(i)])
        else:
            for words in range(0, word_count):
                this_index = 0
                for position in range(0, 5):
                    digit = random.randint(1, 6)
                    this_index += digit * pow(10, position)
                passphrase.append(word_dict[this_index])
                if verbose:
                    print(this_index)
        return ' '.join(passphrase)


def win():
    #TODO Allow user to specify and display any number of passphrase labels
    #TODO Allow user to save passphrase list to file
    #TODO Allow user to specify any number of passphrases outputed to file
    #TODO Create a button to enable/disable Quantum Mode

    myWin = GraphWin("QDG: Quantum Diceware Generator", 500, 100)   #constructor statement that instantiates the window object as 'myWin'
    row_lblStatus = Point(200,10)
    row_lblPhrase = Point(250,30)   #specifies a location on the window canvas for use by any object\

    phrase = Passphrase(myWin,row_lblPhrase)

    btnGenerate = Button(myWin, Point(100,70), 75, 20, "Generate")
    btnQuit = Button(myWin, Point(300,70), 75, 20, "Quit")

    btnQuit.activate()
    btnGenerate.activate()

    # Button Event Loop
    pt = myWin.getMouse()
    while not btnQuit.clicked(pt):
        if btnGenerate.clicked(pt):
            btnGenerate.deactivate()
            btnQuit.deactivate()

            phrase.generate()   #uses the generate() method of object: phrase from the class: Passphrase

            btnGenerate.activate()
            btnQuit.activate()
        pt = myWin.getMouse()

    myWin.close()
    sys.exit(0)


def main():
    global verbose
    verbose = False
    global quantum
    quantum = True

    win()


if __name__ == '__main__':
    main()
