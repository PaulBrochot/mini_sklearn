    # mini_sklearn 🏠

    A tiny machine learning library written in **pure Python**, with no NumPy and no scikit-learn, built to understand what happens behind `fit()` and `predict()`.

    The goal: **predict the price of an apartment from its surface area**, then compare several models to see which one makes the smallest error.

    > A learning project built to practice object-oriented programming (classes, inheritance, polymorphism) applied to data science.

    ---

    ## Features

    - Load a dataset from a CSV file
    - Randomly split the data into **training** and **test** sets
    - Three models sharing the same interface (`fit`, `predict`, `score`):

    | Model | How it works |
    |---|---|
    | `ModeleMoyenne` | Always predicts the average price. It is the **baseline**: a real model has to beat it. |
    | `RegressionLineaire` | Finds the line `price = a × surface + b` that best fits the data (least squares method). |
    | `KPlusProchesVoisins` | Predicts the average price of the `k` apartments with the closest surface area (k-nearest neighbors). |

    - Evaluation with the **mean absolute error**: how many k€ the model is off by, on average

    ---

    ## Project structure

    ```
    mini_sklearn/
    ├── appartements.csv   # the data (surface in m², price in k€)
    ├── donnees.py         # Dataset class: loading and train/test split
    ├── modeles.py         # Modele base class + the 3 models
    └── main.py            # trains and compares the models
    ```

    ### Class architecture

    ```
    Modele                      ← base class: score() shared by all models
    ├── ModeleMoyenne
    ├── RegressionLineaire
    └── KPlusProchesVoisins
    ```

    The `score()` method is written **only once**, in `Modele`. Each child model inherits it and only needs to define its own `fit()` and `predict()`.

    > Note: class, file and variable names are in French, as the project was written while learning Python in French.

    ---

    ## Installation and usage

    No external dependencies: Python 3 is all you need.

    ```bash
    git clone https://github.com/PaulBrochot/mini_sklearn.git
    cd mini_sklearn
    python3 main.py
    ```

    ---

    ## Example

    ```python
    import random
    from donnees import Dataset
    from modeles import ModeleMoyenne, RegressionLineaire, KPlusProchesVoisins

    random.seed(42)

    data = Dataset("appartements.csv")
    X_train, y_train, X_test, y_test = data.separer(0.8)

    modeles = [ModeleMoyenne(), RegressionLineaire(), KPlusProchesVoisins(k=3)]

    for m in modeles:
        m.fit(X_train, y_train)
        print(type(m).__name__, "→ mean error:", round(m.score(X_test, y_test), 1))

    print(modeles[1].predict([75]))   # estimated price for 75 m²
    ```

    ---

    ## Results

    With `random.seed(42)`, the test set contains the two **smallest** apartments (30 m² and 35 m²):

    | Model | Mean absolute error (k€) |
    |---|---|
    | ModeleMoyenne | 188.8 |
    | RegressionLineaire | 0.9 |
    | KPlusProchesVoisins (k=3) | 81.7 |

    **Analysis**

    - The linear regression is by far the best: the data is almost perfectly linear, and the line keeps working **outside** the range seen during training.
    - k-nearest neighbors struggles here because it **cannot extrapolate**: for a 30 m² apartment, its 3 closest neighbors in the training set are 45, 50 and 60 m², so it predicts their average price (~242 k€) instead of ~150 k€.
    - The baseline (`ModeleMoyenne`) ignores the surface completely, so it makes the largest error.

    > ⚠️ With only 10 apartments, the test set contains just 2 examples: results change a lot with the random split. Try another seed to see k-nearest neighbors perform much better on apartments in the middle of the range.

    ## What I learned

    - Designing a **base class** and **child classes** (inheritance, `super()`)
    - **Polymorphism**: a single loop calls `fit()` and `predict()` on different models
    - Raising exceptions (`NotImplementedError`)
    - Reading a CSV file and splitting data into training and test sets
    - How classic machine learning models work under the hood

    ---

    ## Possible improvements

    - [ ] Try `KPlusProchesVoisins` with different values of `k`
    - [ ] Add the mean squared error (MSE)
    - [ ] Handle several features (surface, number of rooms, neighborhood…)
    - [ ] Compare the results with scikit-learn