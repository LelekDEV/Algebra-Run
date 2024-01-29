# Algebra-Run

## Preamble
Hello everyone! If you have not guessed already this repository contains a project of a clone of the game "Geometry Dash". Let me jump into some details.

## Overview
As of now, the entire project is written in python's pygame library. I've decided to used it because of how simple, light and limitless this game making tool is. To any python haters out there: yes, the pygame module (and the python programming language) might be slow but I just want to say that I simply don't care. Pygame's speed is absoulutely enough for my project and it wont stop me from using it.

## Features

### Physics
In this projec I've tried to make physics as close as possible to the base game while also keeping them in my liking. The current `player.vel.x` to `player.jump_height` to `player.gravity` to `player.rotation_speed` ratio is `16 : 36 : 2.2 : 6`. Thoose number aren't the exact ones from the original Geometry Dash (in fact they are pretty far away from it). That's due to fact that the official Geometry Dash physics values aren't accesible publicly. But don't worry - I'll try my best to update this values in the future to match the base more.

> [!NOTE] 
> This will make most of the levels in the past versions unplayable due to the physics changes

### Level editor
Even though this is the first version of this project, there's still a simple primitive level editor. To ascess it you have to press the `TAB` key at any moment (while in the editor press it again to go back to play mode). Use the `LEFT_ARROW_KEY` and the `RIGHT_ARROW_KEY` to move in the editor. At this moment there's four different objects you can place in the editor:

- Block: a solid blocks on which the player can jump. Any other collision instead of from the top will resut in killing you.
- Spike: a sharp obstacle that kills player on collision.
- Orb: a jump orb that let's you do another jump midair.

> [!NOTE]
> Orbs do support click buffering feature like in original Geometry Dash but well... not exactly. You can still buffer orbs midair but they don't claim your buffer. This means that you only have to click once to activate any amount of orbs (just as shown in the gif below).
> 
> *Hopefuly I'll insert here the gif sometime... ._.*
> 
> That also means that you can make this little combinations of orbs triggered in one click just like this:
> 
> *Hopefuly I'll insert here the gif sometime... ._.*
> 
> Keep in mind that I'll change it in the next versions.

- And the last object - Vertical Flip: yeah, it might sound pretty weird but it is a thing. It is used to flip an object that shares the same position on the grid. I've implemented it like that to save space in the `level.lvl` file (because not a lot of objects are actually flip so it is shorter to make a second object for every flipped one instead to add an information to every objact that it's flipped or not). However, I'll most probably change this system in the future.

> [!NOTE]
> The vertical flip can only be aplied to spikes, since they are the only objects to not have vertical symethry. Try not to place it anywhere else because it's invisible and might be hard to delete whereas unneeded vertical flips will just result in making the `level.lvl` file larger.
