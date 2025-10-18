import pytest
from src.main import ReportRegistry, AverageRatingReport


class TestReportRegistry:
    def test_init(self):
        registry = ReportRegistry()

        assert isinstance(registry.reports, dict)
        assert isinstance(registry.reports["average-rating"], AverageRatingReport)
        assert "average-rating" in registry.reports


    def test_generate_report(self, csv_data):
        registry = ReportRegistry()

        supp_result = registry.generate_report("average-rating", csv_data)
        assert isinstance(supp_result, list)
        assert all(key in supp_result[0] for key in ["brand", "average-rating"])
        assert supp_result != []

        with pytest.raises(ValueError, match="Отчет 'average-price' не поддерживается"):
            registry.generate_report("average-price", csv_data)