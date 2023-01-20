from prettytable import PrettyTable
import json
import logging
import time
import csv


"""Logger configuration"""
logging.basicConfig(filename='test_log.log', level='DEBUG',
                    format='%(asctime)s - %(levelname)s : %(message)s')  # filename='log.log'
logger = logging.getLogger()


def task_number():
    """Generator for decorator"""
    i = 1
    while i < 100:
        yield i
        i += 1


generator = task_number()
func_list = []


def start_style(func):
    """Decorator for each function, just to style output"""
    generator_2 = task_number()

    def tasks(*args, **kwargs):
        if func not in func_list:
            next_gen = next(generator)
            logger.info("==========- Task №" + str(next_gen) + " -==========")
        next_gen_2 = next(generator_2)
        logger.info("-------- Execution №" + str(next_gen_2) + " ---------")
        result = func(*args, **kwargs)
        func_list.append(func)
        return result

    return tasks


# Scalar types, Operators, and Control Flow. Introducing strings, Collections, and Iterators.

""" #1 Your task is to find the angle of the sun above the horizon knowing the time of the day.
    The sun rises in the East at 6:00 AM, which corresponds to an angle of 0 degrees.
    At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
    6:00 PM is the time of the sunset so the angle is 180 degrees. """


@start_style
def sun_angle(day_time):
    try:
        sun_rise = time.strptime('06:00', '%H:%M')
        sun_set = time.strptime('18:00', '%H:%M')
        current_time = time.strptime(day_time, '%H:%M')
        if sun_rise <= current_time <= sun_set:
            angle = (current_time.tm_hour - 6) * 15 + current_time.tm_min * 0.25
            logger.info(f'sun_angle({day_time}) == {angle}')
        else:
            logger.warning('"I don`t see the sun!"')
    except ValueError:
        logger.error('Enter time in right format: "HH:MM"')


sun_angle("18:00 AM")
sun_angle("18:00")
sun_angle("18:01")
sun_angle("06:00")
sun_angle("05:59")

""" #2 We have an array of straight connections between drones. 
Each connection is represented as a string with two names of friends separated by a hyphen. 
For example: "dr101-mr99" means that the dr101 and mr99 are friends. 
Implement a function that allows us to determine more complex connections between drones. 
You are given two names also. Try to determine if they are related through basic_api bonds by any depth. 
For example: if two drones have basic_api friends or friends who have basic_api friends and so on."""


@start_style
def check_connection(connection_array, first_drone_name, second_drone_name):
    dict_groups = {}
    set_number = 0

    def number_of_name_letters(iteration) -> int:
        """Returns the count of letters of the first drone in phrase with of them"""
        iteration_count = 0
        for k in iteration:
            if k == "-":
                return iteration_count
            iteration_count += 1

    for elem in connection_array:  # going over the elements in connection_array
        name_length = number_of_name_letters(elem)
        if elem[:name_length] in dict_groups:  # if name_1 not in the dict_groups -> add and set the group number
            dict_groups[elem[name_length + 1:]] = dict_groups[elem[:name_length]]
        elif elem[name_length + 1:] in dict_groups:  # if name_2 not in the dict_groups -> add and set the group number
            dict_groups[elem[:name_length]] = dict_groups[elem[name_length + 1:]]
        else:  # else -> add, with setting number in order
            dict_groups[elem[:name_length]] = set_number
            dict_groups[elem[name_length + 1:]] = set_number
            set_number += 1
    logger.info(dict_groups[first_drone_name] == dict_groups[second_drone_name])


check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "scout2", "scout3")
check_connection(
    ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
    "dr101", "sscout")

"""#3 Modularity
Create a script that prints csv text with a header and prints it as a table. 
Please use PrettyTable library to print it."""


@start_style
def print_csv(text_or_file, internal_delimiter=',', delimiter=None, quotechar=None):
    """
    :param internal_delimiter: which delimiter between numbers
    :param delimiter: delimiter inside the file, could be null
    :param quotechar: quotechar inside the file, could be null
    """
    x = PrettyTable()
    row_list = []

    def list_forming(reader):  # creates list with nesting "2"
        for row_ in reader:
            row_list.append(row_.split(internal_delimiter))
    if text_or_file.endswith("csv"):   # for file
        with open(text_or_file, newline='') as csv_file:
            read_csv = csv.reader(csv_file, delimiter=delimiter, quotechar=quotechar)
            for row_csv in read_csv:  # add each row to the list with splitting
                list_forming(row_csv)
    else:  # convert row into the list
        list_forming(text_or_file.split("\n"))
    for group in row_list: # table forming
        if row_list.index(group) == 0:  # first group in list - header
            x.field_names = group
        else:  # other elements added as rows
            x.add_row(group)
    logger.info(x)


print_csv("a,b\n1,2")
print_csv("resources/basic_text_3.csv",
          delimiter=',',
          quotechar='"')

"""#4 Build-in Collections
Find the length of the longest substring that consists of the same letter. 
For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". 
The last substring is the longest one which makes it an answer.
Input: String
Output: Int"""


@start_style
def long_repeat(text) -> int:
    letter_dict = {}
    for i in text:
        if i in letter_dict:
            letter_dict[i] += 1
        else:
            letter_dict[i] = 1
    logger.info(max(letter_dict.values()))
    return max(letter_dict.values())


long_repeat('sdsffffse')
long_repeat('ddvvrwwwrggg')

"""#5 Exceptions
Create a method parse_int that converts string positive number < 10 to an integer number. 
It should raise SpecialBlaException in case of the string doesn't contain a number. 
Otherwise, return this value (feel free to use 'int()')."""

dict_word_conversion = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


class SpecialBlaException(Exception):
    def __init__(self, msg='Invalid data', *args):
        super().__init__(msg, *args)


@start_style
def parse_int(text_number) -> int:
    if text_number in dict_word_conversion:
        logger.info(dict_word_conversion[text_number])
        return dict_word_conversion[text_number]
    else:
        logger.warning("Invalid data")
        raise SpecialBlaException


parse_int('one')
# parse_int('0')
# parse_int('red')

"""#6 Iteration and Iterables
Create your own implementation of range(n): returns generator that generates integers from 0 to n(n>0). 
(Please use yield operator )"""


@start_style
def my_range(number):
    i = 0
    while i != number:
        yield i
        i += 1


for j in my_range(3):
    logger.info(j)

"""#7 File IO and Resource Management
Current file contains text like this:
 \n\n\n{“a”:\n\n\n{”b”\n: 1}}
You need to read the file and make `b` value 2. 
To do this you need to read file as json(`import json; json.reads(...)`) and manipulate them as a dictionary"""


@start_style
def read_file(file_name, value_for_insert, file_type_json: bool = False, nested_param_1=None, nested_param_2=None):
    with open(file_name) as f:  # open the file
        row = ""
        for line in f:
            if file_type_json:  # depending on file type used different way of file reading
                row += line.strip()
            else:
                row += line.replace('\\n', '').replace('”', '\"').replace('“', '\"').strip()
    json_row = json.loads(row)
    if nested_param_1 is None:  # for updating json value nesting 1
        logger.info(json_row)
        logger.warning("Parameter is not filled, here nothing to change")
    else:
        if not nested_param_2:  # for updating json value nesting 2
            logger.info(f'Json before changing {json_row[nested_param_1]}')
            json_row[nested_param_1] = value_for_insert
            logger.info(f'Json after changing {json_row[nested_param_1]}')
        else:  # for json nesting 2
            logger.info(f'Json before changing {json_row[nested_param_1][nested_param_2]}')
            json_row[nested_param_1][nested_param_2] = value_for_insert
            logger.info(f'Json after changing {json_row[nested_param_1][nested_param_2]}')


read_file(file_type_json=False,
          file_name="resources/Basic_text",
          nested_param_1="a",
          nested_param_2="b",
          value_for_insert=2)
read_file(file_type_json=True,
          file_name="resources/Basic_text_2",
          nested_param_1="hub_gw_parameters",
          nested_param_2="hub_gw_region",
          value_for_insert=2)

"""#8 Classes
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O)
who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in horizontal, vertical,
 or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for the results of this game.
You are given a result of a game and you must determine if the game ends
in a win or a draw as well as who will be the winner.
Make sure to return "X" if the X-player wins and "O" if the O-player wins.
If the game is a draw, return "D". Implement this task using classes “Cell” with inherited “XCell” and “OCell”"""


class XCell:
    def x_win(self):
        logger.info("X")


class OCell:
    def o_win(self):
        logger.info("O")


class Cell(XCell, OCell):
    def draw(self, cell_value):
        if cell_value == "O":
            self.o_win()
        elif cell_value == "X":
            self.x_win()
        else:
            logger.info("D")


cell = Cell()


@start_style
def checkio(data):
    for i in data:
        if len(i) != 3:
            logger.error("Invalid data")
            raise KeyError('Invalid data')

    for i in data:
        if data[data.index(i)][0] == data[data.index(i)][1] == data[data.index(i)][2] != ".":
            cell.draw(data[data.index(i)][0])
            return
        elif data[0][data.index(i)] == data[1][data.index(i)] == data[2][data.index(i)] != ".":
            cell.draw(data[0][data.index(i)])
            return
    k = 0
    while k != -2:
        if data[0 + k][0] == data[1][1] == data[2][-1 - k] != ".":
            cell.draw(data[0 + k][0])
            return
        k -= 1
    cell.draw(".")


x = ["X.O",
     "XX.",
     "XOO"]
checkio(["X.O", "XX.", "XOO"])
checkio(["X.O", "XXX", "XOO"])
checkio(["X.O", "OXO", "OOX"])

checkio(["X.O", "XX.", "XOO"])
checkio(["OO.", "XOX", "XOX"])
checkio(["OOX", "XXO", "OXX"])
checkio(x)
