print("Hello, I'm a Reverse word Order")
Sentence = input("Please enter a sentence: ")

Words_list = Sentence.split()
Words_list.reverse()
x = ' '.join(Words_list)

print(x)
