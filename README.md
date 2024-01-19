# CSI4180_Homework0
 Homework 0 for CSI 4180

**Files:**

 output.txt: word frequency list is written to this file after the program has been run


 ebookOne.txt: This file can be used to run the program (_The Great Gatsby_)
 
 ebookTwo.txt: This file can also be used to run the program (_The Adventures of Sherlock Holmes_)
 
 homework0.py: This file contains all of my code. Instructions to run it can be found below

 

 **Instructions for running homework0.py:**
 
  In order to run this file through the command line, a text file is required.
  
  Example Command:
  
  python3 homework0.py ebookOne.txt --lower --removePunct --lemma --removeStopWords
  

  --lower: lowecases all text in the file provided. In the example above, all text in ebookOne.txt is lowercased
  
  --removePunct: removes all punctuation excluding punctuation for contractions. In the example above, punctuation is removed from ebookOne.txt
  
  --lemma: lemmatizes all words in the file provided. In the example above, all text in ebookOne.txt is lemmatized
  
  --removeStopWords: removes all stop words from the file provided. In the example above, all stop words are removed from ebookOne.txt

  Note: The four command line arguments above are optional. You can include any number of them in any order as long as they always come after the text file in your command
  
  Note: ebookOne.txt could be replaced with ebookTwo.txt in your command

 **Credit to AI:**
 
  I utilized https://copilot.microsoft.com to assist me with writing portions of my code. In homework0.py, there are comments that specify exactly which lines were written  with the help of AI. I only used this tool to help me with removing punctuation, counting the words and writing them to output.txt, and for creating the graph.
