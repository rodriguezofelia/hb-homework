"""Print out all the melons in our inventory."""


from melons import melons

def print_all_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon, characteristics in melons.items():
        print(melon.upper())

        for characteristic, value in characteristics.items():
            print(f"{characteristic}: {value}")

        print("------------------")

print_all_melons(melons)
