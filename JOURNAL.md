
# Experiment results

## Feature type based experiments

### With numerical features only

    Find the code at: notebooks/feature_experiments/pp_with_numerical_features.ipynb

    Tried several different algorithms:
        * Linear Regression ('mae': 2591.301854580673)
        * LR with L1 regularization ('mae': 2591.3018262598803)
        * LR with L2 regularization ('mae': 2580.879972075066)

        * Random Forest ('mas': 1582.333400234843)
        * Ada Boost ('mas': 2314.3984964299284)

    None of them were trained on scaled data

    - The best one by far is Random Forest
    - Seems like regularization doesn't help, the models haven't overfit
  

### With numerical and boolean features only

    Find the code at: notebooks/feature_experiments/pp_with_numerical_and_boolean.ipynb

    Tried several different algorithms:
        * Linear Regression ('mae': 2476.184748352771)
        * LR with L1 regularization ('mae': 2476.184684099405)
        * LR with L2 regularization ('mae': 2455.4171776187445)

        * Random Forest ('mae': 1543.3680359153436, r2': 0.8454098339729921)
        * Ada Boost ('mae': 2077.0537898462258)

    None of them were trained on scaled data

    - Slightly better results on all algorithms used
    - Boolean features are useless to us
    - Ada Boost won't do


    From here on I'll refer to numerical and boolean features as just numerical
    From here on this is our base model using numerical features


### With all features except the anonymous ones and model name

    Find the code at: notebooks/feature_experiments/pp_with_categorical.ipynb

    Tried only those two this time:
        * Linear Regression ('mae': 2092.3902383415016)
        * Random Forest ('mae': 1186.1121940042963)
  
    None of them were trained on scaled data

    - Good, we have some improvement

    I tried Random Forest on scaled data and managed:
        * Random Forest ('mas': 0.023340695355454924, 'r2': 0.9058097095315579)
    
    - With is a slight but notable improvement, I'll stick to that configuration

    From here on this is our base model using categorical features

### With just categorical features

    Find the code at: notebooks/feature_experiments/pp_with_categorical.ipynb

    I only tried Random Forest with scaled data
        * Random Forest ('mae': 0.05576980390771338)

    - The other features are also useful, duh


## Categorical feature based experiments

### With numerical and car class features

    Find the code at: notebooks/feature_experiments/pp_with_car_class.ipynb

    Car class is a feature that @stefanhalvadzhiev engineered

    Tried these here:
        * Linear Regression ('mae': 0.047601994219254276, 'r2': 0.6612018466832905)
        * Random Forest ('mae': 0.02866481845207747, 'r2': 0.8714833542650766)

    Turns out that, contrary to our beliefs, this feature doesn't add too much
    new useful information

### With numerical and car age features

    Find code at: notebooks/feature_experiments/pp_with_age.ipynb

    Tried:
        * Random Forest ('mae': 0.03168711392853584, 'r2': 0.8285503755995923)

    - Age for some reason lowered the R2 score comapared to the base numerical
    model

    No satisfying results :(


### With car country features

    Find code at: notebooks/feature_experiments/pp_with_country.ipynb

    Tried:
        * Random Forest ()


### With body type

    Find code at: notebooks/feature_experiments/pp_with_body_type.ipynb

    Tried:
        * Random Forest ('mae': 1457.2447660646897, 'r2': 0.8549143878962937)

    - Turns out body type affect slightly the price, it is useful in our experiments

## Neural network experiments

### With numerical features

    The architecture was Input - Dense(256, 'relu') - Dense(256, 'relu') - Dense(1, 'linear')

    After 20 epochs with batch size 128 we got
        'mae': 0.03476074184260313
        'r2': 0.7608392242752923

    with was alright but not satisfying

### With all features except model_name

    The architecture was Input - Dense(256, 'relu') - Dense(256, 'relu') - Dense(1, 'linear')

    After 20 epochs with batch size 128 we got

## Outlier experiments

    I removed all records with price_use < 500 and price_usd > 35'000 which amounted to about 1500 records removed

    I trained a Random Forest model with that data and got our currently-best model with the following metrics

        'rmse': 0.047438160879931066
        'mae': 0.02907861805919358
        'r2': 0.9151684424220554

    Which is better than our previous best model
    
    - Outliers were messing with us after all


# Feature importance insights

    After using yet again Random Forest though this time as a method to find the importance of features, I found out that most of them are with close to zero value compared to a special few
    By hand and eye I extracted those:

    ['odometer_value', 'year_produced', 'engine_capacity', 
    'drivetrain_front', 'class_high-end', 'transmission_automatic',
    'number_of_photos', 'up_counter', 'duration_listed']

    Then I ran a Random Forest model and got 
        'rmse': 15.078059749785991
        'mae': 0.5313118575918222
        'r2': -0.05208823494223284

    Please note that those were not scaled values that I passed to the model
    I am not sure about 
    I think it is because i extracted those features from the same model
    architectually speaking

    Then I tried a neural network for sanity check
    The architecture was Input - Dense(256, 'relu') - Dense(256, 'relu') - Dense(1, 'linear')

    After 20 epochs with batch size 128 we got
        'mae': 3714.0451438475243
        'r2': 0.25510930747502736

    which was depressing, but then it got more depressing when I found out that I basically tested the model on the training data (casual stuff) and did not notice. Really, if it was something else we shouldn't have got such results


# EDA insights

    I found out that there were really rare prices in the dataset. Very few cars had a price of above 35'000 and the really cheap cars (price less than 500) were looking like the rest. My guessing is those cars were hit and in really bad shape - undrivable. 
