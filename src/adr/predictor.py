"""Adverse Drug Reaction predictor using simple rules."""

# Drug-ADR database (simplified)
ADR_DATABASE = {
    "warfarin": ["bleeding", "skin necrosis", "purple toe syndrome"],
    "clopidogrel": ["bleeding", "thrombotic thrombocytopenic purpura"],
    "metoprolol": ["bradycardia", "hypotension", "fatigue"],
    "simvastatin": ["myopathy", "rhabdomyolysis", "hepatotoxicity"],
}

def predict_adr_risk(drug: str, age: int, kidney_function: str = "normal") -> dict:
    """
    Predict ADR risk based on drug and patient factors.
    
    Returns:
        dict with risk_score, possible_adrs, recommendations
    """
    base_adrs = ADR_DATABASE.get(drug, ["unknown"])
    
    # Age adjustment
    age_risk = 0
    if age > 75:
        age_risk = 2
        age_note = "Elderly: increased sensitivity"
    elif age > 65:
        age_risk = 1
        age_note = "Geriatric: monitor closely"
    else:
        age_note = "Standard precautions"
    
    # Kidney adjustment
    kidney_risk = 0
    if kidney_function == "impaired":
        kidney_risk = 2
        kidney_note = "Renal impairment: dose adjustment needed"
    else:
        kidney_note = "Normal kidney function"
    
    total_risk = len(base_adrs) + age_risk + kidney_risk
    
    if total_risk >= 5:
        risk_level = "High"
        recommendation = "Consider alternative therapy or intensive monitoring"
    elif total_risk >= 3:
        risk_level = "Moderate"  
        recommendation = "Monitor for adverse effects"
    else:
        risk_level = "Low"
        recommendation = "Standard monitoring"
    
    return {
        "drug": drug,
        "risk_level": risk_level,
        "risk_score": total_risk,
        "possible_adrs": base_adrs,
        "recommendation": recommendation,
        "age_consideration": age_note,
        "kidney_consideration": kidney_note
    }
