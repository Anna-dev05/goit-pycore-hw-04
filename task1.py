def total_salary(path: str) -> tuple:
    try:
        total = 0
        count = 0

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip() 
                if not line:
                    continue
                _, salary = line.split(",") 
                total += int(salary)
                count += 1

        if count == 0:
            return (0, 0)

        average = total / count
        return (total, average)

    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
        return (0, 0)

    except Exception as e:
        print(f"Помилка обробки файлу: {e}")
        return (0, 0)


if __name__ == "__main__":
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")




