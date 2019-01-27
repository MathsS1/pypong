import turtle

from models.game import PongGame
from objects.menu import Menu

# the game will end after 3 goals
pong = PongGame(goal_limit=3)

pong.window.title('Pong Game by @mellomaths')
pong.window.bgcolor('black')
pong.window.setup(width=800, height=600)
pong.window.tracer(0)
pong.window.listen()

menu = Menu(pong)
pong.window.onscreenclick(menu.onclickhandler)

pong.config_keybindings()

pong.window.mainloop()

# pong.start()

