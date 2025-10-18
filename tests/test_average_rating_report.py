import pytest
from src.main import AverageRatingReport


class TestAverageRatingReport:
    def test_generate_report(self, csv_data):
        result = AverageRatingReport().generate(csv_data)

        assert isinstance(result, list)
        assert isinstance(result[0], dict)
        assert len(result) == 3
        assert all(key in result[0] for key in ["brand", "average-rating"])


    def test_calculate_average_rating(self, csv_data):
        result = AverageRatingReport().generate(csv_data)

        apple_data = next(item for item in result if item["brand"] == "apple")
        assert apple_data["average-rating"] == 4.75

        samsung_data = next(item for item in result if item["brand"] == "samsung")
        assert samsung_data["average-rating"] == 4.65

        xiaomi_data = next(item for item in result if item["brand"] == "xiaomi")
        assert xiaomi_data["average-rating"] == 4.70


    def test_sorting_rating(self, csv_data):
        result = AverageRatingReport.generate(csv_data)

        ratings = [item["average-rating"] for item in result]
        assert ratings == sorted(ratings, reverse=True)


    def test_empty_data(self):
        result = AverageRatingReport.generate([])
        assert result == []
