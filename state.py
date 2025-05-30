from person import Person
import random

# Global
ctime = 0
room_area = [0, 0, 500, 800]  # x1, y1, x2, y2
door = None


class PersonState:
    persons = []

    @staticmethod
    def init():
        """Initialize the person state with a list of Person objects."""
        global persons
        persons = [
            Person(position=(500, 500),
                   size=(15, 15),
                   color=(random.randint(0, 255),
                          random.randint(0, 255),
                          random.randint(0, 255)))
            for _ in range(40)
        ]

    @staticmethod
    def run_all():
        global persons
        """Update the state of all persons."""
        for person in persons:
            person.run()

        # Remove persons that have exited
        persons = [person for person in persons if person.state != "done"]
