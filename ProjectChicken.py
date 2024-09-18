"""
Final Project: "Project Chicken"
CS151
Author: Ming Zhang


Credit to Stardew Valley: "White chicken, brown chicken"
Calciumtrice: "Red, blue, green slime"
Tumblr-@odicia for background
MicroOne: Winning and losing background

"""


import turtle
import random as r

# class that contains the game's information
class Game:
    screen = turtle.Screen() # Basic global screen

    # Constructor
    def __init__(self):
        """Contains basic information that the game has"""
        Game.screen.screensize(600, 600, bg = "white")
        Game.screen.bgpic("background.gif")

        Game.screen.mode('logo')

        # turns tracer off
        turtle.tracer(False)


        self.originX = 0
        self.originY = -100

        # Boundary
        self.xMin = -350
        self.yMin = -275
        self.xMax = 350
        self.yMax = 175
        
        # Movement speed
        self.speed = 10

        # Whether or not the game is currently running
        self.started = True

        # Whether or not the game is over
        self.gameover = False

        # Makes the slimes and sets its hp and exp value
        self.slimes = self.makeSlimes(10, 15)

        # Places the slimes at their locations
        self.placeSlimes()

        # makes the chicken and sets its base attack
        self.chicken = self.makeChicken(15)

        # Places the chicken at the origin
        self.placeChicken(self.originX, self.originY)

        # Key events
        self.setupEvents()

        # Displays chicken's statistics
        self.displayStats()

        self.screen.update()


    # Plays the game
    def play(self):
        Game.screen.listen()

        Game.screen.mainloop()
    
    

        
    # Makes the chicken
    def makeChicken(self, attack):
        """Makes the chicken only if self.started is True
        has parameter of a base attack that can be set"""

        # makes a turtle object and returns it
        if self.started is True:
            chicken = turtle.Turtle()
            Game.screen.register_shape("whiteChicken1.gif")
            
            chicken.shape("whiteChicken1.gif")

            chicken.penup()
            self.attack = attack
            self.chickenExp = 0
            self.level = 1


            return chicken

    # Places the chicken at a x, y location
    def placeChicken(self, x, y):
        self.chicken.goto(x, y)        

    # Makes slimes
    def makeSlimes(self, hp, exp):
        """Makes 3 turtles named slime1, slime2, and slime3. Each slime has a base hp value and
        an exp value to give to the player when defeated. hp and exp can be set
        """

        if self.started is True:
            # registers all of the slime.gifs
            for i in range(3):
                Game.screen.register_shape("slime" + str(i+1) + ".gif")

            # sets the slime's mode to not be defeated when it is created
            self.defeat1 = False

            # makes the slime turtle with its attributes
            self.slime1 = turtle.Turtle()
            self.slime1.shape("slime1.gif")
            self.hp1 = hp
            self.exp1 = exp
            self.slime1.penup()
            
            # Does the same with slimes 2 and 3, but with different HP and different exp
            self.defeat2 = False
            self.slime2 = turtle.Turtle()
            self.slime2.shape("slime2.gif")
            self.hp2 = hp*2+10
            self.exp2 = exp + r.randrange(5, 8)
            self.slime2.penup()

            self.defeat3 = False
            self.slime3 = turtle.Turtle()
            self.slime3.shape("slime3.gif")
            self.hp3 = hp*5
            self.exp3 = exp + r.randrange(13, 17)
            self.slime3.penup()

    # places slimes at designated locations
    def placeSlimes(self):

        self.slime1.goto(-300, 100)
        self.slime2.goto(0, 100)
        self.slime3.goto(300, 100)
    
            
    
    # compares the stats of the chicken with a specified slime
    def compareStats1(self):
        if self.attack >= self.hp1 and self.chicken.distance(self.slime1.pos()) <= 80:
            self.defeat1 = True

    def compareStats2(self):
        if self.attack >= self.hp2 and self.chicken.distance(self.slime2.pos()) <= 80:
            self.defeat2 = True

    def compareStats3(self):
        if self.attack >= self.hp3 and self.chicken.distance(self.slime3.pos()) <= 80:
            self.defeat3 = True
            

    # Gives the exp to the chicken depending on which slime is defeated        
    def giveExp(self):

        # for slime1. Once it is defeated, text will show "slime defeated", which will disappear
        # after 2 seconds. Then resets the slime's defeat attribute to False
        if self.defeat1 is True and self.chicken.distance(self.slime1.pos()) <= 80:
            self.chickenExp += self.exp1
            self.defeatSlime1 = turtle.Turtle()
            self.defeatSlime1.penup()
            self.defeatSlime1.hideturtle()
            self.defeatSlime1.goto(-50, -200)
            self.defeatSlime1.write("Green Slime defeated", True, "center", ("Verdana", 10))
            self.screen.ontimer(self.defeatSlime1.undo, 2000)
            self.defeat1 is False
            self.screen.update()

        # same applies for slime2 and slime3
        if self.defeat2 is True and self.chicken.distance(self.slime2.pos()) <= 80:
            self.chickenExp += self.exp2
            self.defeatSlime2 = turtle.Turtle()
            self.defeatSlime2.penup()
            self.defeatSlime2.hideturtle()
            self.defeatSlime2.goto(-50, -200)
            self.defeatSlime2.write("Blue Slime defeated", True, "center", ("Verdana", 10))
            self.screen.ontimer(self.defeatSlime2.undo, 2000)
            self.defeat2 is False
            self.screen.update()

        if self.defeat3 is True and self.chicken.distance(self.slime3.pos()) <= 80:
            self.chickenExp += self.exp3
            self.defeatSlime3 = turtle.Turtle()
            self.defeatSlime3.penup()
            self.defeatSlime3.hideturtle()
            self.defeatSlime3.goto(-50, -200)
            self.defeatSlime3.write("Red Slime defeated", True, "center", ("Verdana", 10))
            self.screen.ontimer(self.defeatSlime3.undo, 2000)
            self.defeat3 is False      
            self.screen.update()

    # function to level the chicken up
    def levelUp(self):
        self.level += 1
        self.attack += r.randrange(15, 19)
        self.leveledUp = True

    # checks the current chicken exp and determine whether or not the chicken has leveled up
    def checkExp(self):
        correctLevel = self.chickenExp / 50
        while self.level < correctLevel:
            self.levelUp()

    # displays the chicken's attack and level
    def displayStats(self):
        self.attackStat = turtle.Turtle()
        self.attackStat.hideturtle()
        self.attackStat.penup()
        self.attackStat.goto(200, 250)
       
        self.attackStat.write("Current Attack: " + str(self.attack) + "\n Current Level: " + str(self.level), True, "center", ("Verdana", 20))
        self.screen.update()

    # Goes to game over screen if chicken loses to slime1
    def chickenDefeat1(self):
        if self.attack < self.hp1 and self.chicken.distance(self.slime1.pos()) <= 80:
            self.started = False
            self.gameover = True
            self.gameOver()
    
    # Goes to game over screen if chicken loses to slime2
    def chickenDefeat2(self):
        if self.attack < self.hp2 and self.chicken.distance(self.slime2.pos()) <= 80:
            self.started = False
            self.gameover = True
            self.gameOver()

    # Goes to game over screen if chicken loses to slime3
    def chickenDefeat3(self):
        if self.attack < self.hp3 and self.chicken.distance(self.slime3.pos()) <= 80:
            self.started = False
            self.gameover = True
            self.gameOver()

    # sets self.started to false if chicken collides with slime
    def checkCollisions(self):
        self.slime1Collision = False
        self.slime2Collision = False
        self.slime3Collision = False

        # Conditionals if collided
        if self.started is True:

            # give textboxes that display options
            if self.chicken.distance(self.slime1.pos()) <= 55:
                self.slime1Collision = True
                self.chicken.forward(-self.speed)
                self.started = False
                self.textBox()


            if self.chicken.distance(self.slime2.pos()) <= 55:
                self.slime2Collision = True
                self.chicken.forward(-self.speed)
                self.started = False
                self.textBox()


            if self.chicken.distance(self.slime3.pos()) <= 55:
                self.chicken.forward(-self.speed)
                self.slime3Collision = True
                self.started = False
                self.textBox()

        self.screen.ontimer(self.checkCollisions, 10)
        self.screen.update()

    # creates yes and no textboxes, as well as questions for chicken when they collide
    # with slime
    def textBox(self):
        if self.started is False:
            Game.screen.tracer(False)
            self.selection = turtle.Turtle()
            self.selection.hideturtle()
            self.selection.penup()
            self.selection.goto(-200, -200)
            self.selection.begin_fill()
            self.selection.fillcolor("pink")
            self.selection.pendown()
            for i in range(4):
                self.selection.forward(50)
                self.selection.right(90)
            self.selection.end_fill()
            self.selection.penup()
            self.selection.goto(-185, -175)
            self.selection.write("Yes")


            self.selection.penup()
            self.selection.goto(200, -200)
            self.selection.pendown()
            self.selection.begin_fill()
            self.selection.fillcolor("yellow")
            for i in range(4):
                self.selection.forward(50)
                self.selection.right(90)
            self.selection.end_fill()
            self.selection.penup()
            self.selection.goto(220, -175)
            self.selection.write("No")


            if self.slime1Collision is True:
                self.text = turtle.Turtle()
                self.text.penup()
                self.text.hideturtle()
                self.text.goto(-300, -50)
                self.text.write("DO YOU WANT TO FIGHT THE GREEN SLIME? \n CLICK YES FOR YES. CLICK NO FOR NO", font=("Verdana", 20))     
                 
            elif self.slime2Collision is True:
                self.text = turtle.Turtle()
                self.text.penup()
                self.text.hideturtle()
                self.text.goto(-300, -50)
                self.text.write("DO YOU WANT TO FIGHT THE BLUE SLIME? \n CLICK YES FOR YES. CLICK NO FOR NO", font=("Verdana", 20))

            elif self.slime3Collision is True:
                self.text = turtle.Turtle()
                self.text.penup()
                self.text.hideturtle()
                self.text.goto(-300, -50)
                self.text.write("DO YOU WANT TO FIGHT THE RED SLIME? \n CLICK YES FOR YES. CLICK NO FOR NO", font=("Verdana", 20))
        

        
    # controls key events
    def setupEvents(self):
        Game.screen.onkeypress(self.up, "Up")
        Game.screen.onkeypress(self.down, "Down")
        Game.screen.onkeypress(self.left, "Left")
        Game.screen.onkeypress(self.right, "Right")
        Game.screen.listen()
        Game.screen.onclick(self.yesNoClick)
        Game.screen.onkey(turtle.bye, "q")


        self.screen.ontimer(self.checkCollisions, 10)
        self.screen.update()

    # Controls the whether the slime is fought
    def yesNoClick(self, mouseX, mouseY):
        if self.started is False:            

            if mouseY < -150 and mouseY > -200:
                if mouseX > 200 and mouseX < 250:
                    self.started = True
                    self.chicken.goto(self.originX, self.originY)
                    self.selection.clear()
                    self.text.clear()
                    self.screen.update()

                # controls what happens if the chicken wins or loses
                elif mouseX > -200 and mouseX < -150:
                    self.started = True
                    if self.chicken.distance(self.slime1.pos()) <= 80:
                        self.compareStats1()
                    
                    if self.chicken.distance(self.slime2.pos()) <= 80:
                        self.compareStats2()
                    
                    if self.chicken.distance(self.slime3.pos()) <= 80:
                        self.compareStats3()
                        
                    self.giveExp()
                    self.checkExp()
                    self.winGame()

                    self.chickenDefeat1()
                    self.chickenDefeat2()
                    self.chickenDefeat3()

                    self.newAttack = 0
                    self.newAttack += self.attack

                    self.newLevel = 0
                    self.newLevel += self.level

                    self.attackStat.undo()
                    self.attackStat.goto(200, 250)
                    self.attackStat.write("Current Attack: " + str(self.newAttack) + "\n Current Level: " + str(self.newLevel), True, "center", ("Verdana", 20))

                    self.chicken.goto(self.originX, self.originY)
                    self.selection.clear()
                    self.text.clear()
                    self.screen.update()
                print(self.chickenExp)
            

    # command for moving upwards
    def up(self):
        if self.started is True:
            self.chicken.setheading(0)
            self.chicken.forward(self.speed)

            if self.chicken.xcor() < self.xMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() < self.yMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")

            if self.chicken.xcor() > self.xMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() > self.yMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")



        self.screen.update()

    # command for moving downwards
    def down(self):
        if self.started is True:    
            self.chicken.setheading(180)
            self.chicken.forward(self.speed)

            if self.chicken.xcor() < self.xMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() < self.yMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")

            if self.chicken.xcor() > self.xMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() > self.yMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")


        self.screen.update()
        
    # command for moving left
    def left(self):
        if self.started is True:
            self.chicken.setheading(270)
            self.chicken.forward(self.speed)
            
            self.chicken.shape("whiteChicken1.gif")

            if self.chicken.xcor() < self.xMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() < self.yMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")

            if self.chicken.xcor() > self.xMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() > self.yMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")

        self.screen.update()

    # command for moving right
    def right(self):

        Game.screen.register_shape("whiteChicken2.gif")
        if self.started is True:
            self.chicken.setheading(90)
            self.chicken.forward(self.speed)
            
            self.chicken.shape("whiteChicken2.gif")

            if self.chicken.xcor() < self.xMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() < self.yMin:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")

            if self.chicken.xcor() > self.xMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            
            if self.chicken.ycor() > self.yMax:
                self.chicken.forward(-self.speed)
                print("You cannot leave the screen")
            

        self.screen.update()
        
        
    # displays game over screen if chicken loses to slime
    def gameOver(self):
        if self.gameover is True:
            Game.screen.clear()
            self.over = turtle.Turtle()
            self.over.hideturtle()
            self.over.penup()

            Game.screen.bgpic("otherBackground.gif")
            self.over.write("GAME OVER \n PRESS Q TO EXIT", True, "center", ("Verdana", 60))
            Game.screen.listen()
            Game.screen.onkey(turtle.bye, "q")
            Game.screen.mainloop()
        self.screen.update()
    
    # displays winning screen if chicken hits specified level
    def winGame(self):
        if self.level == 8:
            Game.screen.clear()
            self.newChicken = turtle.Turtle()
            Game.screen.register_shape("brownChicken.gif")
            self.newChicken.shape("brownChicken.gif")
            self.newChicken.penup()
            self.newChicken.goto(0, -200)

            Game.screen.bgpic("otherBackground.gif")
            self.win = turtle.Turtle()
            self.win.hideturtle()
            self.win.penup()
            self.win.write("CONGRATULATIONS!!! \n YOU ARE THE CHICKEN \n AMONGST CHICKENS \n PRESS Q TO EXIT", True, "center", ("Verdana", 30))
            Game.screen.listen()
            Game.screen.onkey(turtle.bye, "q")
            Game.screen.mainloop()
        self.screen.update()


def main():
    game = Game()
    game.play()

if __name__ == "__main__":
    main()
            