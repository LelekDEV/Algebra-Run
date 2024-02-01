# Algebra-Run

## Preamble
Hello everyone! If you have not guessed already this repository contains a project of a clone of the game "Geometry Dash". Let me jump into some details.

## Overview
As of now, the entire project is written in python's pygame library. I've decided to used it because of how simple, light and limitless this game making tool is. To any python haters out there: yes, the pygame module (and the python programming language) might be slow but I just want to say that I simply don't care. Pygame's speed is absoulutely enough for my project and it wont stop me from using it.

## Quit keybinds
- `UP_ARROW_KEY` - jump
- `ALL_ARROW_KEYS` - move in the editor
- `TAB` - switch between play and edit mode
- `Q` - save the level
- `W` - enable show-hitboxes
- `E` - enable noclip

## Features

### Physics
In this projec I've tried to make physics as close as possible to the base game while also keeping them in my liking. The current `PLAYER_SPEED` to `PLAYER_JUMP_HEIGHT` to `PLAYER_GRAVITY` to `PLAYER_ROTATION_SPEED` ratio is `16 : 36 : 2.2 : 6`. Remember that just to shorten it from now on i'll be using custom shortcut *the golden ratio* whenever referencing it. Thoose number aren't the exact ones from the original Geometry Dash (in fact they are pretty far away from it). That's due to fact that the official Geometry Dash physics values aren't accesible publicly. But don't worry - I'll try my best to update this values in the future to match the base more.

> [!NOTE] 
> This will make most of the levels in the past versions unplayable due to the physics changes

Also I've implemented snapping mechanic. What it basically does is that it lets you survive and clamp on top of the block if the distance to it's top is less than `PLAYER_SNAP_LIMIT`. It's purpose is to make the game smoother and function as a drawback to imperfect physics. The current `PLAYER_SNAP_LIMIT` value is set to quarter of a regular block.

### Level editor
Even though this is the first version of this project, there's still a simple primitive level editor. To ascess it you have to press the `TAB` key at any moment (while in the editor press it again to go back to play mode). Use the `LEFT_ARROW_KEY`, `RIGHT_ARROW_KEY`, `UP_ARROW_KEY` and `DOWN_ARROW_KEY` to move in the editor. At this moment there's four different objects you can place in the editor:

- Block: a solid blocks on which the player can jump. Any other collision instead of from the top will resut in killing you.
- Spike: a sharp obstacle that kills player on collision.
- Orb: a jump orb that let's you do another jump midair. They have a slightly less jump height than regular jumping which isn't the case of the original game but that'll of course change in the future.

> [!NOTE]
> Orbs do support click buffering feature like in original Geometry Dash. If you don't know what it is - it's a mechanic that allows you to hold jump midair and immediately jump on the first possible frame on next touched orb. Buffer resets on touching ground.

- And the last object - Vertical Flip: yeah, it might sound pretty weird but it is a thing. It is used to flip an object that shares the same position on the grid. I've implemented it like that to save space in the `level.lvl` file (because not a lot of objects are actually flip so it is shorter to make a second object for every flipped one instead to add an information to every objact that it's flipped or not). However, I'll most probably change this system in the future.

> [!NOTE]
> The vertical flip can only be aplied to spikes, since they are the only objects to not have vertical symethry. Try not to place it anywhere else because it's invisible and might be hard to delete whereas unneeded vertical flips will just result in making the `level.lvl` file larger.

### Level saving
After you finally finish your level you can save it to the file in order to keep it. It is done via `Q` key in the editor. Here is an example of how a `level.lvl` file could look like:
```
10 0 10 1 11 1 12 1 12 0 25 2 25 1 25 0 26 2 27 2 27 1 27 0 29 3 29 2 29 1 29 0 30 3 31 3 31 2 31 1 31 0 33 2 33 1 33 0 40 1 40 0 38 2 38 1 39 2 40 2 38 0 43 3 43 2 43 1 43 0 45 2 45 1 45 0 48 3 48 2 48 1 48 0 50 2 50 1 50 0 53 1 54 1 55 1 64 1 64 0 69 1 69 0 64 4 69 4 77 1 77 0 78 1 79 1 79 0 85 3 85 2 85 1 85 0 86 3 87 3 87 2 87 1 87 0 90 5 92 4 97 4 99 3 102 4 104 3 106 2 111 2 113 1 115 2 115 6 121 4 122 4 12 5 11 5 10 5 18 4 16 4 17 4 28 7 27 7 29 7 25 6 33 6 38 6 39 6 45 6 50 6 53 0 55 0 81 0 83 0 82 0 93 0 93 1 94 1 95 1 95 0 115 0 115 1 115 7 115 8 119 3 114 8 113 8 112 8 111 8 110 8 109 8 108 8 107 8 106 8 105 8 104 8 103 8 102 8 101 8 100 8 99 8 98 8 97 8 96 8 123 4 125 3 82 7 41 7 42 7 78 5 86 6 130 2 130 1 130 0 130 5 130 6 130 8 130 7 134 4 134 3 134 0 134 8 134 7 138 8 138 5 138 4 138 1 138 0 129 1 129 0 128 0 143 0 143 4 142 5 143 5 144 5 147 0 147 4 147 5 146 5 148 5 153 4 153 3 153 2 153 1 153 0 155 3 155 2 155 1 155 0 157 2 157 1 157 0 162 2 162 1 162 0 155 6 153 7 157 5 159 4 162 5 165 2 167 4 166 2 168 4 163 0 164 0 
16 0 17 0 18 0 5 0 6 0 34 0 35 0 36 0 37 0 24 0 23 0 53 2 54 2 55 2 64 3 69 3 74 0 75 0 76 0 121 0 122 0 115 3 115 5 121 3 122 3 10 4 11 4 12 4 16 3 18 3 17 3 27 6 28 6 29 6 25 5 33 5 38 5 39 5 45 5 50 5 57 0 51 0 56 0 52 0 65 0 70 0 81 1 82 1 83 1 84 0 80 0 88 0 89 0 90 0 91 0 92 0 93 2 94 2 95 2 96 0 98 0 97 0 99 0 100 0 101 0 102 0 103 0 104 0 105 0 106 0 107 0 108 0 109 0 110 0 111 0 112 0 113 0 114 0 119 2 97 7 98 7 99 7 100 7 101 7 102 7 103 7 104 7 105 7 106 7 107 7 108 7 109 7 110 7 111 7 112 7 113 7 114 7 123 3 123 0 125 2 96 7 82 6 41 6 42 6 78 4 86 5 127 0 138 3 134 1 130 4 134 6 138 6 129 2 128 1 143 1 144 0 142 0 143 3 144 4 142 4 147 1 146 0 148 0 147 3 146 4 148 4 158 0 159 0 160 0 161 0 153 6 155 5 157 4 159 3 162 4 165 3 165 0 166 0 167 0 168 0 169 0 166 3 167 5 168 5 164 1 163 1 131 0 132 0 133 0 135 0 136 0 137 0 135 8 136 8 137 8 131 8 132 8 133 8 
22 1 35 1 54 4 75 1 82 3 94 3 108 1 126 0 126 1 150 0 150 1 150 2 159 1 165 4 167 6 151 2 151 1 151 0 
10 4 11 4 12 4 16 3 17 3 18 3 25 5 27 6 28 6 29 6 33 5 38 5 39 5 45 5 50 5 64 3 69 3 115 5 97 7 98 7 99 7 100 7 101 7 102 7 103 7 104 7 105 7 106 7 107 7 108 7 109 7 110 7 111 7 112 7 113 7 114 7 119 2 121 3 122 3 123 3 125 2 96 7 82 6 41 6 42 6 78 4 86 5 138 3 134 6 130 4 143 3 144 4 142 4 147 3 146 4 148 4 153 6 155 5 157 4 159 3 162 4 131 8 132 8 133 8 135 8 136 8 137 8
```

As you can see it consist of four lines of different numbers which are the level data. The system works like this:
- the numbers create pairs which represent position of the object;
- next, the line of the position defines the type of the object (first is for blocks, second for spikes etc.);
- lastly, if theres no object of a given type the line will only contain the `-` sign just to make reading the file easier.
  
A this moment the project doesn't support managing multiple files, so in order to save more than one level you have to change the name of already saved file to something like `level-01.lvl` and change it back to normal if you want to replay it.

### Songs
The default song used in this project is "sans." composed by Toby Fox. You can add a custom one at any moment. In order to do it you have to get here any other song named `song.ogg `. You don't necessarily have to use the `.ogg` file format. If you want to have other formats remember that you have to change it in the game code:

```python
269. # Change the song path right here
270. pygame.mixer.music.load('song.ogg') <- Change 'song.ogg' to whatever
271. pygame.mixer.music.play()
```

## Other stuff

### Framerate
With everything said we can't forget about framerate. After all it's still a pretty important thing. Currently the game is capped at 60 FPS. If you ever will have changed the maximum framerate you'll also have to change all the values so they match your framerate and the game runs at the same speed. Also the game doesn't use the `DELTA_TIME`. To anyone uninitiated, multiplying (almost) every value a game has to offer by the time difference (delta) between two frames you'll make the game run at the consisted speed amongst every possible framerate. I've decided not to use this feature because it can make some inconsistencies on lower framerate (ussualy caused by lag spikes) at the cost of occasional music desync. However it isn't really a problem on higher-than-intended FPS cap so I'll probably make an option in the future to automatically turn on `DELTA_TIME` whenever the FPS are above 60.

### Other modes
At any moment you can turn on the following modes:

- Show-hitbox mode: turned on by pressing `W` key. Shows you hitboxes of the objects (blue - solid, red - hazard, green - orbs trigger area, yellow - snapping limit). It also shows the player hitbox (red) and the player trail (green).
- Noclip mode: turned on by pressing `E` key. Let's you go trough hazards and solids. Touching solids results in clamping you to the top (just like snapping feature).

Additionally, both of theese modes are indicated by little cricles on the top right of the screen (show-hitbox - blue circle, noclip - red circle).

## Epilogue

### Contributing
If you'd like to contribute to the development of this project, follow these guidelines:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/your-feature.
3. Make your changes and commit them: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature/your-feature.
5. Create a pull request.

### License
This project currently doesn't run on any licence.

### Acknowledgments
Special thanks to the creator of Geometry Dash (RobTop) for inspiring this project. Also I want to give a shout out Toby Fox the creator of "Undertale" for making his awesome soundtrack. If you enjoy this project, consider supporting the original game on [the official Geometry Dash steam site](https://store.steampowered.com/app/322170/Geometry_Dash/).

### Contact
For questions or suggestions, feel free to contact me:

- Email - some.email@gmail.com

Happy gaming! 🚀
