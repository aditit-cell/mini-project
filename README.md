Steps to run the commands on terminal:)
````bash
source venv/bin/activate
````
````bash
make
````
````bash
code results/coverage_log.csv
````
next inside the ml folder:
````bash
cd ml
````
````bash
source ../venv/bin/activate
````
````bash
ls ../results
````
````bash
python3 train_model.py
````
````bash
ls
````
u should see the following:
model.pkl  prioritized_tests.csv  priority_plot.png  train_model.py
````bash
code prioritized_tests.csv
````
this will open vs code and show the output csv
````bash
python3 -c "import joblib; m=joblib.load('model.pkl'); print(m)"
````
it should show RandomForestClassifier()
and to see plot click the png from the vs code
