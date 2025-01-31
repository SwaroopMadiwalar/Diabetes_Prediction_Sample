from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    # Dummy model: randomly predict 'Positive' or 'Negative'
    prediction = random.choice(['Positive', 'Negative'])
    return render_template('result.html', prediction_text='Predicted Result: {}'.format(prediction))

if __name__ == '__main__':
    app.run(debug=True)
