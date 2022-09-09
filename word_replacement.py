from dataclasses import replace


#birsuyilmaz
def replace_word():
    str_ = input("Please enter a string: ")
    word = input("Please enter a word you want to replace: ")
    replacement = input("Please enter a word you want to replace with: ")
    new_str = str_.replace(word, replacement)
    return new_str

print(replace_word())
#birsuyilmaz