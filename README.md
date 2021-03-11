# chess_tournament
Program monitoring scores for a chess tournament, using Swiss pairing algorithm.

# Run program

## Run program from scratch

To run chess_scores_manager program:

1. Clone chess_manager_program in target folder:  
   git clone [https://github.com/Alexandremerancienne/chess_tournament](https://github.com/Alexandremerancienne/chess_tournament)    
4. Open your terminal and head to target folder.  
5. Create a virtual environment to install required packages: 
    
   Required packages are listed in requirements.txt file.  
   To create and activate a virtual environment, you can check the explanations provided in the following [README](https://github.com/Alexandremerancienne/scraping_program).  

4. Once required packages have been installed, run command (Windows OS): `python chess_scores_manager.py`

## Generate random variables and database

Some functions - such as the review of the players and the tournaments - are really useful only after generating a database.  

In addition to the program, a set of random variables (players, matches, rounds) has been added to generate random tournaments.  

To generate a random tournament, launch random_tournament.py file from the terminal, once in the top-level folder of the project:  
`python random_tournament.py`  

The script will generate a set of 50 random players and 10 random tournaments.  

# Functions

Once the program launched, the welcome page presents the following options:

## Generate new tournament 

This option allows the creation of a new tournament of 8 players:
* Each tournament includes 4 rounds of 2 matches;
* The matches are generated according to a Swiss-pairing algorithm.
* Optional sections have been added in controllers/controller_tournament.py and models/model_tournament  
to visualize the functioning of the algorithm. 
* All optional sections have been identified and can be deleted without affecting the program,  
so as to guarantee a more user-friendly interface.

## Players Database

This option gives access to the database of all players. 

The following actions are possible :

1. **"See all players"**: See all database players and sort them by ranking or by last name ;
2. **"Change player ranking"**: Change the ranking of a player;
3. **"Add new player"**: Add a player to the database of players.  

Options 2 and 3 allow to change the database of players without generating a new tournament.
   
## Tournaments Database

This option gives access to the database all players. 

The following actions are possible :

1. **"See all tournaments"**: See all database tournaments, as well as the details of any tournament; 
2. **"See tournament players"**: Search a tournament by name, location or year, and sort its players by ranking or by last name.

## Quit program

This option closes chess_scores_manager program. 

# Generate flake8-html report

flake8-html is a flake8 plugin to generate HTML reports of flake8 violations.

To generate flake8-html report:

1. Install flake8-html plugin in your virtual environment (plugin available on [Pypi.org](https://pypi.org/project/flake8-html/) website): `pip install flake8-html` 
2. Run flake8 from the top_level folder of chess_scores_manager program:  

   `flake8 --format=html --htmldir=<report_location>`  

   For instance, if you want to store your report in a folder named "flake_report", run:  

   `flake8 --format=html --htmldir=flake_report`  

   If you want to ignore the presence of a file or a folder when running flake8-html, add `--exclude` option to the command:  

   `flake8 --exclude=<file or folder to exclude> --format=html --htmldir=<name_of_holding_folder>`  
   
   The parameters of flake8 screening (such as maximum line length) are defined in setup.cfg file
