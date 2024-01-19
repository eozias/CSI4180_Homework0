import argparse
import string
import matplotlib.pyplot as plt
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import stopwords
from collections import Counter


def homeworkZero():
    #Sets up command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'))
    parser.add_argument("--lower", action="store_true")
    parser.add_argument("--lemma", action="store_true")
    parser.add_argument("--removeStopWords", action="store_true")
    parser.add_argument("--removePunct", action= "store_true")
    args = parser.parse_args()

    #Reads the file and initiates preprocessing
    with args.file as file:
        content = file.read()
        tokens = word_tokenize(content)
        totalTokens = len(tokens)
        print("The total number of tokens in this txt file before preprocessing is: ")
        print(totalTokens)
        print()
        content = ' '.join(tokens)

        #Turns all text to lowercase if --lower was entered
        if args.lower:
            print("Converting to lowercase...")
            content = content.lower()

        #Removes Punctuation from the text if --removePunct was entered
        if args.removePunct:
            #Used https://copilot.microsoft.com to help with lines 40-44
            print("Removing punctuation...")
            tokenizer = RegexpTokenizer(r'\w+\'?\w+|\w+')
            words = tokenizer.tokenize(content)
            words_without_punctuation = [''.join(c for c in word if c not in string.punctuation or c in ["'", "’"]) for
                                         word in words]
            content = ' '.join(words_without_punctuation)

        #Lemmatizes all words if --lemma was entered
        if args.lemma:
            print("Lemmatizing the text...")
            lemmatizer = WordNetLemmatizer()
            tokens = word_tokenize(content)
            lemmaWords = [lemmatizer.lemmatize(token, pos = "v") for token in tokens]
            content = ' '.join(lemmaWords)

        #Removes all stop words regardless of character case if --removeStopWords was entered
        if args.removeStopWords:
            print("Removing stop words...")
            stop_words_lower = set(word.lower() for word in stopwords.words('english'))
            stop_words_upper = set(word.title() for word in stopwords.words('english'))
            stop_words = stop_words_lower.union(stop_words_upper)
            tokens = word_tokenize(content)
            tokensNoSWs = [tok for tok in tokens if tok not in stop_words]
            content = ' '.join(tokensNoSWs)

    #Used https://copilot.microsoft.com to help with lines 66-70
    #This code counts how many words are left after preprocessing. Then, prints the words
    word_counts = Counter(word_tokenize(content))
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    with open('output.txt', 'w') as f:
        for i, (word, count) in enumerate(sorted_word_counts, start=1):
            f.write(f'{i}: {word}: {count}\n')


    # Convert to the python set to get the unique tokens
    content = content.split()
    tokens = set(content)
    numTokens = len(tokens)
    print("\nThe number of unique tokens in this txt file are: ")
    print(numTokens)

    #Make the graph, utilized https://copilot.microsoft.com to help with the graph
    words = [word for word, count in sorted_word_counts]
    counts = [count for word, count in sorted_word_counts]
    plt.plot(np.arange(len(words)), counts)
    plt.xlabel("Words Represented by Numbers in the output.txt File")
    plt.ylabel("Word Frequency")
    plt.title("Logarithmic Distribution of Word Frequencies")
    plt.yscale('log')
    plt.show()

if __name__ == "__main__":
    homeworkZero()
