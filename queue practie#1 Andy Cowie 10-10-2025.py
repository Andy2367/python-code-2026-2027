'''
queues
10-10-2025
Andy Cowie
'''

queue = []
max_e = 5
elements = 0

if elements == max_e:
    print ("queue is full, can't add any more at this time")
else:
    while elements < max_e:
        queue.append(input("pleas input the thing you would like to add to the que or stop to exit: "))
        elements = (elements + 1)
        if elements >= max_e:
            print ("sorry queue is full pleas dequeue to add more items")
        elif input.lower == stop:
            print ("the elements in the queue are ",queue)
            