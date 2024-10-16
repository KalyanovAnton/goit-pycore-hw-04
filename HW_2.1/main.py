def total_salary(path):
    try:
        with open(path, encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                name, price = line.strip().split(',')
                total += int(price)
                count += 1
            if count == 0:
                return (0,0)
            average = total/count
            return(total, average)   
    except FileNotFoundError:
        print(f"Файл {path} не знайдено")
        return (0, 0)
    except ValueError:
        print(f"Помилка обробки даних у файлі {path}.")
        return(0, 0)
    except Exception as e:
        print(f"Виникла несподівана помилка: {e}")
        return (0, 0)
    

total, average = total_salary('D:\projects\HW\goit-pycore-hw-04\HM_2.1\workprice.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")