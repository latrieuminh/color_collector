# Color Collector Game

This project will guide you through creating a simple game called "Color Collector" using Python's Pygame library. In this game, the player controls a square that collects blocks of a target color. The target color changes periodically, and the player's score increases or decreases based on whether they collect the correct color block.

## Table of Contents

1. [Game Design](#game-design)
2. [Step-by-Step Instructions](#step-by-step-instructions)
   - [Step 1: Initialize Pygame](#step-1-initialize-pygame)
   - [Step 2: Set Up Display and Colors](#step-2-set-up-display-and-colors)
   - [Step 3: Create Base Sprite Classes](#step-3-create-base-sprite-classes)
   - [Step 4: Add Player Class](#step-4-add-player-class)
   - [Step 5: Create Block Class with Movement](#step-5-create-block-class-with-movement)
   - [Step 6: Add Main Game Variables](#step-6-add-main-game-variables)
   - [Step 7: Handle Events and Player Updates](#step-7-handle-events-and-player-updates)
   - [Step 8: Detect Collisions and Update Score](#step-8-detect-collisions-and-update-score)
   - [Step 9: Draw and Display Game Elements](#step-9-draw-and-display-game-elements)
   - [Step 10: End Game Screen](#step-10-end-game-screen)
3. [Conclusion](#conclusion)

## Game Design

1. **Player:** The player is a square that moves using the arrow keys.
2. **Blocks:** Blocks appear with different colors and bounce around the screen. The player collects these blocks to gain or lose points based on the target color.
3. **Score:** The player scores points by collecting blocks of the target color. Points are lost if they collect the wrong color.
4. **Timer:** The game has a time limit, after which it ends, and the player's final score is displayed.

## Step-by-Step Instructions

### Step 1: Initialize Pygame

1. Import the necessary libraries (`pygame`, `random`, `time`).
2. Initialize Pygame to start working with the game functions:
   ```python
   pygame.init()
   ```

### Step 2: Set Up Display and Colors

1. Set the screen width and height as variables.
2. Define colors for the background, player, and possible block colors.
3. Create the game window and set a title for it using `pygame.display.set_mode` and `pygame.display.set_caption`.

Here's an expanded guide on creating the `GameSprite` base class. This class will serve as a foundation for any objects you want to display on the screen, such as the player and the colored blocks.

### Step 3: Create Base Sprite Classes

In Pygame, sprites are objects that represent anything that needs to be displayed on the screen. To manage game elements like the player and blocks, we'll create a base class called `GameSprite` that contains shared properties and methods.

#### Step-by-Step Instructions

1. **Define the `GameSprite` Class**  
   To create a base sprite class, define a class called `GameSprite` that inherits from `pygame.sprite.Sprite`. This inheritance allows you to take advantage of Pygame's built-in sprite handling features, like grouping and collision detection.
   
   ```python
   class GameSprite(pygame.sprite.Sprite):
       def __init__(self, color, x, y, width, height, speed):
           super().__init__()  # Initialize the sprite superclass
   ```

2. **Set Up the `__init__` Method**  
   The `__init__` method initializes each `GameSprite` object with essential properties, like its appearance and position. Here’s how to add each attribute:

   - **Color**: The color of the sprite. This will be set by filling a Pygame `Surface` with the desired color.
   - **Size (width and height)**: Determines the size of the sprite on the screen.
   - **Position (x, y)**: Specifies the starting coordinates of the sprite.
   - **Speed**: Controls the movement speed of the sprite (useful for moving objects like the player and blocks).

3. **Add a `reset` Method**  
   The `reset` method draws the sprite onto the game window at its current position. This is used to update the sprite's position on each frame, so it's crucial to call this method for each sprite in the main game loop.

   ```python
       def reset(self):
           main_win.blit(self.image, (self.rect.x, self.rect.y))  # Draw the sprite on the game window
   ```

### Step 4: Add Player Class

1. Create a `Player` class that inherits from `GameSprite`.
2. Add an `update` method to control the player's movement using keyboard input:
   - Use `pygame.key.get_pressed()` to detect arrow keys for movement.
   - Adjust the player's position based on key presses and check for screen boundaries.

### Step 5: Create Block Class with Movement

1. Define a `Block` class that also inherits from `GameSprite`.
2. Add an `update` method to move the block and make it "bounce" off the screen edges:
   - Change the direction of movement if the block hits any screen edge.
3. Randomize each block's color, position, and speed.

### Step 6: Add Main Game Variables

1. Set up the score, game duration, and a timer to track the game start and target color change intervals.
2. Use `random.choice` to pick a starting target color from the available colors.
3. Define a function that generates new blocks with random properties and adds them to a `pygame.sprite.Group`.

### Step 7: Handle Events and Player Updates

1. In the main game loop, add an event handler to check if the player closes the game window.
2. Call the `update` methods for the player and blocks.

### Step 8: Detect Collisions and Update Score

1. Use `pygame.sprite.spritecollide` to detect collisions between the player and blocks.
2. If a collision occurs:
   - Check if the block's color matches the target color.
   - Adjust the score based on whether it matches the target color or not.
   - Generate a new block to replace the collected one.

### Step 9: Draw and Display Game Elements

1. In the game loop, fill the background color.
2. Use `reset` methods to draw the player and blocks.
3. Display the score, target color, and remaining time on the screen.
   - Use `pygame.font.Font` to set up a font and render text with `render` and `blit`.
4. Update the display with `pygame.display.update` to show the latest frame.

### Step 10: End Game Screen

1. After the game loop, create an end screen to display the final score.
2. Render and display the game-over message using the `render` and `blit` methods.
3. Add a short delay to allow the player to view their score before the program closes.

## Conclusion

You've now created a "Color Collector" game using Pygame. This game includes key programming concepts like handling user input, updating game states, detecting collisions, and managing sprite objects. Customize and expand this game by adding new features or modifying its rules.

--- 

Feel free to experiment and add new features! Enjoy building your game!
