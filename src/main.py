import csv
from tabulate import tabulate
import argparse

class DataProcessor:
    def __init__(self):
        self.data: list = []

    def read_files(self, files_paths: list[str]) -> None:
        for file in files_paths:
            try:
                with open(file, "r") as f:
                    reader = csv.DictReader(f)
                    self.data.extend(list(reader))
            except FileNotFoundError:
                print(f"Ошибка: Файл '{file}' не найден")
                raise

class AverageRatingReport:
    @staticmethod
    def generate(data: list[dict]) -> list[dict]:
        brand_ratings: dict = {}

        for row in data:
            brand: str = row["brand"]
            rating: float = float(row["rating"])
            if brand not in brand_ratings:
                brand_ratings[brand] = []
            brand_ratings[brand].append(rating)

        report_data: list = []
        for brand, ratings in brand_ratings.items():
            avg_rating: float = sum(ratings) / len(ratings)
            report_data.append({
                "brand": brand,
                "average-rating": round(avg_rating, 2)
            })
        report_data.sort(key=lambda x: x["average-rating"], reverse=True)

        return report_data

class ReportRegistry:
    def __init__(self):
        self.reports = {
            "average-rating": AverageRatingReport()
        }

    def generate_report(self, report_name: str, data: list[dict]) -> list[dict]:
        if report_name not in self.reports:
            raise ValueError(f"Отчет '{report_name}' не поддерживается")

        return self.reports[report_name].generate(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="+", required=True)
    parser.add_argument("--report", required=True)

    try:
        args = parser.parse_args()
    except SystemExit:
        print("Ошибка: не указаны обязательные аргументы")
        return

    try:
        processor = DataProcessor()
        processor.read_files(args.files)

        report_registry = ReportRegistry()
        report_data = report_registry.generate_report(args.report, processor.data)

        headers: list = ["brand", "rating"]
        data: list = [[item["brand"], item["average-rating"]] for item in report_data]
        custom_indices = range(1, len(data) + 1)
        print(tabulate(data, headers, tablefmt="pretty", showindex=custom_indices, stralign="left"))

    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()