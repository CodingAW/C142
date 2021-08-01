from flask import Flask, jsonify, request
import csv

allMovies = []

with open("movies.csv", encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

likedMovies = []
unlikedMovies = []
unwatchedMovies = []

app = Flask(__name__)


@app.route('/getData')
def getMovieData():
    return jsonify({
        "data": allMovies[0],
        "status": "Success"
    }, 400)


@app.route('/getLikedData', methods=['POST'])
def getLikedMovies(allMovies=allMovies):
    movie = allMovies[0]
    allMovies = allMovies[1:]
    likedMovies.append(movie)
    return jsonify({
        "status": "Success"
    }, 400)


@app.route('/getUnlikedData', methods=["POST"])
def getUnlikedMovies(allMovies=allMovies):
    movie = allMovies[0]
    allMovies = allMovies[1:]
    unlikedMovies.append(movie)
    return jsonify({
        "status": "Success"
    }, 400)

@app.route('/getUnwatchedData', methods=["POST"])
def getUnwatchedMovies(allMovies=allMovies):
    movie = allMovies[0]
    allMovies = allMovies[1:]
    unwatchedMovies.append(movie)
    return jsonify({
        "status": "Success"
    }, 400)


if __name__ == '__main__':
    app.run()
