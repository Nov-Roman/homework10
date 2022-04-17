from flask import Flask
from utils import load_candidates, formatting, getting_id, getting_skill

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = load_candidates('candidates.json')
    return formatting(candidates)


@app.route("/candidates/<int:candidate_id>")
def page_candidates(candidate_id):
    candidates = load_candidates('candidates.json')
    candidate = getting_id(candidates, candidate_id)
    return f'<img src="{candidate["picture"]}">' + formatting(list(candidate))


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = load_candidates('candidates.json')
    candidates_skills = getting_skill(candidates, skill)
    return formatting(candidates_skills)


if __name__ == "__main__":
    app.run()
