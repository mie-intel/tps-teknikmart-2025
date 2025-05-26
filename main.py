import game
import map
from person import Person
import random

person = [
    Person(position=(500, 500), size=(15, 15), color=(0, 255, 0)) for _ in range(100)
]
while True:
    game.run_game()
    map.create_obstacle(position=(200, 200), size=(15, 15))
    for i in person:
        i.move(random.randint(-15, 15), random.randint(-15, 15))
        i.draw()
    # person.draw()
    # person.move(random.randint(-10, 10), random.randint(-10, 10))
    game.update_game()

game.exit_game()
