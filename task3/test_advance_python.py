from advance_python import *
import pytest


@pytest.mark.parametrize("inp_out", [(4000, False), (13, True)])
def test_check_fibonacci(inp_out):
    """
    check the fibinacci number true or false
    :return:
    """
    input = inp_out[0]
    out = inp_out[1]
    val = check_fibonacci(input)
    assert val is out


def test_add_iterables():
    """add 2 iterables a and b such that a is even and b is odd"""
    a = [1, 2, 3, 4]
    b = [3, 1, 5, 7]
    val = add_iterables(a, b)
    assert val is 14


def test_skip_vowels():
    """test skip the vowels in the string"""
    val = skip_vowels("sajna")
    assert val == "s j n"


def test_customize_relu():
    """test ReLU function for a 1D array"""
    val = customize_relu([1, 2, -1, 0, 1.1])
    assert val == [1, 2, 1.1]


def test_customize_sigmoid():
    """test sigmoid function for a 1D array"""
    val = customize_sigmoid([5, 6, 1, 0, 3, -5])
    assert val == [0.9933071490757153, 0.9975273768433653, 0.7310585786300049, 0.5, 0.9525741268224334,
                   0.0066928509242848554]


def test_ascii_to_char():
    """test handles small alpha chracter shifting by 5"""
    val = shift_char("sajna")
    assert val == "xfosf"


def test_find_swear_words():
    """test to find swear words"""
    paragraph = "But while I was sitting down, I saw something that drove me crazy. Somebody’d written “Fuck you” on " \
                "the wall. It drove me damn near crazy. I thought how Phoebe and all the other little kids would see " \
                "it, and how they’d wonder what the hell it meant, and then finally some dirty kid would tell " \
                "them—all cockeyed, naturally—what it meant, and how they’d all think about it and maybe even worry " \
                "about it for a couple of days. I kept wanting to kill whoever’d written it. I figured it was some " \
                "perverty bum that’d sneaked in the school late at night to take a leak or something and then wrote " \
                "it on the wall. I kept picturing myself catching him at it, and how I’d smash his head on the stone " \
                "steps till he was good and goddam dead and bloody. But I knew, too, I wouldn’t have the guts to do " \
                "it. I knew that. That made me even more depressed. "
    val = find_swear_words(paragraph)
    assert val == ['damn', 'hell', 'bum']


def test_add_even_numbers():
    """test ading only even number from list"""
    val = add_even_numbers([1, 2, 3, 4, 10])
    assert val is 16


def test_find_biggest_character():
    """test to find biggest character in word"""
    val = find_biggest_character("sajna")
    assert val is "s"


def test_add_3rd_element():
    """add every 3rd element from list"""
    val = add_3rd_element([0, 1, 2, 3, 4, 10])
    assert val is 3


def test_generate_vehicle_num():
    """
    random generating vehicle number test
    """
    val = generate_vehicle_num()
    number_plate = val[0]
    states = number_plate[0:2]
    two_digit = number_plate[2:4]
    two_char = number_plate[4:6]
    four_num = number_plate[6:10]
    assert states == "KA"
    assert two_digit.isdigit()
    assert two_char.isupper()
    assert four_num.isdigit()
    assert len(val) is 15


def test_generate_vehicle_num_using_partial():
    """
    partial function test
    """
    val = generate_vehicle_num_using_partial()
    number_plate = val[0]
    states = number_plate[0:2]
    two_digit = number_plate[2:4]
    two_char = number_plate[4:6]
    four_num = number_plate[6:10]
    assert states == "DL"
    assert two_digit.isdigit()
    assert two_char.isupper()
    assert four_num.isdigit()
    assert len(val) is 15
