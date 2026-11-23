# === Stage 7: Сортировка записей ===
# Project: GreenhouseLog
from datetime import datetime


def sort_by_name(records, reverse=False):
    return sorted(records, key=lambda r: r["название"], reverse=reverse)


def sort_by_date(records, reverse=False):
    return sorted(records, key=lambda r: r["дата_создания"], reverse=reverse)


def sort_by_both(records, reverse=False):
    return sorted(
        records,
        key=lambda r: (r["дата_создания"], r["название"]),
        reverse=reverse,
    )
