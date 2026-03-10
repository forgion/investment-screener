import pytest
from src.normalize import normalize_values

def test_normalize_values_higher_is_better():
    result = normalize_values([10, 544, 34.5, 90], higher_is_better=True)
    assert result == pytest.approx([0, 100, 4.59, 14.98], abs=0.01)

def test_normalize_values_lower_is_better():
    result = normalize_values([10, 544, 34.5, 90], higher_is_better=False)
    assert result == pytest.approx([100, 0, 95.39, 85.02], abs=0.03)

def test_normalize_all_equal_values():
    assert normalize_values([10, 10, 10, 10], higher_is_better=True) == [50, 50, 50, 50]

def test_normalize_empty_values():
    assert normalize_values([]) == []

def test_normalize_invalid_type():
    with pytest.raises(TypeError):
        normalize_values([10, "30", 20, 50])

def test_normalize_bool_is_invalid():
    with pytest.raises(ValueError):
        normalize_values([10, True, 29])

def test_normalize_nan_is_invalid():
    with pytest.raises(ValueError):
        normalize_values([10, float("nan"), 29])