#!/usr/bin/env python3
"""PHARMACOGUARD Demo - Showcases all features."""

print("=" * 60)
print("🩺 PHARMACOGUARD - Personal Pharmacogenomics Assistant")
print("=" * 60)

print("\n📋 Patient Cases:")
print("-" * 40)

# Case 1: Normal metabolizer
print("\n1️⃣ Patient A: Normal CYP2D6 Metabolizer (*1/*1)")
print("   → Codeine: Normal efficacy")
print("   → Warfarin: Standard dosing")

# Case 2: Poor metabolizer  
print("\n2️⃣ Patient B: Poor CYP2D6 Metabolizer (*4/*4)")
print("   → Codeine: No pain relief (alternative needed)")
print("   → Tamoxifen: Reduced efficacy")
print("   → Metoprolol: Increased bradycardia risk")

# Case 3: Ultra-rapid metabolizer
print("\n3️⃣ Patient C: Ultra-rapid CYP2D6 Metabolizer (*1/*1xN)")
print("   → Codeine: Toxicity risk (avoid)")
print("   → Most drugs require higher doses")

print("\n" + "=" * 60)
print("💡 Next Steps:")
print("   • pharmacoguard.py phenotype *1 *4")
print("   • pharmacoguard.py adr warfarin --age 70")
print("   • pharmacoguard.py response codeine *4 *4")
print("=" * 60)

# Run actual predictions
print("\n🔬 Live Predictions:")
print("-" * 40)

import sys
sys.path.insert(0, '.')
from src.cyp450.phenotyper import calculate_phenotype, predict_drug_response

result = calculate_phenotype("*1", "*4")
print(f"\n• CYP2D6 *1/*4: {result['phenotype']}")
print(f"  {result['interpretation']}")

response = predict_drug_response("codeine", result['phenotype'])
print(f"• Codeine response: {response}")
