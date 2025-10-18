Скрипт для анализа CSV-файлов с данными о товарах и генерации отчетов по рейтингам брендов.

### Установка зависимостей
```bash```
pip install -r requirements.txt

### Запуск
python src/main.py --files products1.csv products2.csv --report average-rating

### Прмиер запуска скрипта
<img width="1547" height="182" alt="image" src="https://github.com/user-attachments/assets/fcb496ce-0667-4234-b3ec-95377d1baf6f" />

### Добавление нового отчета
1) Создать класс отчета с методом generate()
  class AveragePriceReport:
      @staticmethod
      def generate(data: list[dict]) -> list[dict]:
          # Логика расчета средней цены по брендам
          return report_data

2) Зарегистрируйте отчет в ReportRegistry:
  class ReportRegistry:
    def __init__(self):
        self.reports = {
            "average-rating": AverageRatingReport.generate,
            "average-price": AveragePriceReport.generate 
        }

3) Запуск нового отчета
  python src/main.py --files products1.csv products2.csv --report average-price

