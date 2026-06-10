def test_phenotype_scoring():
    scores = {"poor": 0, "intermediate": 1, "normal": 2}
    assert scores["normal"] == 2

def test_metabolism_rate():
    rate = 75  # percent
    assert rate > 50
