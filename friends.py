"""
venna mani abhiram reddy
cs-120
project-7
This code reads a friendship network from a file,
 builds a linked list-based structure, 
 finds common friends between two given names, 
 and prints them in sorted order.
"""
from linked_list import *
def main():
    """
    Reads friendship data from a file, builds a network,
      and finds common friends between two names.
    parameters:Name of the input file containing 
    friendship pairs.
    First person's name. Second person's name.
    return: A sorted linked list of common 
    friends or an error message if names are unknown.
    """
    input_file_name = input('Input file: ')
    input_file = open(input_file_name, 'r')
    name_list = LinkedList()
    name_to_node = {}
    # Build the friendship network
    for line in input_file:
        parts = line.strip().split()
        if len(parts) == 2:
            name1 = parts[0]
            name2 = parts[1]
            person1_node = name_to_node.get(name1)
            if not person1_node:
                name_list.append(name1)
                person1_node = name_list.find(name1)
                name_to_node[name1] = person1_node
            person2_node = name_to_node.get(name2)
            if not person2_node:
                name_list.append(name2)
                person2_node = name_list.find(name2)
                name_to_node[name2] = person2_node
            add_friend(person1_node, name2)
            add_friend(person2_node, name1)
    input_file.close()
    # Get the two names to compare
    name1 = input('Name 1: ').strip()
    name2 = input('Name 2: ').strip()
    person1_node = name_to_node.get(name1)
    if not person1_node:
        print("ERROR: Unknown person " + name1)
        return
    person2_node = name_to_node.get(name2)
    if not person2_node:
        print("ERROR: Unknown person " + name2)
        return
    # Find and print common friends
    common_friends = find_common_friends(person1_node, person2_node)
    if common_friends.length() > 0:
        print("Friends in common:")
        sorted_friends = sort_friends(common_friends)
        current = sorted_friends.head
        while current:
            print(current.data)
            current = current.next
def add_friend(node, friend_name):
    """
    Adds a friend to a node's friend list if not already present.
    :parameters: The node representing the person. Name of the friend to add.
    """
    # Add friend to node's friend list if not already present
    current = node.friends.head
    while current:
        if current.data == friend_name:
            return
        current = current.next
    node.friends.append(friend_name)
def find_common_friends(node1, node2):
    """
    Finds common friends between two nodes.
    :parametrs: First person's node. Second person's node.
    :return: A linked list of common friends.
    """
    # Create a new linked list of common friends
    common = LinkedList()
    current1 = node1.friends.head
    while current1:
        current2 = node2.friends.head
        while current2:
            if current1.data == current2.data:
                common.append(current1.data)
            current2 = current2.next
        current1 = current1.next
    return common
def sort_friends(friends_list):
    """
    Sorts a linked list of friends using bubble sort.
    :parameters : The linked list of friends.
    :return: A sorted linked list.
    """
    # Simple bubble sort on linked list
    if not friends_list.head or not friends_list.head.next:
        return friends_list
    sorted_list = LinkedList()
    current = friends_list.head
    while current:
        sorted_list.append(current.data)
        current = current.next
    changed = True
    while changed:
        changed = False
        current = sorted_list.head
        while current and current.next:
            if current.data > current.next.data:
                temp = current.data
                current.data = current.next.data
                current.next.data = temp
                changed = True
            current = current.next
    return sorted_list
if __name__ == "__main__":
    main()