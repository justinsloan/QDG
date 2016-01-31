import quantumrandom

word_dict = {}
with open('./word_list.txt') as f:
    for line in f.readlines():
        index, word = line.strip().split('\t')
        word_dict[int(index)] = word

def generate_diceware_password(word_count=6):
    import random
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

def term(request=10, count=6):
    print(" _____________________________________")
    print("|QUANTUM DICEWARE".ljust(33) + " v0.2|")
    print("|-------------------------------------|")

    if quantum:
        print("|Quantum Mode....................[ ON]|")
    else:
        print("|Quantum Mode....................[OFF]|")

    if verbose:
        print("|Verbose Mode....................[ ON]|")
    else:
        print("|Verbose Mode....................[OFF]|")
        
    if write_to_file:
        print("|File Output.....................[ ON]|")
    else:
        print("|File Output.....................[OFF]|")
    print("|-------------------------------------|")
    show_requests = "| Generating " + str(request) + " passphrases"
    print(show_requests.ljust(38) + "|")
    show_count = "|   with " + str(count*12.9) + " bits of entropy"
    print(show_count.ljust(38) + "|")
    print("|-------------------------------------|")
    
    for num in range(0,request):
        print("| " + generate_diceware_password(count).ljust(35) + " |")
    print("|-------------------------------------|")

def main():
    global verbose
    verbose = False
    global quantum
    quantum = True
    global write_to_file
    write_to_file = False

    term()

if __name__ == '__main__':
    main()
