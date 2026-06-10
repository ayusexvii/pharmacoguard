#!/usr/bin/env python3
"""PHARMACOGUARD - Personal pharmacogenomics assistant."""

import argparse
import sys
from src.cyp450.phenotyper import calculate_phenotype, predict_drug_response
from src.adr.predictor import predict_adr_risk

def main():
    parser = argparse.ArgumentParser(description="PHARMACOGUARD - Pharmacogenomics insights")
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # CYP2D6 phenotype command
    cyp_parser = subparsers.add_parser("phenotype", help="Predict CYP2D6 phenotype")
    cyp_parser.add_argument("allele1", help="First allele (e.g., *1, *4)")
    cyp_parser.add_argument("allele2", help="Second allele")
    
    # ADR prediction command
    adr_parser = subparsers.add_parser("adr", help="Predict ADR risk")
    adr_parser.add_argument("drug", help="Drug name")
    adr_parser.add_argument("--age", type=int, default=40, help="Patient age")
    adr_parser.add_argument("--kidney", choices=["normal", "impaired"], default="normal")
    
    # Drug response command
    resp_parser = subparsers.add_parser("response", help="Predict drug response")
    resp_parser.add_argument("drug", help="Drug name")
    resp_parser.add_argument("allele1", help="First allele")
    resp_parser.add_argument("allele2", help="Second allele")
    
    args = parser.parse_args()
    
    if args.command == "phenotype":
        result = calculate_phenotype(args.allele1, args.allele2)
        print(f"\n🧬 CYP2D6 Result:")
        print(f"   Genotype: {args.allele1}/{args.allele2}")
        print(f"   Phenotype: {result['phenotype']}")
        print(f"   Activity Score: {result['activity_score']}")
        print(f"   {result['interpretation']}")
        
    elif args.command == "adr":
        result = predict_adr_risk(args.drug, args.age, args.kidney)
        print(f"\n⚠️ ADR Risk Assessment for {args.drug}:")
        print(f"   Risk Level: {result['risk_level']}")
        print(f"   Possible ADRs: {', '.join(result['possible_adrs'])}")
        print(f"   {result['recommendation']}")
        
    elif args.command == "response":
        phenotype = calculate_phenotype(args.allele1, args.allele2)
        response = predict_drug_response(args.drug, phenotype['phenotype'])
        print(f"\n💊 Drug Response Prediction:")
        print(f"   Drug: {args.drug}")
        print(f"   Phenotype: {phenotype['phenotype']}")
        print(f"   Expected Response: {response}")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
