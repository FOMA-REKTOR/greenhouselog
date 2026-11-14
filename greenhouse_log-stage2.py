# === Stage 2: Проверка полей ===
# Project: GreenhouseLog
greenhouse_fields.py

from datetime import date


class FieldError(Exception):
    """Ошибка валидации полей сущности «грядка»."""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


def normalize_name(value):
    """Нормализация названия грядки: убираем пробелы по краям и внутри."""
    cleaned = value.strip()
    cleaned = " ".join(cleaned.split())
    return cleaned


def normalize_crop(value):
    """Нормализация культуры: приводим к нижнему регистру и убираем лишние пробелы."""
    cleaned = value.strip().lower()
    cleaned = " ".join(cleaned.split())
    return cleaned


def normalize_area(value):
    """Нормализация площади: убираем лишние пробелы и переводим в число."""
    cleaned = value.strip()
    return float(cleaned)


def normalize_date(value):
    """Нормализация даты посадки: приводим к формату ГГГГ-ММ-ДД."""
    cleaned = value.strip()
    return date.fromisoformat(cleaned)


def validate_field(name, value, expected_type, normalizer):
    """Проверка одного поля с нормализацией и понятным сообщением об ошибке."""
    if value is None or (isinstance(value, str) and value.strip() == ""):
        raise FieldError(f"Поле {name} не может быть пустым.")

    cleaned = normalizer(value)

    if not isinstance(cleaned, expected_type):
        raise FieldError(
            f"Поле {name} должно содержать значение типа {expected_type.__name__}, "
            f"а получено: {value!r}."
        )

    return cleaned


def validate_garden(name, crop, area, planting_date):
    """Валидация всех полей сущности «грядка».

    Возвращает нормализованные значения полей в том же порядке.
    """
    normalized_name = validate_field(
        "название", name, str, normalize_name
    )
    if normalized_name == "":
        raise FieldError("Название грядки не может быть пустым.")

    normalized_crop = validate_field(
        "культура", crop, str, normalize_crop
    )
    if normalized_crop == "":
        raise FieldError("Культура не может быть пустой.")

    normalized_area = validate_field(
        "площадь", area, float, normalize_area
    )
    if normalized_area <= 0:
        raise FieldError("Площадь грядки должна быть положительным числом.")

    normalized_date = validate_field(
        "дата посадки", planting_date, date, normalize_date
    )

    return normalized_name, normalized_crop, normalized_area, normalized_date
