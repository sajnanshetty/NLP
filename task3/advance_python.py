import functools
import operator
import string
import random
import math
from functools import partial
import urllib.request as urllib2


def check_fibonacci(num: int):
    """
    case1:
    Write a function using only list filter lambda that can tell whether a number
     is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till
    """
    is_perfect_square = lambda x: True if math.pow(int(math.sqrt(x)), 2) == x else False
    is_fib = lambda x: True if is_perfect_square(5 * x * x + 4) or is_perfect_square(5 * x * x - 4) else False
    return is_fib(num)


def add_iterables(l1: list, l2: list):
    """
    case 2.1:
    Using list comprehension (and zip/lambda/etc if required) write an expression that:
    add 2 iterables a and b such that a is even and b is odd
    """
    return sum([a + b for a, b in zip(l1, l2) if a % 2 == 0 and b % 2 != 0])


def skip_vowels(word: str):
    """
    case 2.2:
    Using list comprehension (and zip/lambda/etc if required) write an expression that:
    strips every vowel from a string provided (tsai>>t s)"""
    format_word = [ch for ch in word if ch.lower() not in ['a', 'e', 'i', 'o' 'u']]
    return ' '.join(format_word)


def customize_relu(l: list):
    """
    case 2.3:
    Using list comprehension (and zip/lambda/etc if required) write an expression that:
    acts like a ReLU function for a 1D array"""
    return [item for item in l if bool(item) and item > 0]


def customize_sigmoid(l: list):
    """
    case 2.4:
    Using list comprehension (and zip/lambda/etc if required) write an expression that:
    acts like a sigmoid function for a 1D array"""
    return [1 / (1 + math.exp(-i)) for i in l]


def ascii_to_char(x: str):
    """
    handles small alpha chracter shifting by 5
    """
    if x + 5 > 122:
        return chr(96 + ((x + 5) - 122))
    else:
        return chr(x + 5)


def shift_char(s: str):
    """
    case 2.5:
    Using list comprehension (and zip/lambda/etc if required) write an expression that:
    acts like a sigmoid function for a 1D array
    takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn"""
    return ''.join(list(map(ascii_to_char, [ord(ch) for ch in s])))


def find_swear_words(paragraph: str):
    """
    case 3:
    A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of
     the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
    """
    swear_word_url = "https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt"
    swear_word_container = list(
        map(lambda word: word.decode('utf-8').rstrip('\n'), urllib2.urlopen(swear_word_url).readlines()))
    return [word for word in paragraph.split() if word in swear_word_container]


def add_even_numbers(l: list):
    """
    case 4.1:
    using reduce function:
    add only even numbers in a list
    """
    return functools.reduce(operator.add, filter(lambda x: x % 2 == 0, l))


def find_biggest_character(s: str):
    """
    case 4.2:
    using reduce function:
     find the biggest character in a string (printable ascii characters)
    """
    return functools.reduce(lambda a, b: a if ord(a) > ord(b) else b, s)


def add_3rd_element(l: list):
    """
    case 4.3:
    using reduce function:
    adds every 3rd number in a list
    """
    return functools.reduce(operator.add, l[::3])


def generate_vehicle_num(state: str = "KA"):
    """
    case 5:
    Using randint, random.choice and list comprehensions,
    write an expression that generates 15 random KADDAADDDD number plates,
    : where KA is fixed,
    :  D stands for a digit,
    : A stands for Capital alphabets. 10<<DD<<99
    :  & 1000<<DDDD<<9999
    """
    return [
        f"{state}{random.randint(10, 100)}{''.join(random.choices(string.ascii_uppercase, k=2))}{random.randint(1000, 10000)}"
        for i in range(15)]


def generate_vehicle_num_using_partial():
    """
    case 6:
    Write the above again from scratch where KA can be changed to DL,
    and 1000/9999 ranges can be provided.
    Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided
    """
    partial_fuc = partial(generate_vehicle_num, "DL")
    return partial_fuc()


if __name__ == "__main__":
    # print(add_even_numbers([1, 2, 3, 4, 10]))
    # print(add_3rd_element([0, 1, 2, 3, 4, 10]))
    # print(find_biggest_character("sajna"))
    # print(add_iterables([1, 2, 3, 4], [3, 1, 5, 7]))
    # print(skip_vowels('sajna'))
    # print(customize_relu([1, 2, -1, 0, None]))
    # print(shift_char("sajna"))
    # print(generate_vehicle_num())
    # print(customize_sigmoid([5,6,1,0,3, -5]))
    # print(generate_vehicle_num_using_partial())
    # print(check_fibonacci(13))
    # print(find_swear_words("ballsack bi+ch sajna"))
    pass
