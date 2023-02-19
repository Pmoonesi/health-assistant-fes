# health-assistant-fes
This is the second project for the course Computational Intelligence - Spring 2022, Dr. Ebadzadeh

## introduction
In this project we have a simple panel where we get the data from the user, then we use fuzzy logic to calculate the health status of the user. 

For this purpose we first need to fuzzify the data, this is implemented in `fuzzification.py` where we used the plots we were given in the project description to extract the membership functions. Then we have to infer the data, this is implemented in `inference.py` where we extracted the rules from the `rules.fcl` and then calculated the membership of each outcome. Finally we had to defuzzify the results, this is implemented in `defuzzification.py` where we used the centroid method to calculate the final result. to implement the centroid defuzzification method we used the skfuzzy library.

Finally we combine these steps in the `final_result.py` and we return the results in simple text format. 

## structure
You need these files to run the project. the `static` and `templates` folders are for the flask panel and I am not going to explain them here.

    .
    ├── ...
    ├── static
    ├── templates
    ├── app.py
    ├── defuzzification.py
    ├── final_result.py
    ├── fuzzification.py
    ├── inference.py
    ├── requirements.txt
    └── rules.fcl

## how to run
We first need to install the requirements, you can do this by running the following command in the terminal.
``` bash
pip install -r requirements.txt
```
As I mentioned earlier, we have a simple panel for user to enter the data. It is implemented in the `app.py` with flask. You can run the app by running the following command in the terminal.
``` bash
python app.py
```
Now, you can access this panel by going to [`http://127.0.0.1:8448/`](http://127.0.0.1:8448/) in your browser.
