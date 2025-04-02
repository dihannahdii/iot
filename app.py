from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///highscores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'player_name': self.player_name,
            'score': self.score,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S')
        }

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scores', methods=['GET'])
def get_scores():
    scores = HighScore.query.order_by(HighScore.score.desc()).limit(10).all()
    return jsonify([score.to_dict() for score in scores])

@app.route('/api/scores', methods=['POST'])
def add_score():
    data = request.get_json()
    new_score = HighScore(
        player_name=data['player_name'],
        score=data['score']
    )
    db.session.add(new_score)
    db.session.commit()
    return jsonify(new_score.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True) 