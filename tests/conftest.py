import csv
import os
import tempfile
import pytest


@pytest.fixture
def csv_data():
    return [
        {"name": "iphone 15 pro", "brand": "apple", "price": "999", "rating": "4.9"},
        {"name": "galaxy s23 ultra", "brand": "samsung", "price": "1199", "rating": "4.8"},
        {"name": "redmi note 12", "brand": "xiaomi", "price": "199", "rating": "4.7"},
        {"name": "iphone 14", "brand": "apple", "price": "899", "rating": "4.6"},
        {"name": "galaxy a54", "brand": "samsung", "price": "499", "rating": "4.5"}
    ]

@pytest.fixture
def single_csv_file(csv_data):
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "brand", "price", "rating"])
        writer.writeheader()
        writer.writerows(csv_data)
        temp_path = f.name

    yield temp_path
    os.unlink(temp_path)

@pytest.fixture
def multiple_csv_files(csv_data):
    file_paths = []

    first_half = csv_data[:3]
    second_half = csv_data[3:]

    for i, data in enumerate([first_half, second_half]):
        with tempfile.NamedTemporaryFile(mode='w', suffix=f'_{i}.csv', delete=False, newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "brand", "price", "rating"])
            writer.writeheader()
            writer.writerows(data)
            file_paths.append(f.name)

    yield file_paths

    for path in file_paths:
        os.unlink(path)

@pytest.fixture
def empty_csv_file():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "brand", "price", "rating"])
        writer.writeheader()
        temp_path = f.name

    yield temp_path
    os.unlink(temp_path)