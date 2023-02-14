def say_something(number, word):
    word = word.capitalize()
    return word * number

number = int(input('Введите число '))
word = input("Введите слово ")

print(say_something(number, word))

def say_something(number: int, word: str) -> str:
    word = word.capitalize()
    return word * number