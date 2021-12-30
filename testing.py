import spacy
import en_core_web_sm

# initializing the nlp library used to tokenize the words
nlp = en_core_web_sm.load()

# list the "numbers" in the question to be determined
numbers = []

# places words in a sentence
sentence = ""

# index for starting to split sentences
start_index = 0

# places sentence in an array of sentences to correlate with the numbers that the sentence contains
sentences = []

# opening data file originally and checking whether the line of data includes a verb
with open("data2.txt", "r") as data_file:
    # takes the whole text as "lines"
    for lines in data_file:
        doc = nlp(lines)
        for token in doc:
            if token.pos_ == "VERB":
                # creates a sentence from the text using numbers ex: lines[0:10]
                sentence = lines[start_index:lines.index(token.text)]
                sentences.append(sentence)
                # replaces the start_index so there is a new set of words
                start_index = lines.index(token.text)
                # empties the sentence to be appended again
                sentence = ""
        # splits the lines data to capture which are numbers
        data = lines.split()

# checks whether the word is a digit and appends to the numbers array
for word in data:
    if word[0].isdigit() == True:
        numbers.append(word)

# iterates through the numbers and sentences to check whether the number is in the sentence and if true, prompts the user the number and associated sentence
for num in numbers:
    for sentence in sentences:
        if num in sentence:
            print("What does " + "'" + num + "'" +
                  " mean in this part of the question?: " + sentence + "\n")
            # breaking out of second for-loop to ensure the num is not searched in other sentences (just once)
            break
