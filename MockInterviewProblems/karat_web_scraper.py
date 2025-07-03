""" 
You are working on a web scraper. You have received the contents of many websites in the form of a collection of (website, string) pairs.
In order to determine where to start investigating a topic, we would like to find the website with the most instances of a specific word.

Write a function that takes in a collection of strings, and a word, and returns the name of the website containing the most instances of the word.
If multiple websites contain the same number, return the first one in the input.

Example:
scraping = [
  ["hockeyplayers.com", "Hockey Player magazine's exclusive interview with famous goalie"],
  ["sports.com", "Hockey player shot the hockey puck into the hockey net, scoring a goal"],
  ["football.com", "World record breaking touchdown made by a new football player"],
  ["rugby.com", "Unique point scored as ball bounces off foot of player"]
]
finder(scraping, "Hockey") -> "sports.com"
finder(scraping, "player") -> "hockeyplayers.com"
finder(scraping, "foot")   -> "rugby.com"

The word does not count if it is part of another word, and is not case sensitive. For example if the word is "foot", it would not count if "football" is present.

Complexity analysis variables:
P = Number of pairs
S = Length of website content strings 
(note: Web URLs and the searched for string have constant length)

"""
scraping = [
    ["hockeyplayers.com", "Hockey Player magazine's exclusive interview with famous goalie"],
    ["sports.com", "Hockey player shot the hockey puck into the hockey net, scoring a goal"],
    ["football.com", "World record breaking touchdown made by a new football player"],
    ["rugby.com", "Unique point scored as ball bounces off foot of player"]
]


# Time: O(n*k), where n: number of sentences;  k: number of words in sentence
# Space: O(1), where amount of variables is constant

def finder(scraping, word):
    count = 0
    best_website = ""
    for website, text in scraping:
        #website = sentence[0]
        #text = sentence[1]
        #print(website)
        #print(text)
        cur_count = 0

        for w in text.split():
            w = w.strip(",.!();")
            if w.lower() == word.lower():
               cur_count+=1
        if cur_count > count:
            count = cur_count
            best_website = website
        
    return best_website
         
print(finder(scraping, "Hockey"))
# Now with a Counter 
# Time: O(n*k), where n: number of sentences;  k: number of words in sentence
# Space: O(n), since we have a dictionary

def finder(scraping, word):
    count = 0
    best_website = ""
    for website, text in scraping:
        cur_count = 0
        dic = {}
        for w in text.split():
            w = w.strip(",.!();")
            if w in dic:
                dic[w] +=1
            else:
                dic[w] = 1


        if word in dic and dic[word] > count:
            count = dic[word]
            best_website = website
    return best_website


# Now same but with a counter 
from collections import Counter

def finder(scraping, word):
    word = word.lower()
    count = 0
    best_website = ""

    for website, text in scraping:
        # Preprocess text: split into words, strip punctuation, lowercase
        words = [w.strip(",.!();").lower() for w in text.split()]

        # Use Counter to count all words
        word_counts = Counter(words)

        if word_counts[word] > count:
            count = word_counts[word]
            best_website = website

    return best_website

                
        