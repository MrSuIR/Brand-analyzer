Скрипт для анализа CSV-файлов с данными о товарах и генерации отчетов по рейтингам брендов.

### Установка зависимостей
```
pip install -r requirements.txt
```

### Запуск
```
python src/main.py --files products1.csv products2.csv --report average-rating
```

### Пример запуска скрипта
<img width="1521" height="185" alt="image" src="https://github.com/user-attachments/assets/84a3a18d-af09-4f1f-96d0-e71478b267ed" />

### Добавление нового отчета
1) Создайте класс отчета с методом generate()
```
  class AveragePriceReport:
      @staticmethod
      def generate(data: list[dict]) -> list[dict]:
          # Логика расчета средней цены по брендам
          return report_data
```

2) Зарегистрируйте отчет в ReportRegistry:
```
  class ReportRegistry:
    def __init__(self):
        self.reports = {
            "average-rating": AverageRatingReport.generate,
            "average-price": AveragePriceReport.generate 
        }
```

3) Запуск нового отчета
```
  python src/main.py --files products1.csv products2.csv --report average-price
```

