from engine.spread_generator import generate_spreads
from engine.risk_model import evaluate_risk
from ai_layer.evaluator import ai_explain

def run_harvester():
    spreads = generate_spreads()
    results = []

    for spread in spreads:
        risk = evaluate_risk(spread)
        ai_notes = ai_explain(spread, risk)

        results.append({
            "spread": spread,
            "risk": risk,
            "ai": ai_notes
        })

    return results
