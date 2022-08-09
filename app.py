#import libraries
import numpy as np
import pandas as pd
import pickle
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))
#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')
    #To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    dataset = pd.read_csv('Market_Basket_Optimisation.csv', header=None)
    transactions = []
    for i in range(0, 7501):
        transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])

    from apyori import apriori
    rules = apriori(transactions=transactions, min_support=0.003, min_confidence=0.2, min_lift=3, min_length=2,
                    max_length=2)

    results = list(rules)

    # results

    def inspect(results):
        lhs = [tuple(result[2][0][0])[0] for result in results]
        rhs = [tuple(result[2][0][1])[0] for result in results]
        supports = [result[1] for result in results]
        confidences = [result[2][0][2] for result in results]
        lifts = [result[2][0][3] for result in results]
        return list(zip(lhs, rhs, supports, confidences, lifts))

    resultsinDataFrame = pd.DataFrame(inspect(results),columns=['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    # resultsinDataFrame

    return render_template('index.html', lhs0=lhs[0],rhs0=rhs[0],
                           lhs1=lhs[1],rhs1=rhs[1],
                           lhs2=lhs[2],rhs2=rhs[2],
                           lhs3=lhs[3],rhs3=rhs[3],
                           lhs4=lhs[4],rhs4=rhs[4],
                           lhs5=lhs[5],rhs5=rhs[5],
                           lhs6=lhs[6],rhs6=rhs[6],
                           lhs7=lhs[7],rhs7=rhs[7],
                           lhs8=lhs[8],rhs8=rhs[8],)
if __name__ == "__main__":
    app.run(debug=True)