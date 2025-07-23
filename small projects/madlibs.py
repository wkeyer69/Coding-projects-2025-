with open("text.txt", "r") as file:
    story = file.read()
    
words = []
target = -1

start_of_word = "<"
end_of_word = ">"

for i, char in enumerate(story):
    if char == start_of_word:
        target = i

    if char == end_of_word and target != -1:
        word = story[target: i + 1]
        words.append(word) 
        target = -1

anwsers = {}

for word in words: 
    anwser = input(f" enter a word: {word}")
    anwsers[word] = anwser 

for word in words: 
    story = story.replace(word, anwsers[word])





