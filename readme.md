# Project Overview

This project offers a comprehensive demonstration of various machine learning techniques, including synthetic data generation, feature engineering, and advanced natural language processing (NLP) using large language models (LLMs). While the current focus is on evaluating courses and instructors, the framework is designed to be highly adaptable, allowing you to modify it for any set of attributes or measures.

The project is implemented using Angular for the frontend dashboard and Express.js with a MySQL API for the backend. The dashboard allows for dynamic visualization and exploration of generated datasets.




## 1- Synthetic data Generation, Model training and evalutation

In this example, designing a feedback evaluation system for courses taken by employees involves creating a comprehensive feedback form. This form should capture a variety of perspectives, including the effectiveness of the course, the quality of the instructor, and the overall learning experience. For a more comprehensive overview, including full dataset generation, model training, and evaluation, please refer to the related project [here](https://github.com/Da-HaTer/Feedback-Dataset/blob/main/feedback-simulation.ipynb) or on [Kaggle](https://www.kaggle.com/code/oussamahaboubi/feedback-simulation).


## 2- Data integration
the data is transformed and imported into the database using [this python script]([script](https://github.com/Da-HaTer/Feedback-Dataset/blob/main/db_script.py)) and its corresponding mysql related modules.

## 3- Visualization
refer to [Angular](https://github.com/Da-HaTer/Angular-Dashboard/) and [Express.js](https://github.com/Da-HaTer/Express-server/) sections


# How to Run:
```shell
git clone --recursive https://github.com/Da-HaTer/Feedback-Dataset
```
You can follow the steps provided in the notebook to generate your own version of the dataset or use the one provided in this project ([feedback_dataset_fr.csv ](https://github.com/Da-HaTer/Feedback-Dataset/blob/main/feedback_dataset_fr.csv))
- Follow the steps provided in [Express.js](https://github.com/Da-HaTer/Express-server/).
- Run [db_script.py](https://github.com/Da-HaTer/Feedback-Dataset/blob/main/db_script.py) to create the database and insert the data, make sure to install the required python modules and to check your database connection and credentials (make sure you ``./Express/.env`` file exists with a valid path).
- Follow the steps provided in [Angular](https://github.com/Da-HaTer/Angular-Dashboard/) .
