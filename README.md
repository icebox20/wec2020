# Cosmetic Chess

## About

Cosmetic chess is a the similar to the chess you may know, but have some very cool changes! 
Cosmetic chess incorporated the rules of previously known standard chess with a few exciting twists and pieces. This newly modified game can be played with your friends online or in person
## Usage

1. Using a python IDE, Run `pip install pygame` to install pygame module

2. Download all files present within the game file on github

3. Load the python code within your IDE and run program

4. Once User interface is shown, select size of your desired chess board and begin playing!

## Server Usage

1. Using npm, Run `npm install` to install all the required dependencies 

2. A mongodb database is required for this server to work please add your database to a `.env file` in the main directory

3. Run using `npm run dev`

## Directions for using Program
	
1. Rules put in place for each piece:
    * Pawns 
        * Fill the front row of players sides of the board. 
        * Pawns may move in distances of 1-3 squares, and may only take opposing pieces in a diagonal manner
     when they are blocked by opposite team.
    * Bishops 
        *  Move and are placed as normal.
    * Rooks 
        * Move and are placed as normal.
    * Knights
        * Move like a queen, except they can only reach between 2 and 4 (inclusive) squares away
    * Queen
        * They may move in straight and diagonal lines
    * King
        * Moves and should be protected as normal
    * Vanguards
        * May move in an L of any size
       
2. Select any size of chess board you would like to play on

3. Play with your friends using applications such as teamviewer or play over a video call and use the given letters and numbers to say your moves.

## Work Flow

	- Project rolled out using agile methodology with 2 sprints
    - 1st sprint was focused on creating a normal functional chess game 
    - 2nd sprint was focused on meeting the project requirements

## Future Improvements

	1. Add some sort of CPU that a player can play against if alone.
	2. Improved UI design.
	3. Queen move timer to make the queen not as overpowered in skillset.
	4. Deploying the program online so that it can be played online without any excess factors.
	5. Adding different chess plays such as Castling.

## Sources

Drew a lot of insipiration from this youtube channel in figuring out how to create a chess board and make pieces move.
* [Chess Board & moves](https://www.youtube.com/channel/UCaEohRz5bPHywGBwmR18Qww)
* [L shape research for knight and vanguard](https://www.geeksforgeeks.org/count-ways-to-place-knights-moving-in-l-shape-in-chessboard/)
