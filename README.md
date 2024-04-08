________________________________________________________________________
DOCUMENTATION FOR COMMAND-LINE WEATHER CHECKING APPLICATION USING PYTHON
________________________________________________________________________


-------------------------------
THIS APPLICATION ALLOWS YOU TO:
-------------------------------

  1> Check weather by providing a city name.
  2> Add a city to your list of favorite cities.
  3> Remove a city from your list of favorite cities.
  4> List all your favorite cities.


-----------------
COMMANDS TO USE:-
-----------------

  -h, --help            show this help message and exit
  
  --add-favorite ADD_FAVORITE
                        Add city to favorites

  --remove-favorite REMOVE_FAVORITE
                        Remove city from favorites

  --list-favorites      List favorite cities



You can run the script with appropriate command-line arguments to perform these actions.
For example:-

python weather_app.py London
python weather_app.py --add-favorite Paris
python weather_app.py --remove-favorite Paris
python weather_app.py --list-favorites

This application includes proper error handling and data validation. It also provides basic documentation of the commands through the --help option in argparse.
