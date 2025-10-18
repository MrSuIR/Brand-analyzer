import pytest
from src.main import DataProcessor


class TestDataProcessor:
    def test_read_single_file(self, single_csv_file):
        processor = DataProcessor()
        processor.read_files([single_csv_file])

        assert isinstance(processor.data, list)
        assert isinstance(processor.data[0], dict)
        assert len(processor.data) == 5
        assert all(key in processor.data[0] for key in ["name", "brand", "price", "rating"])
        brands = [row["brand"] for row in processor.data]
        assert "apple" in brands
        assert "samsung" in brands
        assert "xiaomi" in brands


    def test_read_multiple_files(self, multiple_csv_files):
        processor = DataProcessor()
        processor.read_files(multiple_csv_files)

        assert isinstance(processor.data, list)
        assert isinstance(processor.data[0], dict)
        assert len(processor.data) == 5
        assert all(key in processor.data[0] for key in ["name", "brand", "price", "rating"])
        brands = [row["brand"] for row in processor.data]
        assert "apple" in brands
        assert "samsung" in brands
        assert "xiaomi" in brands


    def test_read_empty_files(self, empty_csv_file):
        processor = DataProcessor()
        processor.read_files([empty_csv_file])

        assert len(processor.data) == 0


    def test_read_nonexistent_file(self):
        processor = DataProcessor()

        with pytest.raises(FileNotFoundError):
            processor.read_files(["nonexistent_file.csv"])

