"""Tests for CYP450 phenotype prediction."""

import pytest
from src.cyp450.phenotyper import calculate_phenotype, predict_drug_response

def test_normal_metabolizer():
    """Test normal metabolizer phenotype."""
    result = calculate_phenotype("*1", "*1")
    assert result["phenotype"] == "Normal Metabolizer"
    assert result["activity_score"] == 2.0

def test_poor_metabolizer():
    """Test poor metabolizer phenotype."""
    result = calculate_phenotype("*4", "*4")
    assert result["phenotype"] == "Poor Metabolizer"
    assert result["activity_score"] == 0.0

def test_intermediate_metabolizer():
    """Test intermediate metabolizer."""
    result = calculate_phenotype("*1", "*4")
    assert result["phenotype"] == "Intermediate Metabolizer"
    assert result["activity_score"] == 1.0

def test_codeine_response():
    """Test codeine response prediction."""
    result = predict_drug_response("codeine", "Poor Metabolizer")
    assert "Reduced efficacy" in result

def test_edge_cases():
    """Test unknown alleles."""
    result = calculate_phenotype("*unknown", "*1")
    assert result["phenotype"] in ["Normal Metabolizer", "Intermediate Metabolizer"]
