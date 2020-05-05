"""Print out all the melons in our inventory."""


from melons import melon_catalogue


def print_melon(melon_name):
    """Print each melon with corresponding attribute information."""
    try:
        melon_name = melon_name.capitalize()
        print(melon_name.upper())

        for key in melon_catalogue[melon_name].keys():
            print(f"    {key}: {melon_catalogue[melon_name][key]}")
    except:
        print('OOPS! That melon is not in the catalogue.')

