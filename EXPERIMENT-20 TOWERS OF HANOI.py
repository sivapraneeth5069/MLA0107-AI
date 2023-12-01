class Tower:
    def __init__(self, name):
        self.name = name
        self.disks = []
    def move_disk(self, disk):
        if not self.disks or disk > self.disks[-1]:
            self.disks.append(disk)
        else:
            print("Invalid move: Cannot place a larger disk on top of a smaller disk")
    def remove_disk(self):
        if self.disks:
            return self.disks.pop()
        else:
            print("Error: No disks to remove")
def solve_towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        destination.move_disk(1)
    else:
        solve_towers_of_hanoi(n - 1, source, destination, auxiliary)
        source.move_disk(n)
        solve_towers_of_hanoi(n - 1, auxiliary, source, destination)
source = Tower('A')
auxiliary = Tower('B')
destination = Tower('C')
for i in range(1, 4):
    source.move_disk(i)
solve_towers_of_hanoi(3, source, auxiliary, destination)
print("Source:", source.disks)
print("Auxiliary:", auxiliary.disks)
print("Destination:", destination.disks)
