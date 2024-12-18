def print_10_stars():
    for _ in range(10):
        print("*", end='')
    

def repeat():
    for _ in range(5):
        print_10_stars()
        print()

repeat()