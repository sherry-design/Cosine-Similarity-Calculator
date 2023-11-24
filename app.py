from flask import Flask, request, render_template   
import numpy as np
from numpy.linalg import norm 


app = Flask(__name__)

# define a route to view the homepage where user can input the data
@app.route('/')
def index():
    # render index.html by passing value 2 for 2*2 vector
    return render_template('index.html',size=2) 

# define a route to submit the vector for similarity calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    
    
    try:
     a = 2
     A = np.array([float(request.form.get(f'a_{i}'))  if request.form.get(f'a_{i}') is not None else 0.0 for i in range(a)])
     B = np.array([float(request.form.get(f'b_{i}')) if request.form.get(f'b_{i}') is not None else 0.0 for i in range(a)])
     cosine = np.dot(A, B) / (norm(A) * norm(B))
     return f"Cosine Similarity: {cosine}"
    except ValueError:
     return "Invalid input for vector elements."

   

if __name__ == '__main__':
    # running the flask in debug mode
    app.run(debug=True)