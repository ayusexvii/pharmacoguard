"""CYP450 phenotype prediction based on genotype."""

# CYP2D6 allele activity scores (simplified)
ALLELE_SCORES = {
    "*1": 1.0,   # normal function
    "*2": 1.0,   # normal function  
    "*3": 0.0,   # no function
    "*4": 0.0,   # no function
    "*5": 0.0,   # deletion, no function
    "*6": 0.0,   # no function
    "*9": 0.5,   # decreased function
    "*10": 0.5,  # decreased function
    "*17": 0.5,  # decreased function
    "*29": 1.0,  # normal function
    "*41": 0.5,  # decreased function
}

def calculate_phenotype(allele1: str, allele2: str) -> dict:
    """
    Calculate CYP2D6 phenotype from two alleles.
    
    Returns:
        dict with phenotype, score, and interpretation
    """
    score1 = ALLELE_SCORES.get(allele1, 1.0)
    score2 = ALLELE_SCORES.get(allele2, 1.0)
    total_score = score1 + score2
    
    if total_score == 0:
        phenotype = "Poor Metabolizer"
        interpretation = "Significantly reduced metabolism. Dose reduction recommended."
    elif total_score <= 1.0:
        phenotype = "Intermediate Metabolizer"
        interpretation = "Reduced metabolism. Monitor response."
    elif total_score == 2.0:
        phenotype = "Normal Metabolizer"
        interpretation = "Normal metabolism. Standard dosing."
    else:
        phenotype = "Ultra-rapid Metabolizer"
        interpretation = "Increased metabolism. May require higher dose."
    
    return {
        "phenotype": phenotype,
        "activity_score": total_score,
        "allele1": allele1,
        "allele2": allele2,
        "interpretation": interpretation
    }

def predict_drug_response(drug: str, phenotype: str) -> dict:
    """Predict response for specific drugs based on CYP2D6 phenotype."""
    drug_map = {
        "codeine": {
            "Poor Metabolizer": "Reduced efficacy (no pain relief)",
            "Intermediate Metabolizer": "Reduced efficacy",
            "Normal Metabolizer": "Normal efficacy",
            "Ultra-rapid Metabolizer": "Increased risk of toxicity"
        },
        "tamoxifen": {
            "Poor Metabolizer": "Reduced efficacy",
            "Intermediate Metabolizer": "Reduced efficacy", 
            "Normal Metabolizer": "Normal efficacy",
            "Ultra-rapid Metabolizer": "Normal efficacy"
        }
    }
    
    return drug_map.get(drug, {}).get(phenotype, "Data not available")
