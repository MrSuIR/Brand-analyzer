import pytest
from unittest.mock import patch
from src.main import main


class TestMain:
    def test_main_success(self, csv_data):
        test_args = [
            "main",
            "--files", "file1.csv", "file2.csv",
            "--report", "average-rating"
        ]

        with patch("sys.argv", test_args):
            with patch("src.main.DataProcessor") as MockProcessor:
                with patch("src.main.tabulate") as mock_tabulate:
                    with patch("builtins.print") as mock_print:

                        mock_processor_instance = MockProcessor.return_value
                        mock_processor_instance.data = csv_data

                        mock_tabulate.return_value = "отчет"

                        main()

                        MockProcessor.assert_called_once()
                        mock_processor_instance.read_files.assert_called_with(["file1.csv", "file2.csv"])
                        mock_tabulate.assert_called_once()
                        mock_print.assert_called_with("отчет")


    def test_main_no_required_arguments(self):
        test_args = ["main"]

        with patch("sys.argv", test_args):
            with patch("builtins.print") as mock_print:
                main()

                mock_print.assert_called_with("Ошибка: не указаны обязательные аргументы")


    def test_main_file_not_found(self):
        test_args = ["main", "--files", "file.csv", "--report", "average-rating"]

        with patch("sys.argv", test_args):
            with patch("src.main.DataProcessor") as MockProcessor:
                with patch("builtins.print") as mock_print:

                    mock_processor_instance = MockProcessor.return_value
                    mock_processor_instance.read_files.side_effect = FileNotFoundError("Ошибка: Файл file.csv не найден")

                    main()

                    mock_print.assert_called_once()
                    call_args = mock_print.call_args[0][0]
                    assert f"Ошибка: Файл file.csv не найден" in call_args


    def test_main_unsupported_report(self, csv_data):
        test_args = ["main", "--files", "file.csv", "--report", "average-price"]

        with patch("sys.argv", test_args):
            with patch("src.main.DataProcessor") as MockProcessor:
                with patch("src.main.ReportRegistry") as MockRegistry:
                    with patch("builtins.print") as mock_print:

                        mock_processor_instance = MockProcessor.return_value
                        mock_processor_instance.data = csv_data

                        mock_registry_instance = MockRegistry.return_value
                        mock_registry_instance.generate_report.side_effect = ValueError("Отчет average-price не поддерживается")

                        main()

                        mock_print.assert_called_once()
                        call_args = mock_print.call_args[0][0]
                        assert "Отчет average-price не поддерживается" in call_args