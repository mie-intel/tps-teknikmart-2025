import game
import map
from person import Person
import random

person = [
    Person(position=(500, 500), size=(15, 15), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for _ in range(1)
]
while True:
    game.run_game()
    map.create_obstacle(position=(200, 200), size=(15, 15))
    for i in person:
        # i.move(30, 30)
        i.run()
    # person.draw()
    # person.move(random.randint(-10, 10), random.randint(-10, 10))
    game.update_game()

game.exit_game()
