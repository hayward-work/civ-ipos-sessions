class TheWall:
    def __init__(self, number_of_bottles: int =100):
        self.number_of_bottles = tuple(range(number_of_bottles).__reversed__())
    def pass_around(self):
        for bottle in self.number_of_bottles:
            print(f"{bottle} bottles of beer on the wall.")
            print(f"{bottle} bottles of beer.")
            print("Take one down, pass around.")
            if bottle != 0:
                print(f"{(bottle-1)} bottles of beer on the wall.")
                continue
            print("No more bottles of beer on the wall.")

new_wall = TheWall(number_of_bottles=100)
new_wall.pass_around()

# Could have done something with string slicing or something fancy or put instantiate in a separate file,
# but I presume you just need an idea of our baseline ability so this is good enough