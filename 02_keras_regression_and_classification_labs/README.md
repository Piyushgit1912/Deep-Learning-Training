# 02 - Keras Regression & Classification Labs

First models built with Keras: regression, logistic regression, XOR, function approximation and time-series prediction.

| Notebook | Topic | Data |
|---|---|---|
| `01_function_approximation_with_neural_networks.ipynb` | learn a physics equation, a quadratic and a line | generated |
| `02_multi_variable_linear_regression.ipynb` | 3 inputs -> 1 output | inline arrays |
| `03_linear_regression_from_csv.ipynb` | same model, data from CSV | `data-01-test-score - data-01-test-score.csv` |
| `04_restaurant_rating_predictor.ipynb` | small regression network | inline arrays |
| `05_logistic_regression_and_xor.ipynb` | binary classification and the XOR problem | inline arrays |
| `06_stock_price_prediction_linear_and_lstm.ipynb` | linear baseline -> LSTM on a 5-day window | `data-02-stock_daily - data-02-stock_daily.csv` |

The CSV files sit in this folder because the notebooks load them by name. `data-03-diabetes` and `data-04-zoo` are included
for upcoming classification experiments (not used yet).

**Requires:** tensorflow / keras, numpy, matplotlib, scikit-learn
