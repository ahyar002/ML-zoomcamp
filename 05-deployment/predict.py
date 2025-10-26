import pickle


datapoint = {
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'yes',
    'dependents': 'no',
    'phoneservice': 'no',
    'multiplelines': 'no_phone_service',
    'internetservice': 'dsl',
    'onlinesecurity': 'no',
    'onlinebackup': 'yes',
    'deviceprotection': 'no',
    'techsupport': 'no',
    'streamingtv': 'no',
    'streamingmovies': 'no',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'electronic_check',
    'tenure': 1,
    'monthlycharges': 29.85,
    'totalcharges': 29.85
}


# load the model\
def load_model():
    with open('model.bin', 'rb') as f_in:
        model = pickle.load(f_in)
    
    return model


def predict(model, datapoint):

    churn = model.predict_proba(datapoint)[0, 1]

    if churn >= 0.5:
        print('send promo')
    else:
        print('dont do anything')


model = load_model()
predict(model, datapoint)




