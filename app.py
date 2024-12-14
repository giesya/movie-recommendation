from flask import Flask, render_template
import random
import os

app = Flask(__name__)

movie_recommendations = [
    "The 5th Wave",
    "Titanic", 
    "Alangkah Lucunya Negeri Ini",
    "Zathura",
    "Ready or Die"
]

@app.route('/')
def home():
    recommended_movie = random.choice(movie_recommendations)
    return render_template('index.html', movie=recommended_movie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))