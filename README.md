# Communere Test Project

This repository contains three main files : 

### test_project.ipynp : 
This file investigates featureas and trains a model best on best features. It then writes trained model on disk.

### update_db.py : 
A short script to read data from db, feed them on the model, and write model results on db again.

### run_script_every_day.sh : 
Abash script to run update_db.py in an inifitive loop with 24 hours delay.
