Week 2 – Python Fundamentals for Machine Learning
📌 Overview

This repository contains my Week 2 practical work focused on building strong Python foundations for Machine Learning.
The tasks cover NumPy operations, Pandas data manipulation, data visualization, and object-oriented programming, all demonstrated using the Titanic dataset.

The goal of this week was to understand how data is processed, analyzed, visualized, and prepared before applying Machine Learning algorithms.

🛠️ Technologies Used

Python 3

NumPy

Pandas

Matplotlib

Seaborn

Scikit-learn

Jupyter Notebook

VS Code

Git & GitHub

📂 Project Structure
Week-2-Python-ML/
│
├── numpy_basics.py
├── pandas_exploration.ipynb
├── data_visualization.py
├── data_preprocessor.py
│
├── titanic.csv
├── titanic_cleaned.csv
├── processed_titanic.csv
│
├── visualizations/
│   ├── line_age.png
│   ├── scatter_age_fare.png
│   ├── hist_pclass.png
│   ├── bar_survival.png
│   ├── box_fare.png
│   ├── violin_age.png
│   ├── heatmap.png
│   └── pairplot.png
│
└── README.md

✅ Task 2.1: NumPy Array Operations
📄 File: numpy_basics.py
🔹 Description

This script demonstrates 15+ NumPy operations essential for Machine Learning, including:

Array creation (array, zeros, ones, arange)

Reshaping arrays

Indexing and slicing

Mathematical operations (addition, multiplication, dot product)

Statistical operations (mean, median, standard deviation, variance)

Broadcasting

🎯 Learning Outcome

Efficient numerical computation

Understanding multidimensional data

Foundation for ML mathematical operations

✅ Task 2.2: Pandas Data Manipulation (Titanic Dataset)
📄 File: pandas_exploration.ipynb
🔹 Description

This notebook focuses on data cleaning, feature engineering, and exploratory data analysis using the Titanic dataset.

🔹 Key Steps Performed

Loaded dataset using Pandas

Identified and handled missing values

Dropped irrelevant columns

Created 5 new features:

FamilySize

IsAlone

Title

FarePerPerson

AgeGroup

Generated statistical summaries

Created visualizations using Matplotlib

Exported cleaned dataset as titanic_cleaned.csv

🎯 Learning Outcome

Real-world data preprocessing

Feature engineering techniques

Preparing data for ML models

✅ Task 2.3: Data Visualization with Matplotlib & Seaborn
📄 File: data_visualization.py
🔹 Description

This script generates 8 different visualizations using the cleaned Titanic dataset.

📊 Visualizations Included
Plot Type	Description
Line Plot	Age distribution
Scatter Plot	Age vs Fare
Histogram	Passenger class distribution
Bar Chart	Survival rate by gender
Box Plot	Fare by passenger class
Violin Plot	Age by gender
Heatmap	Correlation matrix
Pair Plot	Numerical feature relationships
📁 Output Folder

All plots are saved in the visualizations/ directory as PNG files.

🎯 Learning Outcome

Visual data interpretation

Identifying trends, correlations, and outliers

Communicating insights visually

✅ Task 2.4: Object-Oriented Programming for ML
📄 File: data_preprocessor.py
🔹 Description

This script implements an OOP-based data preprocessing pipeline using a DataPreprocessor class.

🔹 Class Functionalities

Load dataset

Handle missing values

Encode categorical features

Scale numerical features

Split data into training and testing sets

Save processed data

🎯 Learning Outcome

Writing reusable and modular code

Applying OOP concepts in ML workflows

Building scalable preprocessing pipelines

📈 Visual Results Preview

All generated plots are available in the visualizations folder and can be viewed directly on GitHub.

Example:

visualizations/heatmap.png
visualizations/box_fare.png
visualizations/pairplot.png

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install numpy pandas matplotlib seaborn scikit-learn jupyter

2️⃣ Run NumPy Script
python numpy_basics.py

3️⃣ Open Pandas Notebook
jupyter notebook pandas_exploration.ipynb

4️⃣ Generate Visualizations
python data_visualization.py

5️⃣ Run Data Preprocessor
python data_preprocessor.py

📌 Conclusion

This repository demonstrates my understanding of Python fundamentals for Machine Learning, including numerical operations, data manipulation, visualization, and object-oriented design. These skills form the foundation for building and deploying Machine Learning models in upcoming projects.
👤 Author

Zeeshan Ali
Machine Learning Student

⭐ Acknowledgements

Kaggle Titanic Dataset

Python open-source community
