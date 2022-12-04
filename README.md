# ML US baby names

Jupyter Notebook with a script to predict the next most common name in the US,
based on the historical data of most common baby names per year and state.

The datasource is public and can be found in the website of the US Social Security
Administration: <https://www.ssa.gov/cgi-bin/namesbystate.cgi>.

## Installation

Clone this repo and open it with Jupyter Notebook.

## Usage

Run each one of these notebooks in order:

### [1 download raw data](1_download_raw_data.ipynb)

This will download the historical data for each year and state using basic
**web scraping** techniques.

Make sure that the constants `YEAR_START` and `YEAR_END` (which can be found in the
file `constants.py`) match the available dates in the website.

### [2 compute features](2_compute_features.ipynb)

With the historical data, this script will compute the features needed to run the machine learning
algorithm in the next step.

For each year and name, the position or ranking of that name in each state is stored,
normalized from 0 to 1.

Also, the differences of this value with the value of 1, 2, ... until 5 years ago are stored.
These values can range from -1 to 1.

Finaly, the label is stored, indicating if the name was the most used next year or not.
Only one name per year is set to true. All the rest are set to false.

The dataset has the following columns:

- year
- name
- position of current year x 51 states
- difference with 1..5 years ago x 51 states
- label

### [3 generate model](3_generate_model.ipynb)

With the features and labels generated in the previous step, a
[Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
from the library **scikit-learn** is used to train a model that can predict the most common name next year.

The random forest classifier has been used because it is generally a good choice for classification tasks,
especially when the data is complex and there are many features (in this case, we have 306 features).

Random forest is an ensemble method that combines multiple decision trees, each trained on a different
subset of the data, to make predictions. This can improve the accuracy and robustness of the model,
but interpretability of the model is more complicated.

Other classification algorithms have been tested, but none of them has beaten the random forest,
even after optimizing the neural network with a grid search:

- [Logistic regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)
- [Support vector machines](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [Neural networks](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)

The 5 most recent years are removed from the dataset, leaving 51 years to train the model.

Once trained, the model is tested against those missing 5 years, with **80% accuracy**
(not really significant due the low number of predictions).

Finally, a prediction is made for next year 2022: **Liam**.

Will it be correct?
