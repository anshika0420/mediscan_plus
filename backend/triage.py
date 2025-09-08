# Simple rule-based triage logic based on symptom keywords.
def triage_from_symptoms(text: str) -> dict:
    s = text.lower()
    keywords_high = ['blood', 'severe', 'unconscious', 'collapse', 'bleeding', 'tumour', 'lump', 'mass', 'weight loss']
    keywords_medium = ['pain', 'persistent', 'cough', 'fever', 'fatigue', 'night sweat', 'loss of appetite']
    score = 0
    for kw in keywords_high:
        if kw in s:
            score += 3
    for kw in keywords_medium:
        if kw in s:
            score += 1
    if score >= 6:
        level = 'high'
    elif score >= 2:
        level = 'medium'
    else:
        level = 'low'
    return {"level": level, "score": score}
