# === Stage 8: Поиск по нескольким словам ===
# Project: GreenhouseLog
def find_bed(beds, query):
    """
    Поиск грядок по нескольким словам с поддержкой исключений.
    Токены вида "-слово" исключают записи, содержащие это слово;
    остальные токены требуют совпадения хотя бы одного из них.
    """
    exclude = [tok.strip()[1:] for tok in query.split() if tok.startswith("-")]
    must = [tok.strip() for tok in query.split() if not tok.startswith("-")]
    if not must:
        return list(beds)
    must_lower = {w.lower() for w in must}
    exclude_lower = {w.lower() for w in exclude}

    def contains(text, words):
        return any(word in text.lower() for word in words)

    return [bed for bed in beds if contains(bed["название"], must_lower) and not contains(bed["название"], exclude_lower)]


if __name__ == "__main__":
    beds = [
        {"название": "Томаты на южной грядке", "культура": "томат", "площадь": 2.0, "дата": "2024-03-10"},
        {"название": "Перец на северной грядке", "культура": "перец", "площадь": 1.5, "дата": "2024-03-12"},
        {"название": "Огурцы на западной грядке", "культура": "огурец", "площадь": 3.0, "дата": "2024-03-15"},
        {"название": "Баклажаны на восточной грядке", "культура": "баклажан", "площадь": 1.0, "дата": "2024-03-18"},
    ]

    print("Томаты:")
    for bed in find_bed(beds, "томаты"):
        print(f"  {bed['название']}")

    print("грядка -томаты:")
    for bed in find_bed(beds, "грядка -томаты"):
        print(f"  {bed['название']}")

    print("south:")
    for bed in find_bed(beds, "south"):
        print(f"  {bed['название']}")

    print("tomato -tomato:")
    for bed in find_bed(beds, "tomato -tomato"):
        print(f"  {bed['название']}")
