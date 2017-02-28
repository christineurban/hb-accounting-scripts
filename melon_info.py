"""
Prints out all the melons in our inventory
"""

from melons import melons


def print_melons(melon_data):
    for melon, attributes in melon_data.items():
        print melon.upper()
        for attribute, value in attributes.items():
            print "    {}: {}".format(attribute, value)
        
print_melons(melons)