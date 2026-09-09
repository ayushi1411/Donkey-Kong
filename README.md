# Donkey Kong - Python Terminal Game

A classic retro Donkey Kong style game played entirely in the terminal! Navigate the platforms, avoid the fireballs, collect coins, and rescue the Queen to level up!

## 🎮 How to Play

### Controls
The game reads single keystrokes (no need to press Enter).

*   **`a` or `A`**: Move Left
*   **`d` or `D`**: Move Right
*   **`w` or `W`**: Climb Up (when on stairs)
*   **`s` or `S`**: Climb Down (when on stairs)
*   **`[Spacebar]`**: Jump
    *   *Note on jumping*: After pressing Spacebar, you must press a directional key (`w` to jump straight up, `a` to jump left, or `d` to jump right) to complete the jump action over gaps or fireballs!
*   **`q` or `Q`**: Quit the game

### Legend (What the characters mean)
The game board is drawn using ASCII characters. Here is what each symbol represents:

*   **`P` (Player)**: This is you! You spawn at the bottom of the board.
*   **`D` (Donkey)**: The boss enemy located at the top. It paces back and forth and throws fireballs down at you.
*   **`Q` (Queen)**: Your objective. She is locked in the cage at the very top. Reach her to complete the level.
*   **`O` (Fireballs)**: Deadly obstacles thrown by the Donkey. If you touch one, you lose a life and 25 points!
*   **`c` (Coins)**: Collectible items scattered across the floors. Each coin gives you +5 points.
*   **`H` (Stairs/Ladders)**: Use these to climb up and down between different floors. Some stairs might be broken (missing a piece), so watch your step!
*   **`x` (Walls & Floors)**: The solid ground you walk on and the walls of the map/cage.

## 🎯 Scoring & Objectives
*   **Rescue Queen**: +50 points and level up!
*   **Collect Coin**: +5 points.
*   **Hit by Fireball / Donkey**: -25 points and you lose 1 life. (You start with 3 lives).

Good luck, and watch out for the falling fireballs!
