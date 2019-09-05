from random import choice,random, uniform

class String :
    def __init__(self, sequence=''):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        if sequence:
            self.sequence = sequence
        else:
            self.sequence = sequence
            
            # letters = 'abcdefghij'
            # print(len(letters))
            # print(10)
            for i in range(26):
                self.sequence += choice(self.letters)
        self.fitness = 0
        # print(self.sequence)
    


    

    def crossover(self, partner):
        new_sequence = ''
        midpoint = random()*(len(self.sequence)-1)
        # print('midpoint = ' + str(midpoint))
        # print('self = ' + self.sequence)
        # print('partner = ' + partner.sequence)

        for i in range(len(self.sequence)):
            if i < midpoint:
                new_sequence += self.sequence[i]
            else:
                new_sequence += partner.getSequence()[i]
        # print(new_sequence)
        return String(new_sequence)

    def mutation(self):
        list_sequence = list(self.sequence)
        for i in range(len(list_sequence)):
            if uniform(0, 1) < 0.01:
                list_sequence[i] = choice(self.letters)
        self.sequence = ''.join(list_sequence)


    def getSequence(self):
        return self.sequence
    
    def setFitness(self, fitness):
        self.fitness = fitness
    
    def getFitness(self):
        return self.fitness