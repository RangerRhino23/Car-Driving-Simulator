from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import assets.APIs.first_person_movement_api as fpm
import assets.APIs.vehicle_movement_api as vm
import assets.APIs.environment_api as ea

app = Ursina()

def update():
    fpm.player_movement(player, 15)

def input(key):
    if key == 'q':
        application.quit()

ea.build_environment(ground_scale=1500, height=50, walls_invis=False, build_walls=True)

player = FirstPersonController()
car = vm.Vehicle(model='assets/models/car.obj', position=(10,0,10), acceleration=1, friction=35.0, max_velocity=100, driver=player)
car2 = vm.Vehicle(model='assets/models/car2.obj', scale=2, position=(-10,0,-10), acceleration=1, friction=55.0, max_velocity=120, driver=player)

app.update = update()
app.run()