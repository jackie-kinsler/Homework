"""Print out all the melons in our inventory."""


from melons import melon_catalogue


def print_melon(melon_catalogue):
    """Print each melon with corresponding attribute information."""

    for melon in melon_catalogue:
        print(melon.upper())
        for key in melon_catalogue[melon].keys():
            print(f"    {key}: {melon_catalogue[melon][key]}")

print_melon(melon_catalogue)