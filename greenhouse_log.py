# === Stage 1: Каркас модуля ===
# Project: GreenhouseLog
import datetime

class Gрядка:
    def __init__(self, название, культура, площадь, дата_посадки):
        self.название = название
        self.культура = культура
        self.площадь = площадь
        self.дата_посадки = дата_посадки

    def __str__(self):
        return f"{self.название} — {self.культура}, {self.площадь} м², с {self.дата_посадки}"


def make_demo_gрядки():
    return [
        Gрядка("Северная", "томаты", 4.5, datetime.date(2025, 4, 12)),
        Gрядка("Южная", "перцы", 3.0, datetime.date(2025, 4, 20)),
        Gрядка("Западная", "огурцы", 6.2, datetime.date(2025, 5, 2)),
    ]


def main():
    for gрядка in make_demo_gрядки():
        print(gрядка)


if __name__ == "__main__":
    main()
