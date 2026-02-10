import pytest
from script import analyze_data


@pytest.fixture
def mock_meteorite_data():
    return [
        {
            "name": "Tiny Rock",
            "id": "1",
            "mass": "10",
            "year": "1990-01-01T00:00:00.000",
        },
        {
            "name": "Huge Rock",
            "id": "2",
            "mass": "1000",
            "year": "1990-01-01T00:00:00.000",
        },
        {
            "name": "Medium Rock",
            "id": "3",
            "mass": "500",
            "year": "2020-01-01T00:00:00.000",
        },
    ]


def test_analyze_data_logic(mock_meteorite_data):
    results = analyze_data(mock_meteorite_data)

    assert results["count"] == 3
    assert results["max_mass_name"] == "Huge Rock"
    assert results["max_mass_val"] == 1000
    assert results["top_year"] == "1990"
    assert results["top_year_count"] == 2
