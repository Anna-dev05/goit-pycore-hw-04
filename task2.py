
def get_cats_info(path: str) -> list:
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cat_id, name, age = line.split(",")
                cats.append({"id": cat_id, "name": name, "age": age})
        return cats

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return []
    except Exception as e:
        print(f"Помилка обробки файлу: {e}")
        return []


if __name__ == "__main__":
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
