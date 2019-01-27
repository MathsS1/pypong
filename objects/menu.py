import turtle

class Menu(turtle.Turtle):

    def __init__(self, game):
        turtle.Turtle.__init__(self)
        self.game = game
        self.window = game.window

        self.__FONTSIZE = 28
        self.__FONT = ('Courier', self.__FONTSIZE, 'normal')
        self.__FONT_TITLE = ('Courier', 36, 'bold')
        self.__FONT_FOOTNOTE = ('Courier', 16, 'normal')

        self.penup()
        self.penup()
        self.color('white')

        self.setpos(0, 200)
        self.write('CLASSIC', align='center', font=self.__FONT_TITLE)
        self.setpos(0, 150)
        self.write('PONG GAME', align='center', font=self.__FONT_TITLE)
        self.setpos(0, 130)
        self.write('by @mellomaths', align='center', font=self.__FONT_FOOTNOTE)

        self.setpos(100, 0)
        self.write('Close', align='center', font=self.__FONT)

        self.setpos(-100, 0)
        self.write('Start', align='center', font=self.__FONT)


    def onclickhandler(self, x, y):
        if -self.__FONTSIZE < y < self.__FONTSIZE:
            if -150 < x < -50:
                self.clear()
                self.game.start()
            elif 50 < x < 150:
                self.window.bye()

        return

        