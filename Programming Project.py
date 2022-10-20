# Thanks to Kenney Vleugels (www.kenney.nl) for the images used in the game

import pygame as py  # imports the pygame module, used to make the game screen
import random  # imports the random module, used to make generate values randomly
import os  # imports to os module to me get resources from files.
import tkinter  # imports the tkinter module
import time  # imports the time mod

py.init()  # initialising the pygame module
py.font.init()  # initialises the fonts that will be used later.
resolution = tkinter.Tk()
monitorWidth = resolution.winfo_screenwidth()  # Finds the monitor's height.
monitorHeight = resolution.winfo_screenheight()  # Finds the monitor's width.
width = monitorWidth * 0.95  # Height and width of the game of  90% of the height and width of the monitor screen
height = monitorHeight * 0.9
width, height = round(width), round(height)  # Rounds the height and width as every expects them as in integer
if height < 600 or width < 900:  # If the determined height and width of the screen are too small, the game can't be played.
    print("\nThis screen too small to play the game on properly as wither its height is less than 650 pixels or its width is less than 900 pixels.\n")
    time.sleep(5)
    os._exit(0)
win = py.display.set_mode((width, height))  # Makes the screen for the game, using the rounded height and width.
py.display.set_caption("2D Wave Based Shooter")  # Title of the game.

# This part contains all images needed in the game, which are all loaded from the img folder.
playerShipImg = py.image.load(os.path.join("img", "playerShip.png")).convert()  # Loads player ship image
player2ShipImg = py.image.load(os.path.join("img", "playerShip2.png")).convert()  # Loads second player ship image
bgBlue = py.transform.scale(py.image.load(os.path.join("img", "blue.png")),
                            (width, height)).convert()  # Loads background image
bgDarkPurple = py.transform.scale(py.image.load(os.path.join("img", "darkPurple.png")),
                                  (width, height)).convert()  # Loads second background image
bgPurple = py.transform.scale(py.image.load(os.path.join("img", "purple.png")),
                              (width, height)).convert()  # Loads third background image
playerLaserImg = py.image.load(os.path.join("img", "redLaser.png")).convert()  # Loads images for player weapons
playerBombImg = py.image.load(os.path.join("img", "Bomb.png")).convert()
basicEnemyImg = py.image.load(
    os.path.join("img", "basicEnemy.png")).convert()  # Loads images for enemy spaceships and weapons
basicEnemyLaserImg = py.image.load(os.path.join("img", "blueLaser.png")).convert()
moderateEnemyImg = py.image.load(os.path.join("img", "moderateEnemy.png")).convert()
moderateEnemyLaserImg = py.image.load(os.path.join("img", "greenLaser.png")).convert()
dropperEnemyImg = py.image.load(os.path.join("img", "dropperEnemy.png")).convert()
dropperEnemyLaserImg = py.image.load(os.path.join("img", "dropperRedLaser.png")).convert()
strongEnemyImg = py.image.load(os.path.join("img", "strongEnemy.png")).convert()
strongEnemyLaserImg = py.image.load(os.path.join("img", "blueLaserStrong.png")).convert()
# Images for the differently-sized meteors
meteorImg = [py.image.load(os.path.join("img", "smallMeteor.png")).convert(),
             py.image.load(os.path.join("img", "mediumMeteor1.png")).convert(),
             py.image.load(os.path.join("img", "mediumMeteor2.png")).convert(),
             py.image.load(os.path.join("img", "bigMeteor.png")).convert()]
hozLaserBeamImg = py.image.load(os.path.join("img", "hozLaserBeam.png")).convert()  # Loads images for the laser beams
verLaserBeamImg = py.image.load(os.path.join("img", "verLaserBeam.png")).convert()
beamWarningImg = py.image.load(
    os.path.join("img", "laserWarning.png")).convert()  # Loads image for the warning before the laser beam
# Images for the first boss and their weapons
boss1Img = py.image.load(os.path.join("img", "ufoBlue.png")).convert()
boss1LaserImg = py.image.load(os.path.join("img", "blueLaserBoss.png")).convert()
boss1TrackingLaserImg = py.image.load(os.path.join("img", "blueLaserTracking.png")).convert()
boomerangLaserImg = py.image.load(os.path.join("img", "boomerangLaser.png")).convert()
# Image for the second boss
boss2Img = py.image.load(os.path.join("img", "ufoGreen.png")).convert()
# Images for the third boss and their weapons
boss3Img = py.image.load(os.path.join("img", "ufoRed.png")).convert()
laserStarImg = py.image.load(
    os.path.join("img", "laserStar.png")).convert()  # Four lasers will split off from the original one
fourLasersImg = [py.image.load(os.path.join("img", "bossLaserUp.png")).convert(),
                 py.image.load(os.path.join("img", "bossLaserDown.png")).convert(),
                 py.image.load(os.path.join("img", "bossLaserLeft.png")).convert(),
                 py.image.load(os.path.join("img", "bossLaserRight.png")).convert()]
followingLaserImg = py.image.load(os.path.join("img", "followingLaser.png")).convert()
# This part contains all of the sounds needed in the game, loaded from the Sounds folder
# Sounds effects for the game
playerLaser = py.mixer.Sound(os.path.join("Sounds", "playerLaser.wav"))  # Sound effects for player weapons
playerBomb = py.mixer.Sound(os.path.join("Sounds", "playerBomb.wav"))
enemyLaser = py.mixer.Sound(os.path.join("Sounds", "enemyLaser.wav"))  # Sound effects for enemy weapons
laserBeam = py.mixer.Sound(os.path.join("Sounds", "laserBeam.wav"))
bossLaser = py.mixer.Sound(os.path.join("Sounds", "bossLaser.wav"))
enemyCollision = py.mixer.Sound(os.path.join("Sounds", "enemyCollision.wav"))  # Sounds effects for the collisions
meteorCollision = py.mixer.Sound(os.path.join("Sounds", "meteorCollision.wav"))
playerCollision = py.mixer.Sound(os.path.join("Sounds", "playerCollision.wav"))
gamemode = py.mixer.Sound(os.path.join("Sounds", "gamemode.wav"))  # Sound effects in the main menu
section = py.mixer.Sound(os.path.join("Sounds", "section.wav"))

# Music for the game
music = py.mixer.music.load(os.path.join("Sounds", "Bonetrousle.mid"))

powerupImg = {}  # Images for the different powerups
powerupImg["moreHealth"] = py.image.load(os.path.join("img", "health.png")).convert()
powerupImg["moreAmmo"] = py.image.load(os.path.join("img", "ammo.png")).convert()


# This part contains all of the classes.
class Player(py.sprite.Sprite):  # The Player class
    def __init__(self):
        py.sprite.Sprite.__init__(self)  # Initialises the use of a sprite.
        self.image = py.transform.scale(playerShipImg, (80, 70))  # Loads the image for the player sprite.
        self.rect = self.image.get_rect()
        self.rect.center = (100, height // 2)  # Where the player spawns onscreen.
        self.image.set_colorkey((0, 0, 0))  # Any black on the image file is removed.
        self.speed = 8
        self.radius = (self.rect.height // 2)  # Determines player's hitbox
        self.up = False  # These four booleans track the direction the player is moving in at any given time.
        self.down = False
        self.left = False
        self.right = False
        self.dashDelay = 200  # Number of ingame ticks before the player can dash again.
        self.lastDash = py.time.get_ticks()
        self.dashSpeed = 150  # Number of pixels they move when they dash.
        self.shootDelay = 200  # Number of frames before the player can shoot another laser
        self.lastShot = py.time.get_ticks()
        self.ammo = 200  # Amount of ammo left for the lasers
        self.lastDrop = py.time.get_ticks()
        self.health = 100  # Current amount of player health
        self.maxHealth = 100  # Maximum amounts of health and ammo available.
        self.maxAmmo = 200

    # This is the player movement method.
    def update(self):
        key = py.key.get_pressed()
        if key[py.K_LEFT] and self.rect.left >= 10:
            # Player moves left when the left arrow is pressed and they aren't too close to the left end of the screen.
            self.rect.x -= self.speed
            self.up = False  # When they move left the variable self.left becomes True to track this direction.
            self.down = False
            self.left = True
            self.right = False
        if key[py.K_RIGHT] and self.rect.right <= width - 10:
            # Player moves right when the right arrow is pressed and they aren't too close to the right end of the screen.
            self.rect.x += self.speed
            self.up = False  # When they move right then self.right=True to track this movement.
            self.down = False
            self.left = False
            self.right = True
        if key[py.K_UP] and self.rect.top >= 10:
            # Player moves up when the up arrow is pressed and they aren't too close to the top of the screen.
            self.rect.y -= self.speed
            self.up = True  # When they move up then self.up=True to track their upwards movement.
            self.down = False
            self.left = False
            self.right = False
        if key[py.K_DOWN] and self.rect.bottom <= height - 25:
            # Player moves down when the down arrow is pressed and they aren't too close to the bottom of the screen.
            self.rect.y += self.speed
            self.up = False  # When they move down then self.down=True to track their downwards movement.
            self.down = True
            self.left = False
            self.right = False
        if key[py.K_z] and self.ammo > 0:
            self.shoot()  # When z is pressed, lasers are fired.
        if key[py.K_x]:
            self.drop()  # When x is pressed, bombs are dropped.
        if key[py.K_c]:
            self.health = self.maxHealth  # Debugging

    def dash(self):
        time = py.time.get_ticks()  # Starts measuring the number of ticks from this point.
        if time - self.lastDash > self.dashDelay:  # Checks if more than 200 frames have passed since the last dash.
            self.lastDash = time
            if self.up:  # They dash upwards if they are moving upwards.
                self.rect.y -= self.dashSpeed
                if self.rect.top < 10:
                    self.rect.top = 10
            if self.down:  # They dash downwards if they are moving downwards.
                self.rect.y += self.dashSpeed
                if self.rect.bottom > height - 25:
                    self.rect.bottom = height - 25
            if self.left:  # They dash to the left if they are moving to the left.
                self.rect.x -= self.dashSpeed
                if self.rect.left < 10:
                    self.rect.left = 10
            if self.right:  # They dash to the right if they are moving to the right.
                self.rect.x += self.dashSpeed
                if self.rect.right > width - 10:
                    self.rect.right = width - 10
        # All four of the nested if statements stop the player from dashing offscreen.

    def shoot(self):
        now = py.time.get_ticks()
        if now - self.lastShot > self.shootDelay:  # Checks if more than 200 frames have passed since the last shot.
            self.lastShot = now
            laser1 = PlayerLaser(self.rect.right, self.rect.top)  # One laser is spawned at the top of the ship
            laser2 = PlayerLaser(self.rect.right, self.rect.bottom)  # One is spawned at the bottom of the ship
            allSprites.add(laser1)  # The lasers are added to the relevant sprite groups
            playerWeapons.add(laser1)
            allSprites.add(laser2)
            playerWeapons.add(laser2)
            self.ammo -= 2  # Every time the player shoots they lose two ammo.
            playerLaser.play()

    def drop(self):
        bombTime = py.time.get_ticks()
        if bombTime - self.lastDrop > self.shootDelay:  # Checks if > 200 frames have passed since the last bomb drop.
            self.lastDrop = bombTime
            bomb1 = PlayerBomb(self.rect.centerx, self.rect.bottom)  # Bomb is spawned beneath the ship.
            allSprites.add(bomb1)  # The bomb is added to the relevant sprite groups
            playerWeapons.add(bomb1)
            playerBomb.play()


class Player1(Player, py.sprite.Sprite):
    def __init__(self):
        Player.__init__(self)
        super().__init__()  # Inherits all attributes and methods from player class
        self.rect.center = (100, 200)

    def update(self):
        key = py.key.get_pressed()
        if key[py.K_LEFT] and self.rect.left >= 10:
            # Player moves left when the left arrow is pressed and they aren't too close to the left end of the screen.
            self.rect.x -= self.speed
            self.up = False  # When they move left the variable self.left becomes True to track this direction.
            self.down = False
            self.left = True
            self.right = False
        if key[py.K_RIGHT] and self.rect.right <= width - 10:
            # Player moves right when the right arrow is pressed and they aren't too close to the right end of the screen.
            self.rect.x += self.speed
            self.up = False  # When they move right then self.right=True to track this movement.
            self.down = False
            self.left = False
            self.right = True
        if key[py.K_UP] and self.rect.top >= 10:
            # Player moves up when the up arrow is pressed and they aren't too close to the top of the screen.
            self.rect.y -= self.speed
            self.up = True  # When they move up then self.up=True to track their upwards movement.
            self.down = False
            self.left = False
            self.right = False
        if key[py.K_DOWN] and self.rect.bottom <= height - 25:
            # Player moves down when the down arrow is pressed and they aren't too close to the bottom of the screen.
            self.rect.y += self.speed
            self.up = False  # When they move down then self.down=True to track their downwards movement.
            self.down = True
            self.left = False
            self.right = False
        if key[py.K_PERIOD] and self.ammo > 0:
            self.shoot()  # When z is pressed, lasers are fired.
        if key[py.K_SLASH]:
            self.drop()  # When x is pressed, bombs are dropped.


class Player2(Player, py.sprite.Sprite):
    def __init__(self):
        Player.__init__(self)
        super().__init__()  # Inherits all attributes and methods from the Player class
        self.image = player2ShipImg  # Loads the image player 2 spaceship
        self.rect = self.image.get_rect()  # Uses a new rect for the new image
        self.image.set_colorkey((0, 0, 0))
        self.rect.center = (100, height - 200)

    def update(self):
        key = py.key.get_pressed()
        if key[py.K_a] and self.rect.left >= 10:
            # Player moves left when A is pressed and they aren't too close to the left end of the screen.
            self.rect.x -= self.speed
            self.up = False  # When they move left the variable self.left becomes True to track this direction.
            self.down = False
            self.left = True
            self.right = False
        if key[py.K_d] and self.rect.right <= width - 10:
            # Player moves right when D is pressed and they aren't too close to the right end of the screen.
            self.rect.x += self.speed
            self.up = False  # When they move right then self.right=True to track this movement.
            self.down = False
            self.left = False
            self.right = True
        if key[py.K_w] and self.rect.top >= 10:
            # Player moves up when W is pressed and they aren't too close to the top of the screen.
            self.rect.y -= self.speed
            self.up = True  # When they move up then self.up=True to track their upwards movement.
            self.down = False
            self.left = False
            self.right = False
        if key[py.K_s] and self.rect.bottom <= height - 25:
            # Player moves down when S arrow is pressed and they aren't too close to the bottom of the screen.
            self.rect.y += self.speed
            self.up = False  # When they move down then self.down=True to track their downwards movement.
            self.down = True
            self.left = False
            self.right = False
        if key[py.K_c] and self.ammo > 0:
            self.shoot()  # When c is is pressed, lasers are fired
        if key[py.K_v]:
            self.drop()  # When v is pressed, bombs are dropped


class PlayerLaser(py.sprite.Sprite):  # The player's laser weapon class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = playerLaserImg  # Loads the image used for the laser sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial x and y coordinate depends player's position.
        self.image.set_colorkey((0, 0, 0))
        self.speed = 10

    def update(self):
        self.rect.x += self.speed  # Moves at 10 pixels per frame
        if self.rect.left >= width:
            self.kill()  # If the laser moves offscreen it is removed.


class PlayerBomb(py.sprite.Sprite):  # The player's bomb weapon class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = playerBombImg  # Loads the image used for the bomb sprite
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial x and y coordinate depends player's position.
        self.image.set_colorkey((0, 0, 0))
        self.speed = 10

    def update(self):
        self.rect.y += self.speed  # Bomb moves downwards by 10 pixels per frame.
        if self.rect.top >= height:
            self.kill()  # If the bomb moves below the screen it is removed.


class BasicEnemy(py.sprite.Sprite):  # The basic enemy class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(basicEnemyImg, (60, 60))  # Loads the basic enemy's image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(width + 100, width + 900)  # Each basic enemy's x and y coordinates are randomised.
        self.rect.y = random.randint(0, height - 60)
        self.speed = 5
        self.radius = (self.rect.height // 2)  # Determines the hitbox of an enemy.
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x -= self.speed  # Moves 5 pixels to the left per frame.
        if self.rect.right <= 0:  # If the enemy moves offscreen when moving left they will be removed.
            self.kill()
        if random.random() > 0.995:
            self.shoot()  # This method is called when a random value from 0-1 is > 0.995

    def shoot(self):  # This method creates a basic laser object to be shot at the player.
        basicLaser = BasicLaser(self.rect.left, self.rect.centery)
        allSprites.add(basicLaser)  # Adds the object to the necessary sprite groups
        basicEnemyWeapons.add(basicLaser)
        enemyLaser.play()  # Plays enemy laser sound


class BasicLaser(py.sprite.Sprite):  # The basic enemy laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = basicEnemyLaserImg  # Loads the basic enemy laser's images
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # The x and y coordinate depend on the position of the basic enemy
        self.speed = 10
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x -= self.speed  # Laser moves at 10 pixels per frame leftwards
        if self.rect.right <= 0:
            self.kill()  # If the laser moves offscreen to the left, it is removed.


class Meteor(py.sprite.Sprite):  # The meteor hazard class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteorImg)  # Loads the image for the meteor sprite, which is randomly selected.
        self.rect = self.image_orig.get_rect()
        self.image = self.image_orig.copy()
        self.rect.x = random.randint(0, width - 100)  # Meteor spawns are a random point across the screen
        self.rect.y = random.randint(-300, -100)  # It spawns at a random point above the screen.
        self.speedY = 5
        self.speedX = random.choice([-3, 3, 0])  # It could move to the left or right or only move vertically.
        self.radius = (self.rect.height // 2)  # Determines the hitbox of the meteor
        self.rotate = 0
        self.rotateSpeed = random.choice([-5, 5])  # Meteor rotates either to the left or right.
        self.rotTime = py.time.get_ticks()
        self.image_orig.set_colorkey((0, 0, 0))

    def rotateMeteor(self):  # Method for rotating the meteor
        timeNow = py.time.get_ticks()
        if timeNow - self.rotTime > 50:  # Every 50 ticks the meteor will rotate
            self.rotTime = timeNow
            self.rotate = (self.rotate + self.rotateSpeed) % 360
            self.image = py.transform.rotate(self.image_orig, self.rotate)  # A new rotated meteor image is loaded.

    def update(self):
        self.rotateMeteor()
        self.rect.x += self.speedX  # Moves downwards and simultaneously left, right or down the middle.
        self.rect.y += self.speedY
        if self.rect.top > height:
            self.kill()  # The meteor is removed if it moves downwards offscreen.


class Powerup(py.sprite.Sprite):  # This is the powerup class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.powerupType = random.choice(["moreHealth", "moreAmmo"])
        self.image = powerupImg[self.powerupType]  # The powerup is randomly selected from more health or ammo.
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.center = (x, y)  # The initial coordinates depend on those of the meteor when it was destroyed
        self.speed = 4  # Moves at 4 pixels per frame

    def update(self):
        self.rect.y += self.speed  # The powerup continously moves downwards after spawning
        if self.rect.top >= height:
            self.kill()  # If it moves beneath the screen, it is removed from the game.


class HozBeamWarning(py.sprite.Sprite):  # The class for the warning before the laser beam fires.
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(beamWarningImg, (100, 100))  # Loads the image for the warning
        self.rect = self.image.get_rect()
        self.rect.x = width - 100  # Always spawns at the end of the screen
        self.rect.y = random.randint(0, height - 100)  # Height of the warning is randomised onscreen
        self.image.set_colorkey((0, 0, 0))
        self.timeOnscreen = py.time.get_ticks()
        self.limit = 2000  # Amount of time laser beam stays onscreen for.

    def update(self):
        timeNow = py.time.get_ticks()
        if timeNow - self.timeOnscreen > self.limit:
            self.timeOnscreen = timeNow
            self.kill()  # After 2000 ticks the warning will disappear
            hozLaserBeam = HozLaserBeam(self.rect.y)
            allSprites.add(hozLaserBeam)  # The laser beam is created and added to relevant sprite groups
            laserBeams.add(hozLaserBeam)


class HozLaserBeam(py.sprite.Sprite):  # The horizontal laser beam class
    def __init__(self, y):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(hozLaserBeamImg, (width, 100))  # Loads the image for the laser beam
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = 0  # Always spawns at the left end of the screen and stretches to the right end
        self.rect.y = y  # The height of the depends on the height of the warning
        self.limit = 3000  # Laser beam appears for 3000 frames.
        self.timeOnscreen = py.time.get_ticks()

    def update(self):
        laserBeam.play()
        timeNow = py.time.get_ticks()
        if timeNow - self.timeOnscreen > self.limit:
            self.timeOnscreen = timeNow  # After 3000 ticks the laser beam is removed from the game.
            self.kill()
            laserBeam.stop()  # Stops the sound effect when it is removed


class ModerateEnemy(py.sprite.Sprite):  # The moderate enemy class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(moderateEnemyImg, (80, 80))  # Loads image for the enemy
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = random.randint(width + 100, width + 800)  # Initial x-position at some point behind the screen
        self.rect.y = random.randint(height // 2 - 300, height // 2 + 300)  # Initial y-position randomised onscreen
        self.speedY = random.choice([-3, 3, 0])  # Player moves up, down or stright when moving leftwards.
        self.speedX = 8
        self.radius = (self.rect.height // 2)  # Determines the enemy hitbox

    def update(self):
        self.rect.x -= self.speedX  # Moves 10 pixels per tick to the left
        self.rect.y += self.speedY
        if self.rect.right <= 0:
            self.kill()  # If they move offscreen, they are removed from the game.
        if random.random() > 0.995:
            self.shoot()  # This method can be called at random.

    def shoot(self):  # Method used to create lasers shot from the enemy
        moderateLaser1 = ModerateLaser(self.rect.left, self.rect.centery)  # ModerateLaser class is called once.
        allSprites.add(moderateLaser1)  # Laser is added to the relevant sprite groups.
        moderateEnemyWeapons.add(moderateLaser1)
        enemyLaser.play()  # Plays enemy laser sound


class ModerateLaser(py.sprite.Sprite):  # The moderate enemy's laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = moderateEnemyLaserImg  # Loads the image for the laser
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))  # Any black on the image is removed.
        self.rect.center = (x, y)  # Coordinates depend on position of the moderate enemy
        self.speed = 10  # Moves at 10 pixels per tick

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()  # If the laser moves offscreen, it is removed from the game


class Boss1(py.sprite.Sprite):  # Class for the first boss
    def __init__(self):
        py.sprite.Sprite.__init__(self)  # Initialises the boss sprite
        self.image = py.transform.scale(boss1Img, (120, 120))  # Loads the boss image
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = width + 200  # Initially spawns behind the screen
        self.rect.y = height // 2  # Initally spawns in the middle as well
        self.speed = 10  # Determines the speed of the boss
        self.health = 50  # Starts off with 50 health points
        self.up = True  # Determines whether the boss moves up or down
        self.radius = self.rect.height // 2
        self.tracking = False

    def update(self):
        if self.rect.right > width - 50:
            self.rect.x -= self.speed  # Until the boss is fully onscreen, it will move to the left
        else:
            if self.up:  # When self.up is True the boss moves upwards
                self.rect.y -= self.speed
                if self.rect.top <= 0:
                    self.up = False  # When the top of the boss hits the top of the screen self.up is False
            if not self.up:  # When self.up is False the boss moves downwards
                self.rect.y += self.speed
                if self.rect.bottom >= height:
                    self.up = True  # When the bottom of the boss hits the screen bottom, self.up becomes True
            if random.random() > 0.94:
                attack = random.choice([0, 1, 2])  # There are three boss attacks in the bossfight.
                if attack == 0:  # Randomly-chosen attack where the boss fires two lasers at the player
                    boss1Laser1 = Boss1Laser(self.rect.centerx, self.rect.top)
                    boss1Laser2 = Boss1Laser(self.rect.centerx, self.rect.bottom)
                    allSprites.add(boss1Laser1, boss1Laser2)  # Lasers are added to the relevant sprite groups
                    basicEnemyWeapons.add(boss1Laser1, boss1Laser2)
                    bossLaser.play()
                if attack == 1 and self.health < 35 and not self.tracking:  # This attack is selected if it is chosen and the boss's health is <35
                    self.tracking = True
                    boss1Warning = Boss1Warning()  # The warning sign for the tracking laser is added onscreen.
                    allSprites.add(boss1Warning)
                if attack == 2 and self.health < 20:  # This attack is selected if it is chosen and the boss's health is <20
                    boomerangLaser = BoomerangLaser(self.rect.left, self.rect.centery)
                    allSprites.add(boomerangLaser)  # The boomerang laser is added to the relevant sprite groups
                    moderateEnemyWeapons.add(boomerangLaser)
                    bossLaser.play()


class Boss1Laser(py.sprite.Sprite):  # The first boss's laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = boss1LaserImg  # Loads the image for the laser.
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.center = (x, y)  # Spawn of the laser depends on the position of the first boss
        self.speed = 12  # Moves at 12 pixels per tick

    def update(self):
        self.rect.x -= self.speed  # Moves leftwards across the screen
        if self.rect.right <= 0:
            self.kill()  # Laser is removed from the game if it moves offscreen.


class Boss1Warning(py.sprite.Sprite):  # The class for the warning before the first boss's tracking laser
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(beamWarningImg, (50, 50))  # Loads the image for the warning
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.x = 0  # x-coordinate always at the left end of the screens
        self.rect.y = height // 2  # y-coordinate is the same as the player's position
        self.limit = 2000  # After 2000 ticks, it disappears and laser is spawned.
        self.target = False
        self.targetPlayer1 = False
        self.getTime = py.time.get_ticks()

    def update(self):
        timeNow = py.time.get_ticks()
        if singleplayer:  # Laser target one player if in singleplayer
            self.rect.y = player.rect.y  # Y-coordinate constantly being updated to be the player's y-position
        if not singleplayer:  # Laser targets either player when in multiplayer
            if not self.target:
                if random.random() > 0.5:  # Laser warning has a 50% chance of targeting either player
                    self.targetPlayer1 = True
                else:
                    self.targetPlayer1 = False
                self.target = True  # Target can't change for this laser warning
            if self.targetPlayer1:  # When this is True, the warning follows player 1 on the y-axis
                self.rect.y = player1.rect.y
            if not self.targetPlayer1:  # When this is False, the warning follows player 2 on the y-axis
                self.rect.y = player2.rect.y
        if timeNow - self.getTime > self.limit:
            self.getTime = timeNow
            self.kill()  # It is removed from the program after 2000 ticks
            boss1TrackingLaser = Boss1TrackingLaser(self.rect.x, self.rect.centery)
            allSprites.add(boss1TrackingLaser)  # Tracking laser is added to the relevant sprite groups.
            moderateEnemyWeapons.add(boss1TrackingLaser)
            boss1.tracking = False
            self.target = False
            bossLaser.play()


class Boss1TrackingLaser(py.sprite.Sprite):  # The first boss's tracking laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = boss1TrackingLaserImg  # Loads the image for the tracking laser.
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))
        self.rect.center = (x, y)  # Spawn of the laser depends on the position of the position of the warning sign
        self.speed = 40  # Moves at 30 pixels per tick

    def update(self):
        self.rect.x += self.speed  # Moves rightwards across the screen
        if self.rect.left >= width:
            self.kill()  # Laser is removed from the game if it moves offscreen.


class BoomerangLaser(py.sprite.Sprite):  # The boomerang laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image_orig = boomerangLaserImg  # Loads the image for the boomerang laser
        self.rect = self.image_orig.get_rect()
        self.image = self.image_orig.copy()  # Creates a copy of laser image
        self.rect.center = (x, y)  # It initial spawn depends on the position of the first boss
        self.speed = 15  # Moves at 10 pixels per tick
        self.rotateLaser = 0
        self.rotateSpeed = random.choice([-5, 5])  # Laser rotates either to the right or left
        self.rotTime = py.time.get_ticks()
        self.left = True
        self.image_orig.set_colorkey((0, 0, 0))

    def rotateBoomerangLaser(self):
        timeNow = py.time.get_ticks()
        if timeNow - self.rotTime > 50:  # Every 50 ticks the laser rotates
            self.rotTime = timeNow
            self.rotateLaser = (self.rotateLaser + self.rotateSpeed) % 360
            self.image = py.transform.rotate(self.image_orig,
                                             self.rotateLaser)  # A new rotated image for the laser is loaded

    def update(self):
        self.rotateBoomerangLaser()
        if self.rect.left <= 200:  # When the laser moves are enough across the screen leftwards, self.left is False
            self.left = False
        if self.left:  # Moves to the left when self.left is True
            self.rect.x -= self.speed
        if not self.left:  # Moves to the right when self.left is False
            self.rect.x += self.speed
        if self.rect.left >= width:
            self.kill()  # Laser is removed when it moves offscreen


class DropperEnemy(py.sprite.Sprite):  # The dropper enemy class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = dropperEnemyImg  # Loads the image for the dropper enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(width + 100, width + 1000)  # Spawns at a position behind the screen
        self.rect.y = height - 120  # Is always at the bottom of the screen
        self.speed = 8  # Moves at 8 pixels per tick
        self.image.set_colorkey((0, 0, 0))
        self.radius = (self.rect.height // 2)  # Determines the hitbox of the enemy

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.kill()  # If they move offscreen, then they are removed from the game
        if random.random() > 0.995:
            self.dropLaser()  # A laser is fired at random

    def dropLaser(self):
        dropperEnemyLaser = DropperEnemyLaser(self.rect.centerx, self.rect.top)
        allSprites.add(dropperEnemyLaser)  # Laser is added to the relevant sprite groups
        basicEnemyWeapons.add(dropperEnemyLaser)
        enemyLaser.play()  # Plays enemy laser sound


class DropperEnemyLaser(py.sprite.Sprite):  # The dropper enemy laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = dropperEnemyLaserImg  # Loads the image for the laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial coordinates of the laser depend on the position of the enemy
        self.image.set_colorkey((0, 0, 0))
        self.speed = 10  # Moves at 10 pixels per tick

    def update(self):
        self.rect.y -= self.speed  # Laser moves vertically downwards
        if self.rect.bottom < 0:
            self.kill()  # If the laser moves beneath the screen, it is removed from the game.


class VerBeamWarning(py.sprite.Sprite):  # The vertical laser beam's warning class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(beamWarningImg, (100, 100))  # Loads the image for the warning
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width - 100)  # Warning appears at a random x coordinate
        self.rect.y = height - 100  # Warning appears at the bottom of the screen
        self.image.set_colorkey((0, 0, 0))
        self.timeOnscreen = py.time.get_ticks()
        self.timeLimit = 2000  # Amount of time laser beam stays onscreen for.

    def update(self):
        timeNow = py.time.get_ticks()
        if timeNow - self.timeOnscreen > self.timeLimit:
            self.timeOnscreen = timeNow
            self.kill()  # After 2000 ticks, the warning is removed from the game
            verLaserBeam = VerLaserBeam(self.rect.centerx)  # Vertical laser beam object is created
            allSprites.add(verLaserBeam)  # Vertical laser beam is added to the relevant sprite groups
            laserBeams.add(verLaserBeam)


class VerLaserBeam(py.sprite.Sprite):  # The vertical laser beam class
    def __init__(self, x):
        py.sprite.Sprite.__init__(self)  # Loads the image for the vertical laser beam
        self.image = py.transform.scale(verLaserBeamImg, (100, height))
        self.rect = self.image.get_rect()
        self.rect.x = x  # X coordinate depends on the x-coordinate of the warning
        self.rect.y = 0  # Always spawn at the top of the screen and goes down to the bottom
        self.timeLimit = 3000  # Laser beam appears for 3000 frames.
        self.image.set_colorkey((0, 0, 0))
        self.timeOnscreen = py.time.get_ticks()

    def update(self):
        timeNow = py.time.get_ticks()
        if timeNow - self.timeOnscreen > self.timeLimit:
            self.timeOnscreen = timeNow
            self.kill()  # After 3000 ticks, the laser beam is taken offscreen


class Boss2(py.sprite.Sprite):  # The class for the second boss
    def __init__(self):
        py.sprite.Sprite.__init__(self)  # Initialises the sprite for the boss class
        self.image = py.transform.scale(boss2Img, (120, 120))  # Loads the image for the second boss
        self.rect = self.image.get_rect()
        self.rect.x = width + 200  # Boss spawns a bit behind the screen
        self.rect.y = height // 2  # They spawn in the vertical middle of the screen
        self.image.set_colorkey((0, 0, 0))
        self.health = 60  # It takes 60 hits to defeat the boss
        self.radius = (self.rect.height // 2)  # Determines the hitbox of the second boss
        self.speed = 10
        self.beamOnscreen = False  # If this is False, a laser beam can be fired
        self.movingUp = True  # When this is True, the boss moves upwards

    def update(self):
        if self.rect.right > width - 50:
            self.rect.x -= self.speed  # Before they are onscreen they move to the left
        else:
            if self.movingUp:  # Moves upwards when this boolean is True
                self.rect.y -= self.speed
                if self.rect.top <= 0:
                    self.movingUp = False  # When they hit the top of the screen they start moving down
            if not self.movingUp:  # Moves downwards when this boolean is False
                self.rect.y += self.speed
                if self.rect.bottom >= height:
                    self.movingUp = True  # When they hit the bottom of the screen they start moving up
            if 20 < self.health <= 40:
                self.speed = 12  # Boss speeds up when their health drops to 40
            if self.health <= 20:
                self.speed = 14  # boss speeds up again when their health drop to 20
            if random.random() > 0.94:
                bossAttack = random.choice([0, 1, 2])  # Represents the three attacks that the boss can use
                if bossAttack == 0:  # Randomly-chosen attack that fires two boomerang lasers at the player
                    boomerangLaser1 = BoomerangLaser(self.rect.centerx, self.rect.top)
                    boomerangLaser2 = BoomerangLaser(self.rect.centerx, self.rect.bottom)
                    allSprites.add(boomerangLaser1,
                                   boomerangLaser2)  # The boomerang lasers are added to the relevant sprite groups
                    moderateEnemyWeapons.add(boomerangLaser1, boomerangLaser2)
                    bossLaser.play()
                if bossAttack == 1 and self.health <= 40 and not self.beamOnscreen:  # Attack for the laser beam that moves across the screen
                    self.beamOnscreen = True  # Whilst this is True no other laser beams can be onscreen
                    bossVerticalBeam = BossVerticalBeam()
                    allSprites.add(bossVerticalBeam)  # Laser beam is added to the relevant sprite groups
                    laserBeams.add(bossVerticalBeam)
                if bossAttack == 2 and self.health <= 20:
                    trackingMeteor = TrackingMeteor()
                    allSprites.add(trackingMeteor)
                    basicEnemyWeapons.add(trackingMeteor)


class BossVerticalBeam(py.sprite.Sprite):  # Class for the vertical laser beam used by the second boss
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(verLaserBeamImg, (100, round(height // 1.8)))  # Loads image for the laser beam
        self.rect = self.image.get_rect()
        self.rect.x = width + 100  # X-position is 100 pixels behind the screen
        self.rect.y = random.choice([0, height - height // 1.8])
        self.speed = 10  # Moves at a speed of 10 pixels

    def update(self):
        self.rect.x -= self.speed  # Moves leftwards across the screen
        if self.rect.right < 0:
            self.kill()  # When it moves offscreen, it is removed from the game
            boss2.beamOnscreen = False  # When it moves offscreen, another laser beam can be fired


class TrackingMeteor(py.sprite.Sprite):  # The tracking meteor class for the second bossfight
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = meteorImg[1]  # Loads the first image stored in the array storing meteors
        self.rect = self.image.get_rect()
        self.rect.x = -100  # Meteor begins offscreen on the left hand side
        if singleplayer:
            self.rect.y = player.rect.y  # Initial y-coordinate is dependant on the player's position
        if not singleplayer:  # If in multiplayer, initial y coordinate depends on either player 1 or 2's position
            if random.random() > 0.5:  # If number from 0-1>0.5 starting y-coordinate is that of player 1's
                self.rect.y = player1.rect.y
            else:  # If number from 0-1<0.5 starting y-coordinate is that of player 2's
                self.rect.y = player2.rect.y
        self.speed = 20  # Meteors move at a speed of 20 pixels per tick
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x += self.speed  # Meteors move leftwards
        if self.rect.left >= width:
            self.kill()  # Once they move offscreen, they are removed from the game


class StrongEnemy(py.sprite.Sprite):  # The strong enemy class
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(strongEnemyImg, (80, 80))  # Loads image for the strong enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(width + 100, width + 900)  # Spawns at a position behind the screen
        self.rect.y = random.randint(height // 2 - height // 3.5, height // 2 + height // 3.5)
        self.speedY = random.choice([-3, 3])  # Enemy either moves up or moves down
        self.speedX = 8  # Moves across the screen at 8 pixels per tick
        self.radius = (self.rect.height // 2)  # Determines the hitbox of the enemy
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        if random.random() > 0.99:  # If a number from 0-1 is more than 0.97, these events occur
            if self.speedY == -3:
                self.speedY = 3  # If player is moving up, they will start moving down
            elif self.speedY == 3:
                self.speedY = -3  # If player is moving down, they will start moving up
        self.rect.x -= self.speedX
        self.rect.y += self.speedY  # Whether it moves up or down is constantly changing
        if self.rect.right <= 0:
            self.kill()  # If the enemy moves offscreen, they are removed.
        if random.random() > 0.995:
            self.shoot()  # If number between 0-1 is >0.995, two lasers are shot

    def shoot(self):
        strongLaser1 = StrongLaser(self.rect.left,
                                   self.rect.centery)  # Objects of lasers are created at the top and bottom of the enemy
        allSprites.add(strongLaser1)  # The laser is added to the relevant sprite groups
        strongEnemyWeapons.add(strongLaser1)
        enemyLaser.play()  # Plays enemy laser sound


class StrongLaser(py.sprite.Sprite):  # The strong laser class
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = strongEnemyLaserImg  # Loads an image for the strong laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial coordinates depend on the strong enemy's position
        self.speed = 12  # Moves at 12 pixels per tick
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x -= self.speed  # Moves leftwards across the screen
        if self.rect.right <= 0:
            self.kill()  # If it moves offscreen on the lefthand side it is removed from the game


class Boss3(py.sprite.Sprite):  # The class for the third boss
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = py.transform.scale(boss3Img, (120, 120))  # Loads the image for the third boss
        self.rect = self.image.get_rect()
        self.rect.x = width + 200  # Boss spawns behind the screen on the right
        self.rect.y = height // 2  # Boss spawns in middle of the screen on the y-axis
        self.health = 70  # it has 70 health points
        self.speed = 12
        self.radius = (self.rect.height // 2)  # Determines the boss's hitbox
        self.image.set_colorkey((0, 0, 0))
        self.movingDown = True  # When this is True the boss moves down

    def update(self):
        if self.rect.right > width - 50:
            self.rect.x -= self.speed  # Boss will first move onscreen
        if self.movingDown:
            self.rect.y += self.speed  # Boss 3 moves downwards
            if self.rect.bottom >= height:
                self.movingDown = False  # When boss 3 hits the bottom of the screen it start moving upwards
        if not self.movingDown:
            self.rect.y -= self.speed  # Boss 3 moves upwards
            if self.rect.top <= 0:
                self.movingDown = True  # When boss 3 hits the top of the screen it start moving downwards
        if 21 <= self.health <= 45:
            self.speed = 14  # When the boss's health reaches 45, their speed increases to 14 pixels per tick
        if self.health <= 20:
            self.speed = 16  # When the boss's health reaches 20, their speed increases to 16 pixels per tick
        if random.random() > 0.97:
            boss3Attack = random.choice([0, 1, 2])  # Attack is randomly selected from whichever number is selected
            if boss3Attack == 0:  # Shoots a laser star in front of them at any point in the battle
                laserStar = LaserStar(self.rect.left, self.rect.centery)
                allSprites.add(laserStar)  # Laser star is added to the relevant sprite groups
                moderateEnemyWeapons.add(laserStar)
                bossLaser.play()
            if boss3Attack == 1 and self.health <= 45:  # Shoots a laser which tracks the player when their health is <=45
                followingLaser = FollowingLaser()
                allSprites.add(followingLaser)  # Following laser is added to the relevant sprite groups
                strongEnemyWeapons.add(followingLaser)
            if boss3Attack == 2 and self.health <= 20:  # Fires lasers from the bottom of the screen upwards when their health is <=20
                boss3Laser = Boss3Laser()
                allSprites.add(boss3Laser)  # This laser is added to the relevant sprite groups
                moderateEnemyWeapons.add(boss3Laser)
                bossLaser.play()


class FollowingLaser(py.sprite.Sprite):  # The class for the following laser
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = followingLaserImg  # Loads the image for the following laser
        self.rect = self.image.get_rect()
        self.rect.x = -100  # Initially spawns behind the screen on the left
        self.rect.y = height + 100  # Initially spawns beneath the screen
        self.image.set_colorkey((0, 0, 0))
        self.speed = 3  # Moves at 3 pixels per tick
        self.following = False
        self.followingPlayer1 = False

    def update(self):
        if singleplayer:
            if player.rect.x > self.rect.x:  # These two if statements make the laser move towards the player horizontally
                self.rect.x += max(self.speed, player.rect.x - self.rect.x)
            if player.rect.x < self.rect.x:
                self.rect.x -= max(self.speed, player.rect.x - self.rect.x)
            if player.rect.y > self.rect.y:  # These two if statements make the laser move towards the player vertically
                self.rect.y += max(self.speed, player.rect.y - self.rect.y)
            if player.rect.y < self.rect.y:
                self.rect.y -= max(self.speed, player.rect.y - self.rect.y)
        if not singleplayer:  # Laser follows either player when in multiplayer mode
            if not self.following:
                if random.random() > 0.5:  # Laser has a 50% chance of following either player 1 or 2
                    self.followingPlayer1 = True
                else:
                    self.followingPlayer1 = False
                self.following = True  # Who its following can't be changed after it is decided
            if self.followingPlayer1:
                if player1.rect.x > self.rect.x:  # These two if statements make the laser move towards player 1 horizontally
                    self.rect.x += max(self.speed, player1.rect.x - self.rect.x)
                if player1.rect.x < self.rect.x:
                    self.rect.x -= max(self.speed, player1.rect.x - self.rect.x)
                if player1.rect.y > self.rect.y:  # These two if statements make the laser move towards player 1 vertically
                    self.rect.y += max(self.speed, player1.rect.y - self.rect.y)
                if player1.rect.y < self.rect.y:
                    self.rect.y -= max(self.speed, player1.rect.y - self.rect.y)
            if not self.followingPlayer1:
                if player2.rect.x > self.rect.x:  # These two if statements make the laser move towards player 2 horizontally
                    self.rect.x += max(self.speed, player2.rect.x - self.rect.x)
                if player2.rect.x < self.rect.x:
                    self.rect.x -= max(self.speed, player2.rect.x - self.rect.x)
                if player2.rect.y > self.rect.y:  # These two if statements make the laser move towards player 2 vertically
                    self.rect.y += max(self.speed, player2.rect.y - self.rect.y)
                if player2.rect.y < self.rect.y:
                    self.rect.y -= max(self.speed, player2.rect.y - self.rect.y)


class Boss3Laser(py.sprite.Sprite):  # The class for the upwards laser fired in boss 3
    def __init__(self):
        py.sprite.Sprite.__init__(self)
        self.image = dropperEnemyLaserImg  # Loads the image for this laser
        self.rect = self.image.get_rect()
        if singleplayer:
            self.rect.x = player.rect.x  # Initial x-coordinate is that of the player's
        if not singleplayer:  # If in multiplayer, then initial x-coordinate is either player 1's or 2's
            if random.random() > 0.5:  # Has a 50% chance of its x-coordinate being player 1's or 2's
                self.rect.x = player1.rect.x
            else:
                self.rect.x = player2.rect.x
        self.rect.y = height + 50  # Spawns beneath the screen
        self.image.set_colorkey((0, 0, 0))
        self.speed = 20  # Moves at 10 pixels per tick

    def update(self):
        self.rect.y -= self.speed  # Laser moves vertically downwards
        if self.rect.bottom < 0:
            self.kill()  # If the laser moves beneath the screen, it is removed from the game.


class LaserStar(py.sprite.Sprite):  # The class for the laser star boss attack
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = laserStarImg  # Loads the image for the laser star
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial coordinates depend on those for the position of the player
        self.image.set_colorkey((0, 0, 0))
        self.speed = 10  # Moves at a speed of 10 pixels per tick

    def update(self):
        self.rect.x -= self.speed  # Moves leftwards across the screen
        if 0 < self.rect.x < width // 1.33:
            if random.random() > 0.98:
                self.kill()  # When it is removed, it splits into four lasers
                laserUp = LaserUp(self.rect.centerx,
                                  self.rect.top)  # Initial positions of the lasers depend on that of the laser star
                laserDown = LaserDown(self.rect.centerx, self.rect.bottom)
                laserLeft = LaserLeft(self.rect.left, self.rect.centery)
                laserRight = LaserRight(self.rect.right, self.rect.centery)
                # Lasers moving in four directions are added to the relevant sprite groups
                allSprites.add(laserUp, laserDown, laserLeft, laserRight)
                moderateEnemyWeapons.add(laserUp, laserDown, laserLeft, laserRight)
        if self.rect.right <= 0:
            self.kill()  # If the laser moves offscreen it is removed from the game


class LaserUp(py.sprite.Sprite):  # The class for the laser fired upwards from the laser star
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = fourLasersImg[0]  # Loads the images for the upwards laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial spawn depends on the laser star's coordinates
        self.speed = 15  # Moves at 15 pixels per tick
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.y -= self.speed  # Laser will move upwards
        if self.rect.bottom <= 0:
            self.kill()  # The laser is removed from the game when it goes above the screen


class LaserDown(py.sprite.Sprite):  # The class for the laser fired downwards from the laser star
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = fourLasersImg[1]  # Loads the image for the rightwards laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial spawn depends on the laser star's coordinates
        self.speed = 15
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.y += self.speed  # Laser will move downwards
        if self.rect.top >= height:
            self.kill()  # Laser is removed when it goes offscreen by going beneath it


class LaserLeft(py.sprite.Sprite):  # The class for the laser fired leftwards from the laser star
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = fourLasersImg[2]  # Loads the image for the leftwards laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial spawn depends on the laser star's coordinates
        self.speed = 15
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x -= self.speed  # Laser will move to the left
        if self.rect.right <= 0:
            self.kill()  # Leftwards laser is removed when it moves offscreen


class LaserRight(py.sprite.Sprite):  # The class for the laser fired rightwards from the laser star
    def __init__(self, x, y):
        py.sprite.Sprite.__init__(self)
        self.image = fourLasersImg[3]  # Loads the image for the rightwards laser
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)  # Initial spawn depends on the laser star's coordinates
        self.speed = 15
        self.image.set_colorkey((0, 0, 0))

    def update(self):
        self.rect.x += self.speed  # Laser will move to the right
        if self.rect.left >= width:
            self.kill()  # Rightwards laser is removed when it moves offscreen


# This part contains all of the main code.
runGame = True  # This is always True otherwise the game will stop working.
gameOver = True  # This starts off as True so the program can set up the start of the game whenever the player loads it up.
clock = py.time.Clock()


def makeBasicEnemies():  # Sub-routine for creating basic enemies.
    basicEnemy = BasicEnemy()
    allSprites.add(basicEnemy)  # Enemy object added to the relevant sprite groups
    basicEnemies.add(basicEnemy)


def makeModerateEnemies():  # Sub-routine for creating moderate enemies.
    moderateEnemy = ModerateEnemy()
    allSprites.add(moderateEnemy)  # Enemy is added to the revelant sprite groups
    basicEnemies.add(moderateEnemy)


def makeDropperEnemies():  # Sub-routine for creating dropper enemies.
    dropperEnemy = DropperEnemy()
    allSprites.add(dropperEnemy)  # Enemy object is added to relevant sprite groups
    basicEnemies.add(dropperEnemy)


def makeStrongEnemies():  # Sub-routine for making strong enemies
    strongEnemy = StrongEnemy()
    allSprites.add(strongEnemy)  # Strong enemy is added to the relevant sprite groups
    basicEnemies.add(strongEnemy)


joysticks = []  # List for all of the recognised controllers
for i in range(py.joystick.get_count()):  # Puts all recognised controllers in a list
    joysticks.append(py.joystick.Joystick(i))
    joysticks[-1].init()  # Initialises all of the recognised controllers


def mainMenu():  # Sub-routine for the main menu
    menuFps = 60
    singleplayer = True  # Determines whether the game is singleplayer or multiplayer
    tooShort = False  # Becomes True if name entered is less than 4 characters
    win.blit(bgBlue, (0, 0))  # Draws a background image for the main menu
    titleFont = py.font.SysFont("papyrus", width // 30)  # Chooses the font and font size for the title
    menuFont = py.font.SysFont("papyrus", width // 40)  # Chooses the font and font size for the rest of the text.
    returnFont = py.font.SysFont("papyrus", width // 48)  # Chooses the font and font size for return to menu text
    title = titleFont.render("2D Wave-based Shooter!", 1, (255, 255, 255))  # Game title
    startTitle = menuFont.render("Start Game", 1, (0, 0, 0))  # Titles for all the sections of the main menu
    optionsTitle = menuFont.render("Singleplayer Mode", 1, (0, 0, 0))
    tutorialTitle = menuFont.render("How To Play", 1, (0, 0, 0))
    controlsTitle = menuFont.render("Singleplayer Controls", 1, (0, 0, 0))
    leaderboardTitle = returnFont.render("Singleplayer Leaderboard", 1, (0, 0, 0))  # Text for going back to the menu
    backToMenu = returnFont.render("Press z to return to the starting menu.", 1, (255, 0, 0))
    username = ""
    win.blit(title, (width // 2 - width // 5, 100))  # Draws the game title onscreen.
    py.draw.rect(win, (0, 255, 0), (width // 2 - width // 8, height - 200, width // 4, 100))
    win.blit(startTitle, (width // 2 - width // 15, height - 175))  # Draws box and text for the start title
    py.draw.rect(win, (0, 255, 0), (25, 100, width // 4, 100))
    win.blit(controlsTitle, (30, 130))  # Draws box and text for the controls title
    py.draw.rect(win, (0, 255, 0), (25, height - 200, width // 4, 100))
    win.blit(tutorialTitle, (60, height - 170))  # Draws box and text for the tutorial title
    py.draw.rect(win, (0, 255, 0), (width - width // 3.5, 100, width // 4, 100))
    win.blit(optionsTitle, (width - width // 3.75, 130))  # Draws box and text for the options title
    py.draw.rect(win, (0, 255, 0), (width - width // 3.5, height - 200, width // 4, 100))
    win.blit(leaderboardTitle, (width - width // 4, height - 175))  # Draws box and text for the leaderboard title
    gameStart = False  # While this is False the game won't start
    mainSection = True  # Booleans for the different section of the main menu
    controlsSection = False
    tutorialSection = False
    optionsSection = False
    leaderboardSection = False
    startSection = False
    controllerControlsSection = False
    while not gameStart:
        clock.tick(menuFps)
        mouse = py.mouse.get_pos()  # Allows mouse coordinates to be taken
        if singleplayer:  # The options box tells you if the game is in single or multiplayer
            optionsTitle = menuFont.render("Singleplayer Mode", 1, (0, 0, 0))
            controlsTitle = menuFont.render("Singleplayer Controls", 1, (0, 0, 0))
            leaderboardTitle = returnFont.render("Singleplayer Leaderboard", 1, (0, 0, 0))
        elif not singleplayer:  # These titles are rewritten when in multiplayer
            optionsTitle = menuFont.render("Multiplayer Mode", 1, (0, 0, 0))
            controlsTitle = menuFont.render("Multiplayer Controls", 1, (0, 0, 0))
            leaderboardTitle = returnFont.render("Multiplayer Leaderboard", 1, (0, 0, 0))

        if mainSection:
            win.blit(bgBlue, (0, 0))
            win.blit(title, (width // 2 - width // 5, 100))
            if width // 2 - width // 8 < mouse[0] < width // 2 - width // 8 + width // 4 and height - 200 < mouse[
                1] < height - 100:
                py.draw.rect(win, (255, 0, 0), (width // 2 - width // 8, height - 200, width // 4, 100))
                win.blit(startTitle,
                         (width // 2 - width // 15, height - 175))  # Box turns red when a mouse hovers over it.
            if width // 2 - width // 8 > mouse[0] or mouse[0] > width // 2 - width // 8 + width // 4 or height - 200 > \
                    mouse[1] or mouse[1] > height - 100:
                py.draw.rect(win, (0, 255, 0), (width // 2 - width // 8, height - 200, width // 4, 100))
                win.blit(startTitle, (
                    width // 2 - width // 15, height - 175))  # Box turns back to green when the mouse goes off it.
            if 25 < mouse[0] < 25 + width // 4 and 100 < mouse[1] < 200:
                py.draw.rect(win, (255, 0, 0),
                             (25, 100, width // 4, 100))  # Controls box turns red when a mouse hovers over it
                win.blit(controlsTitle, (30, 130))
            if mouse[0] < 25 or mouse[0] > 25 + width // 4 or mouse[1] < 100 or mouse[1] > 200:
                py.draw.rect(win, (0, 255, 0),
                             (25, 100, width // 4, 100))  # Box turns back to green when the mouse goes off it
                win.blit(controlsTitle, (30, 130))
            if 25 < mouse[0] < 25 + width // 4 and height - 200 < mouse[1] < height - 100:
                py.draw.rect(win, (255, 0, 0),
                             (25, height - 200, width // 4, 100))  # Tutorial box turns when a mouse hovers over it
                win.blit(tutorialTitle, (50, height - 170))
            if mouse[0] < 25 or mouse[0] > 25 + width // 4 or mouse[1] < height - 200 or mouse[1] > height - 100:
                py.draw.rect(win, (0, 255, 0),
                             (25, height - 200, width // 4, 100))  # Box turns back to green when the mouse goes off it
                win.blit(tutorialTitle, (50, height - 170))
            if width - width // 3.5 < mouse[0] < width - width // 3.5 + width // 4 and 100 < mouse[1] < 200:
                py.draw.rect(win, (255, 0, 0), (
                width - width // 3.5, 100, width // 4, 100))  # Options box turns red when a mouse hovers over it
                win.blit(optionsTitle, (width - width // 3.75, 130))
            if mouse[0] < width - width // 3.5 or mouse[0] > width - width // 3.5 + width // 4 or mouse[1] < 100 or \
                    mouse[1] > 200:
                py.draw.rect(win, (0, 255, 0), (
                width - width // 3.5, 100, width // 4, 100))  # Box turns back to green when the mouse goes off it
                win.blit(optionsTitle, (width - width // 3.75, 130))
            if width - width // 3.5 < mouse[0] < width - width // 3.5 + width // 4 and height - 200 < mouse[
                1] < height - 100:
                py.draw.rect(win, (255, 0, 0), (width - width // 3.5, height - 200, width // 4,
                                                100))  # Leaderboard box turns red when a mouse hovers over it
                win.blit(leaderboardTitle, (width - width // 3.6, height - 175))
            if mouse[0] < width - width // 3.5 or mouse[0] > width - width // 3.5 + width // 4 or mouse[
                1] < height - 200 or mouse[1] > height - 100:
                py.draw.rect(win, (0, 255, 0), (width - width // 3.5, height - 200, width // 4, 100))
                win.blit(leaderboardTitle,
                         (width - width // 3.6, height - 175))  # Box turns back to green when the mouse goes off it
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.MOUSEBUTTONDOWN:  # These events occur if the mouse button is pressed down
                    if width // 2 - width // 8 < mouse[0] < width // 2 - width // 8 + width // 4 and height - 200 < \
                            mouse[1] < height - 100:
                        section.play()  # Plays a sound effect when they switch sections
                        startSection = True  # When they click on the start section they are taken to an input box
                        mainSection = False
                    if 25 < mouse[0] < 25 + width // 4 and 100 < mouse[
                        1] < 200:  # When the click the controls box they are taken there.
                        section.play()  # Plays a sound effect when they switch sections
                        controlsSection = True
                        mainSection = False
                    if 25 < mouse[0] < 25 + width // 4 and height - 200 < mouse[
                        1] < height - 100:  # When they click tutorial they are taken there
                        section.play()  # Plays a sound effect when they switch sections
                        tutorialSection = True
                        mainSection = False
                    if width - width // 3.5 < mouse[0] < width - width // 3.5 + width // 4 and 100 < mouse[
                        1] < 200:  # Clicking this box toggles between singleplayer and multiplayer
                        if singleplayer:
                            singleplayer = False
                        else:
                            singleplayer = True
                        gamemode.play()  # Plays a different sound effect when they toggle between single and multiplayer
                    if width - width // 3.5 < mouse[0] < width - width // 3.5 + width // 4 and height - 200 < mouse[
                        1] < height - 100:  # When they click leaderboard they are taken there
                        section.play()  # Plays a sound effect when they switch sections
                        leaderboardSection = True
                        mainSection = False

        if startSection:
            win.blit(bgBlue, (0, 0))  # Draws the background onscreen again
            usernameOnscreen = menuFont.render(username, 1, (255, 255, 255))
            shortName = menuFont.render("The name entered is too short.", 1, (255, 255, 255))
            if singleplayer:  # Player name is entered if in singleplayer
                userInputText = menuFont.render("Enter a player name between 4 and 10 characters.", 1, (255, 255, 255))
            if not singleplayer:  # Team name is entered if in multiplayer
                userInputText = menuFont.render("Enter a team name between 4 and 10 characters.", 1, (255, 255, 255))
            if tooShort:  # Tells the player there name is too short when tooShort is True
                win.blit(shortName, (width // 2 - width // 4, height // 2 + 200))
            win.blit(usernameOnscreen, (width // 2 - width // 4, height // 2))  # Draws the player's name onscreen
            win.blit(userInputText, (width // 2 - width // 4, height // 2 - 200))
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.KEYDOWN:
                    if event.key == py.K_BACKSPACE:  # Pressing backspace removes one of the characters from the username
                        username = username[:-1]
                    elif event.key == py.K_RETURN and 4 <= len(username) <= 10:
                        return username, singleplayer
                        gameStart = True  # If the user pressed enter then the game begins
                    elif event.key == py.K_RETURN and len(username) < 4:
                        tooShort = True  # Becomes True when the name is less than 4 characters
                    else:
                        if (97 <= event.key <= 122 or 48 <= event.key <= 57) and len(
                                username) < 10:  # Characters can only be letters of the alphabet or numbers
                            username += event.unicode  # Each key the user presses is drawn onscreen

        if controlsSection:
            win.blit(bgBlue, (0, 0))  # Draws the background again
            controlsSectionTitle = titleFont.render("Controls", 1, (255, 255, 255))  # Title of the section
            controllerControls = menuFont.render("Controller controls", 1, (0, 0, 0))  # section for controller controls
            if singleplayer:
                controlsText1 = menuFont.render("Use the up, down, left and right keys to move.", 1,
                                                (255, 255, 255))  # Writes the singleplayer controls
                controlsText2 = menuFont.render("Press left shift to dash in the direction you are moving in.", 1,
                                                (255, 255, 255))
                controlsText3 = menuFont.render("Press z is shoot lasers and x to drop bombs.", 1, (255, 255, 255))
                controlsText4 = menuFont.render("Player lasers have an ammo limit, but bombs don't.", 1,
                                                (255, 255, 255))
                controlsText5 = menuFont.render("Avoid enemy weapons whilst shooting at them.", 1, (255, 255, 255))
            if not singleplayer:
                controlsText1 = menuFont.render("Use the up, down, left and right keys to move player 1.", 1,
                                                (255, 255, 255))  # Writes the multiplayer controls
                controlsText2 = menuFont.render("Use full stop to fire lasers and slash to drop bombs for player 1.", 1,
                                                (255, 255, 255))
                controlsText3 = menuFont.render("Use W, S, A and D to move player 2.", 1, (255, 255, 255))
                controlsText4 = menuFont.render("Use C to fire lasers and V to drop bombs for player 2.", 1,
                                                (255, 255, 255))
                controlsText5 = menuFont.render(
                    "Use right shift to make player 1 dash and left shift to make player 2 dash.", 1, (255, 255, 255))
            win.blit(backToMenu, (50, 25))  # Draws an option to return to the main menu and a box around it.
            win.blit(controlsSectionTitle, (width // 2 - width // 10, 100))  # Draws the title onscreen.
            win.blit(controlsText1, (50, 200))  # Draws the controls onscreen
            win.blit(controlsText2, (50, 300))
            win.blit(controlsText3, (50, 400))
            win.blit(controlsText4, (50, 500))
            win.blit(controlsText5, (50, 600))
            if mouse[0] < width // 2 + width // 4.2 or mouse[0] > width // 2 + width // 4.2 + width // 4 or mouse[
                1] < 0 or mouse[1] > 100:
                py.draw.rect(win, (0, 255, 0), (width // 2 + width // 4.2, 0, width // 4, 100))
                win.blit(controllerControls,
                         (width // 2 + width // 4, 25))  # Box is green when mouse isn't hovering over it
            else:
                py.draw.rect(win, (255, 0, 0), (width // 2 + width // 4.2, 0, width // 4, 100))
                win.blit(controllerControls, (width // 2 + width // 4, 25))  # Bos turns red when mouse hovers over it
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.KEYDOWN:
                    if event.key == py.K_z:  # When z is pressed, you return to the starting menu.
                        mainSection = True
                        controlsSection = False
                if event.type == py.MOUSEBUTTONDOWN:
                    if width // 2 + width // 4.2 < mouse[0] < width // 2 + width // 4.2 + width // 4 and 0 < mouse[
                        1] < 100:
                        section.play()  # Plays a sound effect when they switch sections
                        controlsSection = False  # When you click on controller controls it takes you to another section
                        controllerControlsSection = True

        if controllerControlsSection:
            win.blit(bgBlue, (0, 0))  # Draws the background again
            controllerSectionTitle = titleFont.render("Controller Controls", 1, (255, 255, 255))  # Title of the section
            controllerControlsText1 = menuFont.render("Use up, down, left and right on the d-pad to move.", 1,
                                                      (255, 255, 255))  # Writes the controller controls
            controllerControlsText2 = menuFont.render("Use L1 or LB to dash in the direction you are moving.", 1,
                                                      (255, 255, 255))
            controllerControlsText3 = menuFont.render("Use circle or B to fire lasers.", 1, (255, 255, 255))
            controllerControlsText4 = menuFont.render("Use triangle or Y to drop bombs.", 1, (255, 255, 255))
            controllerControlsText5 = menuFont.render("In multiplayer, the controller is used by player 1.", 1,
                                                      (255, 255, 255))
            keyboardControls = menuFont.render("Keyboard Controls", 1,
                                               (0, 0, 0))  # Section to go back to the keyboard controls
            win.blit(backToMenu, (50, 25))  # Draws an option to return to the main menu and a box around it.
            win.blit(controllerSectionTitle, (width // 2 - width // 7, 100))  # Draws the title onscreen
            win.blit(controllerControlsText1, (50, 200))  # Draw the controller controls onscreen
            win.blit(controllerControlsText2, (50, 300))
            win.blit(controllerControlsText3, (50, 400))
            win.blit(controllerControlsText4, (50, 500))
            win.blit(controllerControlsText5, (50, 600))
            if mouse[0] < width // 2 + width // 4.2 or mouse[0] > width // 2 + width // 4.2 + width // 4 or mouse[
                1] < 0 or mouse[1] > 100:
                py.draw.rect(win, (0, 255, 0), (width // 2 + width // 4.2, 0, width // 4, 100))
                win.blit(keyboardControls,
                         (width // 2 + width // 4, 25))  # Box is green when mouse isn't hovering over it
            else:
                py.draw.rect(win, (255, 0, 0), (width // 2 + width // 4.2, 0, width // 4, 100))
                win.blit(keyboardControls, (width // 2 + width // 4, 25))  # Bos turns red when mouse hovers over it
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.KEYDOWN:
                    if event.key == py.K_z:  # When z is pressed, you return to the starting menu.
                        mainSection = True
                        controllerControlsSection = False  # Controller controls section becomes False
                if event.type == py.MOUSEBUTTONDOWN:
                    if width // 2 + width // 4.2 < mouse[0] < width // 2 + width // 4.2 + width // 4 and 0 < mouse[
                        1] < 100:
                        section.play()  # Plays a sound effect when they switch sections
                        controlsSection = True  # When the box is pressed you return the regular controls section
                        controllerControlsSection = False

        if tutorialSection:
            tutorialFont = py.font.SysFont("papyrus", width // 50)
            win.blit(bgBlue, (0, 0))  # Draws the background again
            tutorialSectionTitle = titleFont.render("How to Play", 1, (255, 255, 255))  # Title of the tutorial section
            tutorialText1 = tutorialFont.render("The aim of the game is to shoot at waves of enemies to get points.", 1,
                                                (255, 255, 255))  # Writes the different lines for the tutorial
            tutorialText2 = tutorialFont.render("Different enemies will drop a different number of points.", 1,
                                                (255, 255, 255))
            tutorialText3 = tutorialFont.render("Enemies will shoot back at the player as well.", 1,
                                                (255, 255, 255))  # These inform the player what they do in the game.
            tutorialText4 = tutorialFont.render("Getting hit by enemy weapons makes you lose health.", 1,
                                                (255, 255, 255))
            tutorialText5 = tutorialFont.render("But enemy lasers can be counterracted by your own weapons.", 1,
                                                (255, 255, 255))
            tutorialText6 = tutorialFont.render("Overtime, the waves will have more enemies and introduce harder ones.",
                                                1, (255, 255, 255))
            tutorialText7 = tutorialFont.render(
                "After some waves, you will fight a boss, who has multiple attacks and a lot more health.", 1,
                (255, 255, 255))
            tutorialText8 = tutorialFont.render("You will avoid enemy attacks by moving around them and dashing.", 1,
                                                (255, 255, 255))
            tutorialText9 = tutorialFont.render("The dash has a short cooldown, so time dashes well.", 1,
                                                (255, 255, 255))
            win.blit(backToMenu, (50, 25))  # Draws an option to return to the main menu and a box around it.
            win.blit(tutorialSectionTitle, (width // 2 - width // 10, 100))  # Draws the tutorial title onscreen.
            win.blit(tutorialText1, (50, 200))  # Draws the tutorial instructions onscreen.
            win.blit(tutorialText2, (50, 250))  # Lines of text are written beneath each-other
            win.blit(tutorialText3, (50, 300))
            win.blit(tutorialText4, (50, 350))
            win.blit(tutorialText5, (50, 400))
            win.blit(tutorialText6, (50, 450))
            win.blit(tutorialText7, (50, 500))
            win.blit(tutorialText8, (50, 550))
            win.blit(tutorialText9, (50, 600))
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.KEYDOWN:
                    if event.key == py.K_z:  # When z is pressed, you return to the starting menu.
                        mainSection = True
                        tutorialSection = False  # Tutorial section becomes False

        if leaderboardSection:
            scores = []  # Lists for the scores and players read from the files
            players = []
            scorePlayerList = [[]]  # List for a 2D array of scores and corresponding players
            if singleplayer:  # Separate lists if the game is in singleplayer or multiplayer
                scoreFile = open("scores.txt", "r")
                for x in scoreFile:  # Appends all scores in the file into the same list
                    scores.append(x.rstrip("\n"))  # Removes the \n from each score
                scoreFile.close()
                nameFile = open("names.txt", "r")
                for y in nameFile:  # Appends all usernames in the files into the same list
                    players.append(y.rstrip("\n"))  # Removes the \n from each player name
                nameFile.close()  # Both files are closed after being read from
            if not singleplayer:
                scoreFile = open("scoresMultiplayer.txt", "r")
                for x in scoreFile:  # Appends all scores in the files into the same list
                    scores.append(x.strip("\n"))  # Removes the \n from the scores
                scoreFile.close()
                nameFile = open("namesMultiplayer.txt.", "r")
                for y in nameFile:  # Appends all team names into the same list
                    players.append(y.strip("\n"))  # Removes the \n from the team names
                nameFile.close()  # Both files are closed after being used
            for z in range(len(scores)):
                scorePlayerList.append(
                    [players[z], scores[z]])  # Appends corresponding names and scores into a 2d array
            scorePlayerList = list(filter(None, scorePlayerList))
            scoreSwap = True
            while scoreSwap:  # Bubble sort to order the list in descending order
                scoreSwap = False  # If no swaps occur in a pass, then the sort ends.
                for n in range(1, len(scorePlayerList)):
                    if int(scorePlayerList[n][1]) > int(scorePlayerList[n - 1][
                                                            1]):  # This happens the score in the next index is bigger than the score in the previous one
                        tempSmallerPlayer = scorePlayerList[n - 1][
                            0]  # The score and name of the previous index are temporarily stored in variables
                        tempSmallerScore = scorePlayerList[n - 1][1]
                        scorePlayerList[n - 1][0] = scorePlayerList[n][
                            0]  # The name and score the next index are stored in the previous index.
                        scorePlayerList[n - 1][1] = scorePlayerList[n][1]
                        scorePlayerList[n][
                            0] = tempSmallerPlayer  # The variables storing the previous name and score are stored in the next index
                        scorePlayerList[n][1] = tempSmallerScore
                        scoreSwap = True  # A swap has occurred, the sort won't end after this pass
            if singleplayer:
                leaderboardSectionTitle = titleFont.render("Singleplayer Leaderboard", 1, (
                255, 255, 255))  # Title of the leaderboard section if in singleplayer
            if not singleplayer:
                leaderboardSectionTitle = titleFont.render("Multiplayer Leaderboard", 1, (
                255, 255, 255))  # Title of the leaderboard section if in multiplayer
            win.blit(bgBlue, (0, 0))  # Redraws the background for the main menu
            win.blit(leaderboardSectionTitle, (width // 2 - width // 5, 100))  # Draws the leaderboard title onscreen
            win.blit(backToMenu, (50, 25))  # Draws the back to menu statement onscreen.
            if len(scorePlayerList) > 5:
                for x in range(0, 5):  # The top five scores are displayed on the leaderboard
                    nameRank = menuFont.render(str(x + 1) + ") " + str(scorePlayerList[x][0]), 1, (255, 255, 255))
                    scoreRank = menuFont.render(scorePlayerList[x][1], 1, (
                    255, 255, 255))  # Each of the top five names and scores are continously drawn onscreen
                    leaderboardY = 200 + (
                            x * 100)  # Each of the players are drawn beneath each-other in descending order of score
                    win.blit(nameRank, (50, leaderboardY))  # Names and scores are drawn onscreen
                    win.blit(scoreRank, (width // 2, leaderboardY))
            if len(scorePlayerList) <= 5:  # All of the scores are displayed on the leaderboard when there are 5 or less.
                for x in range(0, len(scorePlayerList)):
                    nameRank = menuFont.render(str(x + 1) + ") " + str(scorePlayerList[x][0]), 1, (255, 255, 255))
                    scoreRank = menuFont.render(scorePlayerList[x][1], 1, (
                    255, 255, 255))  # Each of the names and scores are continously drawn onscreen
                    leaderboardY = 200 + (
                            x * 100)  # Each of the players are drawn beneath each-other in descending order of score
                    win.blit(nameRank, (50, leaderboardY))  # Names and scores are drawn onscreen
                    win.blit(scoreRank, (width // 2, leaderboardY))
            for event in py.event.get():
                if event.type == py.QUIT:
                    py.quit()  # If the user clicks the cross, they exit the game.
                if event.type == py.KEYDOWN:
                    if event.key == py.K_z:  # When z is pressed, you return to the starting menu.
                        mainSection = True
                        leaderboardSection = False  # Leaderboard section becomes False
        py.display.update()  # Updates the display whenever the sub-routine is called


def drawScreen(singleplayer):
    if phase1:  # Background is blue in first phase
        win.blit(bgBlue, (backgroundX, 0))
        win.blit(bgBlue, (backgroundX2, 0))
    if phase2:  # Background is dark purple in second phase
        win.blit(bgDarkPurple, (backgroundX, 0))
        win.blit(bgDarkPurple, (backgroundX2, 0))
    if phase3:  # Background is purple after the second boss
        win.blit(bgPurple, (backgroundX, 0))
        win.blit(bgPurple, (backgroundX2, 0))
    allSprites.draw(win)  # These two lines draw the sprites and background onto the screen.
    mainFont = py.font.SysFont("papyrus", 50)  # Creates a font to use ingame.
    playerScore = mainFont.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(playerScore, (width - 300, 50))  # Puts the current player's score onscreen.
    if singleplayer:
        ammoRemaining = mainFont.render("Ammo: " + str(player.ammo), 1, (255, 255, 255))
        win.blit(ammoRemaining, (50, 50))  # Puts the amount of ammo the player has left onscreen.
        if not player.health <= 0:  # Draws a healthbar for the player underneath their spaceship
            py.draw.rect(win, (255, 0, 0), (
                player.rect.x, player.rect.y + playerShipImg.get_height() - 25, playerShipImg.get_width(), 10))
            py.draw.rect(win, (0, 255, 0), (player.rect.x, player.rect.y + playerShipImg.get_height() - 25,
                                            playerShipImg.get_width() * (player.health / player.maxHealth), 10))
    if not singleplayer:
        ammoRemaining1 = mainFont.render("Player 1 Ammo: " + str(player1.ammo), 1, (255, 255, 255))
        ammoRemaining2 = mainFont.render("Player 2 Ammo: " + str(player2.ammo), 1, (255, 255, 255))
        win.blit(ammoRemaining1, (50, 50))  # Puts the amount of ammo player 1 has left onscreen.
        win.blit(ammoRemaining2, (50, 150))  # Puts the amount of ammo player 2 has left onscreen.
        if not player1.health <= 0:  # Draws a healthbar for player 1 underneath their spaceship
            py.draw.rect(win, (255, 0, 0), (
                player1.rect.x, player1.rect.y + playerShipImg.get_height() - 25, playerShipImg.get_width(), 10))
            py.draw.rect(win, (0, 255, 0), (player1.rect.x, player1.rect.y + playerShipImg.get_height() - 25,
                                            playerShipImg.get_width() * (player1.health / player1.maxHealth), 10))
        if not player2.health <= 0:  # Draws a healthbar for the player 2 underneath their spaceship
            py.draw.rect(win, (255, 0, 0), (
                player2.rect.x, player2.rect.y + player2ShipImg.get_height() + 5, player2ShipImg.get_width(), 10))
            py.draw.rect(win, (0, 255, 0), (player2.rect.x, player2.rect.y + player2ShipImg.get_height() + 5,
                                            player2ShipImg.get_width() * (player2.health / player2.maxHealth), 10))
    py.display.update()
    allSprites.update()  # These two lines update the screen and sprites whenever this subroutine is called.


while runGame:
    if gameOver:  # These are the processes the game goes through before starting up.
        username, singleplayer = mainMenu()
        gameOver = False
        startHazards = False  # When this is True laser beams and meteors start dropping
        startVerticalLaserBeam = False
        moderateEnemiesSpawn = False  # When the next two are True, new enemies start spawning
        dropperEnemiesSpawn = False
        verLaserBeamSpawn = False
        allBossesDone = False  # Becomes True after all bosses are defeated
        bossSpawn = False
        phase1 = True
        phase2 = False
        phase3 = False
        playerShoot = False
        playerDrop = False
        playerRight = False
        playerLeft = False
        playerUp = False
        playerDown = False
        playerDash = False
        allSprites = py.sprite.Group()  # Creation of the different sprites groups.
        playerWeapons = py.sprite.Group()
        basicEnemies = py.sprite.Group()
        basicEnemyWeapons = py.sprite.Group()
        moderateEnemyWeapons = py.sprite.Group()
        strongEnemyWeapons = py.sprite.Group()
        Meteors = py.sprite.Group()
        powerups = py.sprite.Group()
        laserBeams = py.sprite.Group()
        bosses = py.sprite.Group()
        if singleplayer:
            player = Player()  # Only one player is in the game
            allSprites.add(player)
        if not singleplayer:
            player1 = Player1()  # Two players are in the game
            player2 = Player2()
            allSprites.add(player1, player2)
        boss1 = Boss1()  # Creates objects of the different bosses
        boss2 = Boss2()
        boss3 = Boss3()
        fps = 60  # Number of frames per second the game runs at
        backgroundX = 0
        backgroundX2 = width
        noBasicEnemies = 15  # Game starts with 15 enemies.
        noModerateEnemies = 10
        noDropperEnemies = 20
        noStrongEnemies = 35
        py.time.set_timer(py.USEREVENT + 0, 10000)  # Events that repeat after a certain number of ticks
        py.time.set_timer(py.USEREVENT + 1, 20000)
        py.time.set_timer(py.USEREVENT + 2, 300)
        py.time.set_timer(py.USEREVENT + 3, 7500)
        py.time.set_timer(py.USEREVENT + 4, 40000)
        py.time.set_timer(py.USEREVENT + 5, 60000)
        score = 0
        py.mixer.music.set_volume(0.5)  # Starts the music
        py.mixer.music.play(-1)
        for i in range(noBasicEnemies):  # Creates 15 enemies at the start of the game
            makeBasicEnemies()
    drawScreen(singleplayer)  # This subroutine is constantly being called, so the screen is always being updated.
    backgroundX -= 4  # The two backgrounds are constantly sliding to the left.
    backgroundX2 -= 4
    if backgroundX < bgBlue.get_width() * -1:  # When the end of the background reaches the start of the screen
        # the its position is reset so its start is now at the screen's end.
        backgroundX = bgBlue.get_width()
    if backgroundX2 < bgBlue.get_width() * -1:
        backgroundX2 = bgBlue.get_width()
    if singleplayer:  # Controls controller input in singleplayer
        if playerShoot:
            player.shoot()  # Calls the method for shooting lasers
        if playerDrop:
            player.drop()  # Calls the method for dropping bombs
        if playerRight and player.rect.right <= width - 10:  # Moves the player right when True
            player.rect.x += player.speed
        if playerLeft and player.rect.left >= 10:  # Moves the player left when True
            player.rect.x -= player.speed
        if playerUp and player.rect.top >= 10:  # Moves the player up when True
            player.rect.y -= player.speed
        if playerDown and player.rect.bottom <= height - 25:  # Moves the player up when True
            player.rect.y += player.speed
    if not singleplayer:
        if playerShoot:
            player1.shoot()  # Calls the method for shooting lasers
        if playerDrop:
            player1.drop()  # Calls the method for dropping bombs
        if playerRight and player1.rect.right <= width - 10:  # Moves the player right when True
            player1.rect.x += player1.speed
        if playerLeft and player1.rect.left >= 10:  # Moves the player left when True
            player1.rect.x -= player1.speed
        if playerUp and player1.rect.top >= 10:  # Moves the player up when True
            player1.rect.y -= player1.speed
        if playerDown and player1.rect.bottom <= height - 25:  # Moves the player up when True
            player1.rect.y += player1.speed

    # This for loop goes through the different events that can happen whilst the game is being ran.
    for event in py.event.get():
        if event.type == py.QUIT:  # If the player presses the x in the corner they will quit the game.
            py.quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_LSHIFT:  # When the left shift key is pressed down the program calls the dash method.
                if singleplayer:
                    player.dash()  # A method from the player class.
                else:
                    player2.dash()  # When the left shift is pressed and game is multiplayer, player 2 dashes
            if event.key == py.K_RSHIFT:
                if not singleplayer:
                    player1.dash()  # When the right shift is pressed and game is multiplayer, player 1 dashes
        # Events for controller input
        if event.type == py.JOYBUTTONDOWN:
            if event.button == 2:
                playerShoot = True  # Pressing square or circle on ps4 controller shoots lasers
            if event.button == 3:
                playerDrop = True  # Pressing triangle on ps4 controller drops bombs
            if event.button == 5:  # Pressing R1 makes the player dash
                if singleplayer:
                    player.dash()
                if not singleplayer:
                    player1.dash()  # In multiplayer, player 1 dashes
        if event.type == py.JOYBUTTONUP:
            if event.button == 2:
                playerShoot = False  # Letting go of square or circle on ps4 controller ends the laser shooting
            if event.button == 3:
                playerDrop = False  # Letting go of triangle on ps4 controller ends the bomb dropping
        if event.type == py.JOYHATMOTION:
            if event.value[0] == 1:  # Pressing right on the d-pad makes the player move right
                playerRight = True
                playerLeft = False
                if singleplayer:
                    player.right = True  # Player dashes right when L1 is pressed
                    player.left = False
                    player.up = False
                    player.down = False
                if not singleplayer:
                    player1.right = True  # Player 1 dashes right when L1 is pressed
                    player1.left = False
                    player1.up = False
                    player1.down = False
            if event.value[0] == -1:  # Pressing left on the d-pad makes the player move left
                playerLeft = True
                playerRight = False
                if singleplayer:
                    player.right = False
                    player.left = True  # Player dashes left when L1 is pressed
                    player.up = False
                    player.down = False
                if not singleplayer:
                    player1.right = False
                    player1.left = True  # Player 1 dashes left when L1 is pressed
                    player1.up = False
                    player1.down = False
            if event.value[0] == 0:  # Not pressing either makes the player stationary on the x-axis
                playerLeft = False
                playerRight = False
            if event.value[1] == 1:  # Pressing up on the d-pad makes the player move up
                playerUp = True
                playerDown = False
                if singleplayer:
                    player.up = True  # Player dashes upwards when L1 is pressed
                    player.down = False
                    player.right = False
                    player.left = False
                if not singleplayer:
                    player1.up = True  # Player 1 dashes upwards when L1 is pressed
                    player1.down = False
                    player1.right = False
                    player1.left = False
            if event.value[1] == -1:  # Pressing down on the d-pad makes the player move down
                playerUp = False
                playerDown = True
                if singleplayer:
                    player.up = False
                    player.down = True  # Player dashes downwards when L1 is pressed
                    player.right = False
                    player.left = False
                if not singleplayer:
                    player1.up = False
                    player1.down = True  # Player 1 dashes downwards when L1 is pressed
                    player1.right = False
                    player1.left = False
            if event.value[1] == 0:  # Not pressing either makes the player stationary on the y-axis
                playerUp = False
                playerDown = False

        # Events for things that occur in game
        if event.type == py.USEREVENT + 0 and not bossSpawn:
            if phase1:  # The code occurs before the first boss is defeated
                if not moderateEnemiesSpawn:  # Before 40000 ticks only basic enemies spawn
                    noBasicEnemies += 7  # Every 10000 ticks a new wave begins with 7 more enemies than the last one.
                    for i in range(noBasicEnemies):
                        makeBasicEnemies()
                if moderateEnemiesSpawn:  # After 40000 ticks only moderate enemies will spawn as well
                    for i in range(noBasicEnemies):
                        makeBasicEnemies()
                        makeModerateEnemies()
                    noModerateEnemies += 5  # Each new wave with moderate enemies has 5 more of them.
            if phase2:  # This code occurs after the first boss but before the second on
                if not dropperEnemiesSpawn:  # Happens before dropper enemies are added to the waves.
                    noModerateEnemies += 5  # Number of moderate enemies increments by 10 between each wave
                    for i in range(noModerateEnemies):
                        makeModerateEnemies()
                if dropperEnemiesSpawn:  # Happens after dropper enemies have been added to waves
                    getTime = py.time.get_ticks()
                    noModerateEnemies += 5
                    for i in range(noModerateEnemies):
                        makeModerateEnemies()  # Game spawns in increasing number of dropper and moderate enemies
                    for i in range(noDropperEnemies):
                        makeDropperEnemies()
                    noDropperEnemies += 5  # Number of dropper enemies increments by 5 each wave
            if phase3:  # This code occurs after the second boss is defeated
                noDropperEnemies += 5  # Number of dropper enemies and strong enemies increments by 5 and 7 each wave
                noStrongEnemies += 7
                if noDropperEnemies >= 25:
                    noDropperEnemies = 25  # Number of dropper enemies in a wave can't surpass 35
                if noStrongEnemies >= 45:
                    noStrongEnemies = 45  # Number of strong enemies in a wave can't surpass 40
                for i in range(noStrongEnemies):
                    makeStrongEnemies()  # These enemies will spawn at the start of each wave
                for i in range(noDropperEnemies):
                    makeDropperEnemies()

        if event.type == py.USEREVENT + 1:  # After 20000 ticks, meteors and laser beams will able to appear
            startHazards = True
            if phase2:  # 20000 ticks after the first boss is destroyed, dropper enemies will start spawning
                dropperEnemiesSpawn = True

        if event.type == py.USEREVENT + 2 and startHazards and not bossSpawn:
            meteor = Meteor()  # Meteors will fall every 300 ticks
            allSprites.add(meteor)  # They are added to the relevant sprite groups
            Meteors.add(meteor)

        if event.type == py.USEREVENT + 3 and startHazards and not bossSpawn:
            hozBeamWarning = HozBeamWarning()  # A laser beam warning will appear every 7500 ticks
            allSprites.add(hozBeamWarning)  # Warnings are followed by the actual laser beam.
            if verLaserBeamSpawn:  # A vertical beam warning appears when this True
                verBeamWarning = VerBeamWarning()  # The warning is added to the relevent sprite groups
                allSprites.add(verBeamWarning)

        if event.type == py.USEREVENT + 4:  # After 40000 ticks moderate enemies will start spawning
            moderateEnemiesSpawn = True
            if phase2:  # After 40000 ticks into the second phase, vertical laser beams will start appearing
                verLaserBeamSpawn = True

        if event.type == py.USEREVENT + 5 and not bossSpawn and not allBossesDone:  # Bossfight is triggered after 60000 ticks
            bossSpawn = True  # This means that no other enemies or hazards spawn during the bossfight
            if phase1:  # This code triggers if the first boss hasn't been fought yet
                allSprites.add(boss1)  # First boss is added to the relevant sprite groups
                bosses.add(boss1)
                if singleplayer:
                    player.health = player.maxHealth
                    player.ammo = player.maxAmmo  # Health and ammo are restored to full before a bossfight.
                if not singleplayer:
                    player1.health = player1.maxHealth
                    player1.ammo = player1.maxAmmo
                    player2.health = player2.maxHealth
                    player2.ammo = player2.maxAmmo  # Health and ammo are restored to full for both players
                noModerateEnemies += 5
            if phase2:  # This code triggers if the second boss hasn't been fought but the first has
                allSprites.add(boss2)  # Second boss is added to the relevant sprite groups.
                bosses.add(boss2)
                if singleplayer:
                    player.health = player.maxHealth
                    player.ammo = player.maxAmmo  # Health and ammo are restored to full before a bossfight.
                if not singleplayer:
                    player1.health = player1.maxHealth
                    player1.ammo = player1.maxAmmo
                    player2.health = player2.maxHealth
                    player2.ammo = player2.maxAmmo  # Health and ammo are restored to full for both players
            if phase3:  # This code triggers if the second boss has been fought
                bossSpawn = True
                allSprites.add(boss3)  # Third boss is added to the relevant sprite groups
                bosses.add(boss3)
                if singleplayer:
                    player.health = player.maxHealth
                    player.ammo = player.maxAmmo  # Health and ammo are restored to full before a bossfight.
                if not singleplayer:
                    player1.health = player1.maxHealth
                    player1.ammo = player1.maxAmmo
                    player2.health = player2.maxHealth
                    player2.ammo = player2.maxAmmo  # Health and ammo are restored to full for both players

    if singleplayer:
        if player.health <= 0:
            scoreFile = open("scores.txt", "a")
            scoreFile.write(str(score) + "\n")  # Writes the player's score and name to a file when they die
            scoreFile.close()
            nameFile = open("names.txt", "a")
            nameFile.write(username + "\n")  # Writes the player's name to a file when they die
            nameFile.close()  # Closes both files after they are written to
            gameOver = True  # When the player loses all of their health the game ends.
    if not singleplayer:
        if player1.health <= 0 or player2.health <= 0:
            scoreFile = open("scoresMultiplayer.txt", "a")
            scoreFile.write(str(score) + "\n")  # Writes the team's score to a file when one of the players die
            scoreFile.close()
            nameFile = open("namesMultiplayer.txt", "a")
            nameFile.write(username + "\n")  # Writes the team's name to a file when one of the players die
            nameFile.close()  # Closes both files after they are written to
            gameOver = True  # When one of the players loses all of their health the game ends.

    # Selection of collisions between sprites.
    # Collisions between player and all enemies and enemy weapons in singleplayer
    if singleplayer:
        # Collision between player and basic enemy
        attackBasicPlayer = py.sprite.spritecollide(player, basicEnemies, True, py.sprite.collide_circle)
        for hit in attackBasicPlayer:
            player.health -= 10  # Player loses 10 health points
            playerCollision.play()
        # Collision between player and basic enemy lasers
        attackPlayerBasicLaser = py.sprite.spritecollide(player, basicEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayerBasicLaser:
            player.health -= 10  # When the player collides with enemy lasers, they lose 10 health points.
            playerCollision.play()
        # Collision between player and meteor
        attackPlayerMeteor = py.sprite.spritecollide(player, Meteors, True, py.sprite.collide_circle)
        for hit in attackPlayerMeteor:
            player.health -= 10  # When the player collides with meteors, they lose 10 health points.
            playerCollision.play()
        # Collision between player and powerup
        attackPlayerPowerup = py.sprite.spritecollide(player, powerups, True, py.sprite.collide_circle)
        for hit in attackPlayerPowerup:
            if hit.powerupType == "moreHealth":  # If theyy collide with the shield image, they gain health
                player.health += 20
                if player.health > player.maxHealth:  # If their health becomes larger than the max, then it is set to the max value
                    player.health = player.maxHealth
            if hit.powerupType == "moreAmmo":  # If they collide with the star image, they gain ammo
                player.ammo += 50
                if player.ammo > player.maxAmmo:  # If their ammo becomes larger than the max, then it is set to the max value
                    player.ammo = player.maxAmmo
        # Collision between player and horizontal laser beam
        attackPlayerLaserBeam = py.sprite.spritecollide(player, laserBeams,
                                                        False)  # Laser beam doesn't disappear after a collision
        for hit in attackPlayerLaserBeam:
            player.health -= 1  # Player loses health continously when inside the laser beam
        # Collision between player and moderate enemy lasers
        attackPlayerModerateLaser = py.sprite.spritecollide(player, moderateEnemyWeapons, True,
                                                            py.sprite.collide_circle)
        for hit in attackPlayerModerateLaser:
            player.health -= 15  # When the player collides with moderate enemy lasers, they lose 15 health points.
            playerCollision.play()
        # Collision between player and strong weapons
        attackPlayerStrongLaser = py.sprite.spritecollide(player, strongEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayerStrongLaser:
            player.health -= 20
            playerCollision.play()
        # Collision between player and bosses
        attackPlayerBosses = py.sprite.spritecollide(player, bosses, False, py.sprite.collide_circle)
        for hit in attackPlayerBosses:
            player.health -= 2

    # Collisions between players and all hazards in multiplayer
    if not singleplayer:
        # Collisions between player 1 and the sprite groups
        # Collision between player 1 and basic enemy
        attackBasicPlayer1 = py.sprite.spritecollide(player1, basicEnemies, True, py.sprite.collide_circle)
        for hit in attackBasicPlayer1:
            player1.health -= 10  # Player 1 loses 10 health points
            playerCollision.play()
        # Collision between player 1 and basic enemy lasers
        attackPlayer1BasicLaser = py.sprite.spritecollide(player1, basicEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayer1BasicLaser:
            player1.health -= 10  # When player 1 collides with enemy lasers, they lose 10 health points.
            playerCollision.play()
        # Collision between player 1 and meteor
        attackPlayer1Meteor = py.sprite.spritecollide(player1, Meteors, True, py.sprite.collide_circle)
        for hit in attackPlayer1Meteor:
            player1.health -= 10  # When player 1 collides with meteors, they lose 10 health points.
            playerCollision.play()
        # Collision between player 1 and powerup
        attackPlayer1Powerup = py.sprite.spritecollide(player1, powerups, True, py.sprite.collide_circle)
        for hit in attackPlayer1Powerup:
            if hit.powerupType == "moreHealth":  # If they collide with the shield image, they gain health
                player1.health += 20
                if player1.health > player1.maxHealth:  # If their health becomes larger than the max, then it is set to the max value
                    player1.health = player1.maxHealth
            if hit.powerupType == "moreAmmo":  # If they collide with the star image, they gain ammo
                player1.ammo += 50
                if player1.ammo > player1.maxAmmo:  # If their ammo becomes larger than the max, then it is set to the max value
                    player1.ammo = player1.maxAmmo
        # Collision between player 1 and horizontal laser beam
        attackPlayer1LaserBeam = py.sprite.spritecollide(player1, laserBeams,
                                                         False)  # Laser beam doesn't disappear after a collision
        for hit in attackPlayer1LaserBeam:
            player1.health -= 1  # Player 1 loses health continously when inside the laser beam
        # Collision between player 1 and moderate enemy lasers
        attackPlayer1ModerateLaser = py.sprite.spritecollide(player1, moderateEnemyWeapons, True,
                                                             py.sprite.collide_circle)
        for hit in attackPlayer1ModerateLaser:
            player1.health -= 15  # When player 1 collides with moderate enemy lasers, they lose 15 health points.
            playerCollision.play()
        # Collision between player 1 and strong weapons
        attackPlayer1StrongLaser = py.sprite.spritecollide(player1, strongEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayer1StrongLaser:
            player1.health -= 20
            playerCollision.play()
        # Collision between player 1 and bosses
        attackPlayer1Bosses = py.sprite.spritecollide(player1, bosses, False, py.sprite.collide_circle)
        for hit in attackPlayer1Bosses:
            player1.health -= 2

        # Collisions between player 2 and the sprite groups
        # Collision between player 2 and basic enemy
        attackBasicPlayer2 = py.sprite.spritecollide(player2, basicEnemies, True, py.sprite.collide_circle)
        for hit in attackBasicPlayer2:
            player2.health -= 10  # Player 2 loses 10 health points
            playerCollision.play()
        # Collision between player 2 and basic enemy lasers
        attackPlayer2BasicLaser = py.sprite.spritecollide(player2, basicEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayer2BasicLaser:
            player2.health -= 10  # When player 2 collides with enemy lasers, they lose 10 health points.
            playerCollision.play()
        # Collision between player 2 and meteor
        attackPlayer2Meteor = py.sprite.spritecollide(player2, Meteors, True, py.sprite.collide_circle)
        for hit in attackPlayer2Meteor:
            player1.health -= 10  # When player 2 collides with meteors, they lose 10 health points.
            playerCollision.play()
        # Collision between player 2 and powerup
        attackPlayer2Powerup = py.sprite.spritecollide(player2, powerups, True, py.sprite.collide_circle)
        for hit in attackPlayer2Powerup:
            if hit.powerupType == "moreHealth":  # If they collide with the shield image, they gain health
                player2.health += 20
                if player2.health > player2.maxHealth:  # If their health becomes larger than the max, then it is set to the max value
                    player2.health = player2.maxHealth
            if hit.powerupType == "moreAmmo":  # If they collide with the star image, they gain ammo
                player2.ammo += 50
                if player2.ammo > player2.maxAmmo:  # If their ammo becomes larger than the max, then it is set to the max value
                    player2.ammo = player2.maxAmmo
        # Collision between player 2 and horizontal laser beam
        attackPlayer2LaserBeam = py.sprite.spritecollide(player2, laserBeams,
                                                         False)  # Laser beam doesn't disappear after a collision
        for hit in attackPlayer2LaserBeam:
            player2.health -= 1  # Player 2 loses health continously when inside the laser beam
        # Collision between player 2 and moderate enemy lasers
        attackPlayer2ModerateLaser = py.sprite.spritecollide(player2, moderateEnemyWeapons, True,
                                                             py.sprite.collide_circle)
        for hit in attackPlayer2ModerateLaser:
            player2.health -= 15  # When player 2 collides with moderate enemy lasers, they lose 15 health points.
            playerCollision.play()
        # Collision between player 2 and strong weapons
        attackPlayer2StrongLaser = py.sprite.spritecollide(player2, strongEnemyWeapons, True, py.sprite.collide_circle)
        for hit in attackPlayer1StrongLaser:
            player2.health -= 20
            playerCollision.play()
        # Collision between player 2 and bosses
        attackPlayer2Bosses = py.sprite.spritecollide(player2, bosses, False, py.sprite.collide_circle)
        for hit in attackPlayer1Bosses:
            player2.health -= 2

    # Collision between player weapons and basic enemies
    attackWeaponBasic = py.sprite.groupcollide(basicEnemies, playerWeapons, True, True, py.sprite.collide_circle)
    for hit in attackWeaponBasic:
        score += 1  # When the player weapon destroy a basic enemy, the score goes up by one.
        enemyCollision.play()
    # Collision between player weapons and basic enemy lasers
    WeaponBasicLaser = py.sprite.groupcollide(basicEnemyWeapons, playerWeapons, True, True)
    # Collision between meteors and player weapons
    attackWeaponMeteor = py.sprite.groupcollide(Meteors, playerWeapons, True, True, py.sprite.collide_circle)
    for hit in attackWeaponMeteor:
        if random.random() > 0.7:  # If the number between 0-1 is >0.7, a powerup is created.
            powerup = Powerup(hit.rect.x, hit.rect.y)  # Powerup spawns at the meteor's location
            allSprites.add(powerup)  # This powerup is added to the revelant sprite groups
            powerups.add(powerup)
        meteorCollision.play()
    # Collision between player weapons and moderate enemy lasers
    attackWeaponModerateLaser = py.sprite.groupcollide(moderateEnemyWeapons, playerWeapons, True, True)
    # Collision between player weapons and strong weapons
    attackWeaponStrongLaser = py.sprite.groupcollide(strongEnemyWeapons, playerWeapons, True, True)

    # Collision between player weapons and boss 1
    attackWeaponsBoss1 = py.sprite.spritecollide(boss1, playerWeapons, True, py.sprite.collide_circle)
    for hit in attackWeaponsBoss1:
        boss1.health -= 1  # When player weapons hit the first boss, they lose 1 health point
        if boss1.health <= 0:
            score += 20  # Gains 20 points for beating the first boss
            boss1.kill()  # First boss is removed from the boss
            bossSpawn = False  # Enemies can spawn again
            phase1 = False  # End of the first phase of the game
            phase2 = True  # Start of the second phase
            py.time.set_timer(py.USEREVENT + 0,
                              10000)  # Events that repeat after a certain number of ticks are reset here
            py.time.set_timer(py.USEREVENT + 1, 20000)
            py.time.set_timer(py.USEREVENT + 2, 300)
            py.time.set_timer(py.USEREVENT + 3, 7500)
            py.time.set_timer(py.USEREVENT + 4, 40000)
            py.time.set_timer(py.USEREVENT + 5, 60000)
            startHazards = True
            if singleplayer:
                player.maxHealth = 125  # Max health and ammo are increased after phase 1
                player.maxAmmo = 250
                player.health = player.maxHealth
                player.ammo = player.maxAmmo  # Health and ammo set to their new maximum values.
            if not singleplayer:
                player1.maxHealth = 125  # Max health and ammo are increased after phase 1
                player1.maxAmmo = 250
                player1.health = player1.maxHealth
                player1.ammo = player1.maxAmmo
                player2.maxHealth = 125
                player2.maxAmmo = 250
                player2.health = player2.maxHealth
                player2.ammo = player2.maxAmmo  # Health and ammo set to their new maximum values.
            noModerateEnemies += 10
            for i in range(noModerateEnemies):
                makeModerateEnemies()
            # music=py.mixer.music.load(os.path.join("Sounds","Lyricism Without Tears.mp3"))
            # py.mixer.music.set_volume(0.5)
            # py.mixer.music.play(-1)

    # Collision between player weapons and second boss
    attackWeaponsBoss2 = py.sprite.spritecollide(boss2, playerWeapons, True, py.sprite.collide_circle)
    for hit in attackWeaponsBoss2:
        boss2.health -= 1  # When player weapons hit the second boss, they lose 1 health point
        if boss2.health <= 0:
            score += 40  # Gains 40 points for beating the second boss
            boss2.kill()  # Second boss is removed from the game
            bossSpawn = False
            phase2 = False  # End of the second phase
            phase3 = True  # Start of the third phase
            py.time.set_timer(py.USEREVENT + 0,
                              10000)  # Events that repeat after a certain number of ticks are reset here
            py.time.set_timer(py.USEREVENT + 1, 20000)
            py.time.set_timer(py.USEREVENT + 2, 300)
            py.time.set_timer(py.USEREVENT + 3, 5500)
            py.time.set_timer(py.USEREVENT + 4, 40000)
            py.time.set_timer(py.USEREVENT + 5, 60000)
            startHazards = True  # These are True so that laser beams and meteors start immediately in the next phase
            verLaserBeamSpawn = True
            if singleplayer:
                player.maxHealth = 150  # Max health and ammo are increased after phase 1
                player.maxAmmo = 300
                player.health = player.maxHealth
                player.ammo = player.maxAmmo  # Health and ammo set to their new maximum values.
            if not singleplayer:
                player1.maxHealth = 150  # Max health and ammo are increased after phase 2 for both players
                player1.maxAmmo = 300
                player1.health = player1.maxHealth
                player1.ammo = player1.maxAmmo
                player2.maxHealth = 150
                player2.maxAmmo = 300
                player2.health = player2.maxHealth
                player2.ammo = player2.maxAmmo  # Health and ammo set to their new maximum values.
            for i in range(noStrongEnemies):  # Spawns in dropper and strong enemies at the start of the third phase
                makeStrongEnemies()
            for i in range(noDropperEnemies):
                makeDropperEnemies()

    # Collision between player weapons and third boss
    attackWeaponsBoss3 = py.sprite.spritecollide(boss3, playerWeapons, True, py.sprite.collide_circle)
    for hit in attackWeaponsBoss3:
        boss3.health -= 1  # When player weapons hit the third boss, they lose one health point
        if boss3.health <= 0:
            score += 60  # Player gets 60 points for beating the third boss
            boss3.kill()  # Third boss is removed from the game
            allBossesDone = True
            bossSpawn = False
            py.time.set_timer(py.USEREVENT + 0,
                              10000)  # Events that repeat after a certain number of ticks are reset here
            py.time.set_timer(py.USEREVENT + 1, 20000)
            py.time.set_timer(py.USEREVENT + 2, 300)
            py.time.set_timer(py.USEREVENT + 3, 5500)
            py.time.set_timer(py.USEREVENT + 4, 40000)
            py.time.set_timer(py.USEREVENT + 5, 60000)
            startHazards = True  # These are True so that laser beams and meteors start immediately in the next phase
            verLaserBeamSpawn = True
            if singleplayer:
                player.maxHealth = 175  # Max health and ammo are increased after the third phase
                player.maxAmmo = 350
                player.health = player.maxHealth  # Health and ammo are set to their max values
                player.ammo = player.maxAmmo
            if not singleplayer:
                player1.maxHealth = 175  # Max health and ammo are increased after phase 3 for both players
                player1.maxAmmo = 350
                player1.health = player1.maxHealth
                player1.ammo = player1.maxAmmo
                player2.maxHealth = 175
                player2.maxAmmo = 350
                player2.health = player2.maxHealth
                player2.ammo = player2.maxAmmo  # Health and ammo set to their new maximum values.
            for i in range(noStrongEnemies):  # Spawns in dropper and strong enemies at the after beating boss 3
                makeStrongEnemies()
            for i in range(noDropperEnemies):
                makeDropperEnemies()
    if phase2:
        boss1.health = 500
    if phase3:
        boss1.health = 500
        boss2.health = 500
    if allBossesDone:
        boss3.health = 500
    clock.tick(fps)  # This determines the number of frames per second the game runs at, right now it is 60.
    
    
