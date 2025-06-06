from person import Person
import random
import Game
import utils

# Global
ctime = 0
room_area = [0, 0, 500, 800]  # x1, y1, x2, y2
door = None


class PersonState:
    persons = []
    total_time_spend = [[] for i in range(28)]

    @staticmethod
    def init():
        """Initialize the person state with a list of Person objects."""
        global persons, total_time_spend
        persons = []
        total_time_spend = [[] for _ in range(28)]

    def spawn_person(current_time=0):
        """Spawn a new person at a random position within the room area."""
        global persons
        cur_data = Game.observation_data[current_time // 600]
        num_persons = round(utils.random_data(
            cur_data['people_mean'], cur_data['people_std']))

        print("Minute:", current_time // 60, "Number of persons:", num_persons)
        for _ in range(num_persons):
            spend_time = round(utils.random_data(
                cur_data['spend_mean'], cur_data['spend_std']))
            transaction_time = round(utils.random_data(
                cur_data['transaction_mean'], cur_data['transaction_std']))
            spend_time -= transaction_time
            persons.append(Person(
                position=(500, 500),
                color=(random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255)),
                shopping_time=spend_time,
                transaction_time=transaction_time,
            ))

    def get_total_time_spend():
        """Get the total time spend by all persons."""
        global total_time_spend
        return total_time_spend

    def get_persons():
        """Get the list of persons."""
        global persons
        return persons

    @staticmethod
    def run_all(current_time=0):
        global persons, total_time_spend
        """Update the state of all persons."""
        for person in persons:
            person.run()

        # Remove persons that have exited
        for i in range(len(persons)):
            if not persons[i].inside:
                total_time_spend[(current_time - persons[i].total_all_time) // 600].append(
                    persons[i].total_time)
        persons = [person for person in persons if person.state != "done"]
