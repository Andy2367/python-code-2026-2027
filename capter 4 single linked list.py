class tiketNode:
    def __init__(self, tiket_number):
        self.tiket_number = tiket_number
        self.next_person = None

class TiketCounter:
    def __init__(self):
        self.first_person = None # head of the line
    def take_tiket(self, number):
        print(number)
        new_node = tiketNode(number)
        if not self.first_person:
            self.first_person = new_node
            return
        last = self.first_person
        while last.next_person:
            last = last.next_person
        last.next_person = new_node
    def surve_next_custermer(self):
        if not self.first_person:
            print("No one in line")
            return
        print(f"Now surving ticket: {self.first_person.tiket_number}")

pharmecy_line = TiketCounter()

pharmecy_line.take_tiket(101) # node 1 created (head)
pharmecy_line.take_tiket(102) # node 2 created and linked to node 1
pharmecy_line.take_tiket(103) # node 3 created and linked to node 2 (tail)

pharmecy_line.surve_next_custermer