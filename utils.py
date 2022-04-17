import json


def load_candidates(file_name: json) -> list:
    """
    :return: список кандидатов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def formatting(candidates: list) -> str:
    """
    :return: строку в формате 'Имя кандидата, Позиция кандидата, Навыки кандидата'
    """
    formatting_candidates = ''
    for candidate in candidates:
        formatting_candidates += (
            '<pre>'
            f'Имя кандидата - {candidate["name"]}\n'
            f'Позиция кандидата - {candidate["position"]}\n'
            f'Навыки кандидата - {candidate["skills"]}\n'
            '<pre>'
        )
    return formatting_candidates


def getting_id(candidates: list, candidate_id: str) -> any:
    """
    :return: кандидат по его id
    """
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def getting_skill(candidates: list, skill: str) -> list:
    """
    :return: список кандидатов по навыкам
    """
    candidates_skill = []
    for candidate in candidates:
        if skill.lower() in candidate["skills"].lower().split(', '):
            candidates_skill.append(candidate)
    return candidates_skill
