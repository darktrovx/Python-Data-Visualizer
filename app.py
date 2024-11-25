import os
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request

# Use a non-interactive backend for matplotlib to avoid threading issues
plt.switch_backend('Agg')

app = Flask(__name__)

# Load a sample dataset (e.g., Titanic dataset for demonstration)
data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Preprocess data (optional)
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Fare'] = data['Fare'].fillna(data['Fare'].median())

def generate_plot(data, feature):
    # Ensure the static folder exists
    if not os.path.exists('static'):
        os.makedirs('static')

    plt.figure(figsize=(10, 5))
    if data[feature].dtype == 'object':
        # Bar plot for categorical data
        data[feature].value_counts().plot(kind='bar')
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
    else:
        # Histogram for numerical data
        data[feature].plot(kind='hist', bins=20, alpha=0.7)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Frequency')
    
    plt.tight_layout()
    plot_path = f'static/{feature}_plot.png'
    plt.savefig(plot_path)
    plt.close()
    return plot_path

@app.route('/')
def home():
    return render_template('index.html', columns=data.columns)

@app.route('/visualize', methods=['POST'])
def visualize():
    feature = request.form['feature']
    plot_path = generate_plot(data, feature)
    return render_template('visualize.html', feature=feature, plot_path=plot_path)

if __name__ == '__main__':
    app.run(debug=True)
