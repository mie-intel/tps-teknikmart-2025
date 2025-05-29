import game
import map
from person import Person
import random
from config import *

person = [
    Person(position=(500, 500), size=(15, 15), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))) for _ in range(40)
]


while True:
    game.run_game()
    # map.create_obstacle(position=(200, 200), size=(15, 15))
    map.create_obstacle(position=(150, 600), size=(300, 20))
    game.cashier.draw()
    for i in person:
        i.run()
    game.draw_time()
    game.update_game()

game.exit_game()
