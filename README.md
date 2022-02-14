# Space Shooter
Created: February 13, 2022 <br />
Completed: N/A


Last Edited: February 13, 2022

## Description:
Space Shooter is heavily inspired by the iconic video game Space Invaders. Although Space Shooter and Space Invaders have their inherent differences, the goal of each game is to kill all enemys. 

## Technologies Used:
Normally this project would be done n Scratch, however, I thought it would a fun challenge to make my game in Python. To handle all the game sprites and visuals, I will be using a python Library called Pygame. As the name implies, Pygame is a Python Library specialized for making games. I enjoy using Pygame because it's simple to learn and very powerful.

The environment I will code in will be PyCharm. PyCharm is a powerful Python IDE made by jetBrains. I find PyCharm to be quite user-freindly, which allows me to be more productive while coding.

## Sketch of Project:
![Untitled drawing (2)](https://user-images.githubusercontent.com/57376726/153796915-0652dbdb-92c9-4f40-8f6a-ad3eb223ae23.png)

## Prioritized Features List:
### Creating the Game Windows
1. Creating the window where the game will be played (Priority 1)
    - The window will be 600 pixels wide by 600 pixels tall
    - The basic background will be a nice light blue (0, 255, 255)
2. Creating the start screen window (Priority 4)
    - When you click a button on the screen, the game will begin
    - Will have game a title and the highest score on it
3. Creating the end screen window (Priority 4)
    - When you die this screen will appear
    - When you click a replay button, the game will start again
    - Will have your previous score and your highest score

### Creating Game Objects
1. Creating Player
    - Creating a basic rectangle to represent the Player (Priority 1)
    - Adding the player movement (Priority 1)
    - Adding the player shooting mechanics (Priority 2)
    - Adding the Player Ammo limit (Priority 2)
    - You lose the game if you run out of ammo and still have enemies on the feild (Priority 2)
2. Creating the Bullet
    - Creating a basic rectangle to represent the Bullet (Priority 2)
    - Adding the Bullet Movement (Priority 2)
    - Adding the Bullet Collision with Enemy (Priority 2)
    - Adding the Bullet Collision with Ammo-refill power-up (Priority 
3. Creating the Enemy
    - Creating a basic rectangle to represent the Enemy (Priority 1)
    - Adding Enemy movement patterns (Priority 3)
4. Creating the Power-up
    - Creating a basic rectangle to represent the Power-up (Priority 3)
    - Refilling Player Ammo when hit with bullet (Priority 3)

### Final Features
1. Game Sound affects (Priority 5)
    - Shooting sound affect
    - Collision sound affect
    - Losing sound affect
    - Winning sound affect
2. Background Music (Priority 5)
    - Game screen music
    - Start screen music
    - End screen music
3. Creating images (Priority 5)
    - Adding background image
    - Adding Player, Bullet, Enemy and Powerup image

## Implementation
To implement these features I will use the pygame library. Pygame has many features to make designing games easy. Some of these features include:
- Events
- SpriteGroups
- Display
- Clock

### Objects
- Player
- Bullet
- Enemy
- Power-up
### Scenes
- Start 
- Game
- End
### Logic involved
- Movement
    - The Player Movement
    - The Bullet Movement
    - The Enemy Movement
- Collisions
    - Collisions between the Bullet and the Enemy
    - Collisions between the Bullet and the Power-up
- User interaction
    - Start button on title screen
    - During game, clicking the space bar will shoot a bullet
    - Rerun button on end screen

## Version Guide
During game development, this portion of the file will be updated frequently

### Version 1.0:
        - All of priority 1 and priority 2 were added
