class Building:
    def __init__(self, width, height, brick):
        self.width = width
        self.height = height
        self.brick = brick

    def at_height(self, height):
        if height < self.height:
            return self.brick * self.width
        else:
            return " " * self.width


class Park:
    def __init__(self, width, foliage):
        self.width = width
        self.foliage = foliage

    def at_height(self, height):
        if height == 0 or height == 1:
            return " " * (self.width // 2) + "|" + " " * (self.width // 2)
        elif height == 2:
            return " " * (self.width // 2 - 2) + self.foliage * 5 + " " * (self.width // 2 - 2)
        elif height == 3:
            return " " * (self.width // 2 - 1) + self.foliage * 3 + " " * (self.width // 2 - 1)
        elif height == 4:
            return " " * (self.width // 2) + self.foliage + " " * (self.width // 2)
        else:
            return " " * self.width


class EmptyLot:
    def __init__(self, width, trash):
        self.width = width
        self.trash = trash

    def at_height(self, height):
        if height == 0:
            return self.repeat_trash(self.width, self.trash)
        else:
            return " " * self.width

    def repeat_trash(self, width, trash):
        # Repeat the trash string to fill the width of the empty lot
        result = ""
        while len(result) < width:
            result += trash
        # Ensure the result fits within the specified width
        return result[:width]


def parse_input(input_str):
    elements = []
    parts = input_str.split()
    for part in parts:
        type_str, rest = part.split(":", 1)
        values = rest.split(",")
        if type_str == "b":
            elements.append(Building(int(values[0]), int(values[1]), values[2]))
        elif type_str == "p":
            elements.append(Park(int(values[0]), values[1]))
        elif type_str == "e":     
            elements.append(EmptyLot(int(values[0]), replace_underscore(values[1])))
    return elements

def replace_underscore(string):
    if string == '':
        return '' 
    else:
        if string[0] == '_':
            return ' ' + replace_underscore(string[1:])
        return string[0] + replace_underscore(string[1:])

def max_height(elements, index, current_max):
    if index == len(elements):
        return current_max
    else:
        element = elements[index]
        if type(element) == Building:
            new_max = max(current_max, element.height)
        elif type(element) == Park:
            new_max = max(current_max, 5)
        else:
            new_max = max(current_max, 1)
        return max_height(elements, index + 1, new_max)


def sum_widths(elements, index):
    if index == len(elements):
        return 0
    else:
        return elements[index].width + sum_widths(elements, index + 1)


def print_street_at_height(elements, height, output):
    if not elements:
        return output
    else:
        return print_street_at_height(elements[1:], height, output + elements[0].at_height(height))


def print_street_recursive(elements, height, current_height):
    if current_height > height:
        return
    else:
        print("|" + print_street_at_height(elements, height - current_height, "") + "|")
        print_street_recursive(elements, height, current_height + 1)


def main():
    input_str = input("Street: ")
    elements = parse_input(input_str)
    height = max_height(elements, 0, 0)
    width = sum_widths(elements, 0)

    print("+" + "-" * width + "+")
    print_street_recursive(elements, height, 0)
    print("+" + "-" * width + "+")


main()
