import flask
from flask import render_template

from utils import load_candidates_from_json, get_candidates_by_id, get_candidates_by_name, get_candidate_skill

app = flask.Flask(__name__)

@app.route("/")
def page_main():
  """Главная страница"""
  candidates: list[dict] = load_candidates_from_json()
  return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:idx>")
def page_candidate(idx):
  """Поиск кандидата по id"""
  candidate: dict = get_candidates_by_id(idx)
  if not candidate:
    return "Кандидат не найден"
  return render_template("card.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_skills(candidate_name):
  """Поиск кандидата по имени"""
  candidates: list[dict] = get_candidate_skill(candidate_name.lower())
  return render_template("search.html", candidates=candidates)


@app.route("/skill/<skill_name>")
def page_skills(skill_name):
  """Поиск кандидата по скиллу"""
  candidates: list[dict] = get_candidate_skill(skill_name.lower())
  return render_template("skill.html", candidates=candidates)

app.run()





















