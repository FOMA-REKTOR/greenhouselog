# === Stage 3: Хранилище в памяти ===
# Project: GreenhouseLog
greenhouse_store.py

from datetime import date


class Bed:
    """Грядка теплицы."""

    def __init__(self, name, culture, area, planted_on):
        self.name = name
        self.culture = culture
        self.area = area
        self.planted_on = planted_on

    def __repr__(self):
        return (
            f"Bed(name={self.name!r}, culture={self.culture!r}, "
            f"area={self.area}, planted_on={self.planted_on})"
        )


class BedStore:
    """Хранилище грядок в памяти (словарь id -> Bed)."""

    def __init__(self):
        self._beds = {}
        self._counter = 0

    def add(self, name, culture, area, planted_on):
        """Добавить грядку и вернуть её уникальный идентификатор."""
        self._counter += 1
        bed_id = self._counter
        bed = Bed(name, culture, area, planted_on)
        self._beds[bed_id] = bed
        return bed_id

    def get(self, bed_id):
        """Вернуть грядку по идентификатору или None."""
        return self._beds.get(bed_id)

    def list_beds(self):
        """Вернуть список всех грядок в порядке добавления."""
        return list(self._beds.values())


if __name__ == "__main__":
    store = BedStore()

    id1 = store.add("Северная", "томаты", 1.5, date(2025, 3, 10))
    id2 = store.add("Южная", "перцы", 2.0, date(2025, 3, 12))

    print("Добавлено грядок:", id1, id2)

    print("Грядка 1:", store.get(id1))

    print("Список грядок:")
    for bed in store.list_beds():
        print(" ", bed)

    print("Отсутствует:", store.get(999))
