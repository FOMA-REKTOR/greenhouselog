# === Stage 6: Фильтрация записей ===
# Project: GreenhouseLog
from datetime import date


def build_crop_filter(cultures, start_date=None, end_date=None):
    def filter_records(records):
        result = []
        for record in records:
            if record.get("культура") not in cultures:
                continue
            record_date = record.get("дата_посадки")
            if start_date is not None and record_date < start_date:
                continue
            if end_date is not None and record_date > end_date:
                continue
            result.append(record)
        return result
    return filter_records


def parse_date(value):
    if value is None:
        return None
    if isinstance(value, date):
        return value
    return date.fromisoformat(str(value)[:10])


def filter_bed_records(records, cultures, start_date=None, end_date=None):
    start_date = parse_date(start_date)
    end_date = parse_date(end_date)
    filter_fn = build_crop_filter(cultures, start_date, end_date)
    return filter_fn(records)


def display_filtered_records(records, cultures, start_date=None, end_date=None):
    print("=== Журнал грядок (отфильтровано) ===")
    if not records:
        print("Нет записей по заданным критериям.")
        return
    for record in records:
        print(f"Грядка: {record.get('название')}")
        print(f"  Культура: {record.get('культура')}")
        print(f"  Площадь: {record.get('площадь')}")
        print(f"  Дата посадки: {record.get('дата_посадки')}")
        print("-" * 30)
