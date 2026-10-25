import pytest

from tracker import (
    add_record,
    calculate_total_minutes,
    search_records,
)


def test_add_record():
    records = []

    add_record(records, "2026-10-24", "Python", 60, "Programming")

    assert len(records) == 1
    assert records[0]["topic"] == "Python"
    assert records[0]["minutes"] == 60
    assert records[0]["category"] == "Programming"


def test_invalid_minutes():
    records = []

    with pytest.raises(ValueError):
        add_record(records, "2026-10-24", "Python", -10, "Programming")


def test_empty_topic():
    records = []

    with pytest.raises(ValueError):
        add_record(records, "2026-10-24", "", 60, "Programming")

def test_empty_category():
    records = []

    with pytest.raises(ValueError):
        add_record(records, "2026-10-24", "Python", 60, "")

def test_search_records_ignore_case():
    records = [
        {"date": "2026-10-24", "topic": "Python基础", "minutes": 60, "category": "Programming"},
        {"date": "2026-10-24", "topic": "Java基础", "minutes": 40, "category": "Programming"},
    ]

    results = search_records(records, "python")

    assert len(results) == 1
    assert results[0]["topic"] == "Python基础"



def test_calculate_total_minutes():
    records = [
        {"date": "2026-10-24", "topic": "Python", "minutes": 60, "category": "Programming"},
        {"date": "2026-10-24", "topic": "Java", "minutes": 40, "category": "Programming"},
    ]

    total = calculate_total_minutes(records)

    assert total == 100
