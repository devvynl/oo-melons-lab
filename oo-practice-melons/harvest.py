############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code 
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name 

        self.pairings = []
        print(f'I am {self.name}')

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairing = pairing 
        pairings.append(pairing)
        print(f'Pairing list is now {self.pairings}')

        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        code = super().update_code()
        self.code = new_code
        print(f'The code is now {self.code}')
        # Fill in the rest

# melon1 = MelonType('yw', 'Field 2', 7, None, None, 'Melon 1')

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType(
        "musk",
        "Muskmelon",
        1998,
        "green",
        True,
        True)
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    


    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



