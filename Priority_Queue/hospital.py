# create a node that store information of patient
class Node:
    def __init__(self, pid, pname, priority):
        self.pid = pid
        self.pname = pname
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = self.rear = None

    # 1. Add Patient (Enqueue)
    def enqueue(self, new_node):

       
        if self.front == None:
            self.front = self.rear = new_node
            print("Patient added successfully!")
            return

        # If new patient has highest priority
        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            print("Patient added successfully!")
            return

        # Find the correct position
        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        # Insert the new patient
        new_node.next = temp.next
        temp.next = new_node

        # Update rear if inserted at the end
        if new_node.next == None:
            self.rear = new_node

        print("Patient added successfully!")

    # 2. Display Next Patient
    def display_next(self):

        if self.front == None:
            print("No patients waiting!")
        else:
            print("\nNext Patient to be Treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.pname)
            print("Priority:", self.front.priority)

    # 3. Remove Patient (Dequeue)
    def dequeue(self):

        if self.front == None:
            print("No patients to treat!")
            return

        temp = self.front

        print("\nPatient Treated Successfully!")
        print("Patient ID:", temp.pid)
        print("Patient Name:", temp.pname)
        print("Priority:", temp.priority)

        self.front = self.front.next

        if self.front == None:
            self.rear = None

    # 4. Display All Waiting Patients
    def display_all(self):

        if self.front == None:
            print("No waiting patients!")
            return

        temp = self.front

        print("\nWaiting Patients:")
        print("ID\tName\tPriority")

        while temp != None:
            print(temp.pid, "\t", temp.pname, "\t", temp.priority)
            temp = temp.next


# Main Program

pq = PriorityQueue()

while True:

    print("\n===== HOSPITAL EMERGENCY MANAGEMENT =====")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient After Treatment")
    print("4. Display All Waiting Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        pid = int(input("Enter Patient ID: "))
        pname = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority in [1, 2, 3]:
            pq.enqueue(Node(pid, pname, priority))
        else:
            print("Invalid Priority! Enter 1, 2 or 3.")

    elif choice == 2:
        pq.display_next()

    elif choice == 3:
        pq.dequeue()

    elif choice == 4:
        pq.display_all()

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")
