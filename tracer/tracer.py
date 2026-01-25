import json
from datetime import datetime
categories_out = ['Без категории', 'Еда', 'Транспорт', 'Развлечения', 'Перевод']
categories_in = ['Без категории', 'Перевод', 'Зарплата']
try:
    with open('tracer.json', 'r') as f:
        data = json.load(f)
except:
    data = []

data.append({
    'sum': '200',
    'date': '14.12.12',
    'type': "Расходы",
    'category': 'Еда',
    'description': 'Нет'})
data.append({
    'sum': '10',
    'date': '13.01.20',
    'type': "Доход",
    'category': 'Без категории',
    'description': 'Нет'})
data.append({
    'sum': '700',
    'date': '12.10.25',
    'type': "Доход",
    'category': 'Зарплата',
    'description': 'Нет'})
data.append({
    'sum': '500',
    'date': '12.07.25',
    'type': "Расходы",
    'category': 'Транспорт',
    'description': 'Нет'})
data.append({
    'sum': '700',
    'date': '12.10.25',
    'type': "Доход",
    'category': 'Перевод',
    'description': 'Нет'})
data.append({
    'sum': '300',
    'date': '12.11.25',
    'type': "Расходы",
    'category': 'Без категории',
    'description': 'Нет'})
with (open('data.json', 'w')) as f:
    json.dump(data, f)

# def number(x):
#     # return [int(i) for i in x.split('.')]
#     # return x.strptime(x, '%d-%m-%y')
def updown(a):
    a.sort(key=lambda x: datetime.strptime(x['date'], '%d.%m.%y'))
    return a
def operations(spisok):
    for i, item in enumerate(spisok):
        print(i + 1, '-', item)
    cat = ''
    while cat not in [str(i) for i in range(1, len(spisok) + 1)]:
        cat = input('Введите номер категории: ')
    spisok = [i for i in spisok]
    cat = spisok[int(cat) - 1]
    print('')
    for i in data:
        if i['category'] == cat:
            print(f'Сумма: {i["sum"]}, Тип: {i["type"]}, Дата: {i["date"]}, Категория: {i["category"]}, Описание: {i["description"]}')
    print('')
while True:
    request = ''
    while request not in ['1', '2', '3', '4', '5']:
        request = input("1 - Добавить доход, 2 - Добавить расходы, 3 - Посмотреть итоговый баланс, 4 - История операций, 5 - Анализ\n")
    def get_operation(ink=-1):
        money = input('Введите сумму: \n')
        date = '134231124'
        while date[2] != '.' or date[5] != '.' or int(date[:2]) > 31 or int(date[3:5]) > 12:
            date = input('Введите дату в формате ДД.ММ.ГГ: \n')
        cat = ''
        if ink == 1:
            kk = [str(i) for i in range(len(categories_in) + 2)]
            for i, item in enumerate(categories_in):
                print(i, '-', item)
            print(kk[-1], '- Добавить категорию')
            while cat not in kk:
                cat = input('Введите номер категории: ')
            if cat == str(kk[-1]):
                g = input("Введите название категории: \n")
                categories_in.append(g)
            category = categories_in[int(cat) - 1]
        else:
            kk = [str(i) for i in range(len(categories_out) + 2)]
            for i, item in enumerate(categories_out):
                print(i, '-', item)
            print(kk[-1], '- Добавить категорию')
            while cat not in kk:
                cat = input('Введите номер категории: ')
            if cat == str(kk[-1]):
                g = input("Введите название категории: \n")
                categories_out.append(g)
            category = categories_out[int(cat) - 1]
        description = input('Введите описание: \n')
        return money, date, category, description
    match request:
        case '1':
            money, date, category, desc = get_operation(1)
            data.append({
                'sum': money,
                'type': 'Доход',
                'date': date,
                'category': category,
                'description': desc})
            with (open('data.json', 'w')) as f:
                json.dump(data, f)
            print('Сохранено')
        case '2':
            money, date, category, desc = get_operation()
            if int(money) > balance:
                print('\n!       На балансе недостаточно средств.       !\n')
            else:
                data.append({
                    'sum': money,
                    'type': 'Расходы',
                    'date': date,
                    'category': category,
                    'description': desc})
                with (open('data.json', 'w')) as f:
                    json.dump(data, f)
                print('Сохранено')
            #добавить расход
        case '3':
            balance = sum(int(t['sum']) if t['type'] == 'Доход' else -int(t['sum']) for t in data)
            print('Ваш баланс: ', balance)

            #росмотреть итоговый баланс
        case '4':
            filter_choice = ''
            while filter_choice not in ['0', '1', '2', '3', '4', '5']:
                filter_choice = input("Доступные фильтры: 0 - Без фильтров, 1 - Дата (Возрастание), 2 - Дата (Убывание), 3 - Категория (Доход), 4 - Категория (Расходы), 5 - Конкретная дата\n")
            print('')
            match filter_choice:
                case '0':
                    for i in data:
                        print(f'Сумма: {i["sum"]}, Тип: {i["type"]}, Дата: {i["date"]}, Категория: {i["category"]}, Описание: {i["description"]}')
                    print('')
                case '1':
                    for i in updown(data):
                        print(f'Сумма: {i["sum"]}, Тип: {i["type"]}, Дата: {i["date"]}, Категория: {i["category"]}, Описание: {i["description"]}')
                    print('')
                case '2':
                    for i in updown(data)[::-1]:
                        print(f'Сумма: {i["sum"]}, Тип: {i["type"]}, Дата: {i["date"]}, Категория: {i["category"]}, Описание: {i["description"]}')
                    print('')
                case '3':
                    spisok = set([i["category"] for i in data if i['type']=='Доход'])
                    operations(spisok)
                case '4':
                    spisok = set([i["category"] for i in data if i['type'] == 'Расходы'])
                    operations(spisok)
                case '5':
                    dates = set([i['date'] for i in updown(data)])
                    print('Cуществующие даты: ')
                    for i in dates:
                        print('  ', i)
                    print('')
                    date_filter = input('Введите дату в формате ДД.ММ.ГГ: \n')
                    for x in [i for i in data if i['date']==date_filter]:
                        print(f'Сумма: {x["sum"]}, Тип: {x["type"]}, Дата: {x["date"]}, Категория: {x["category"]}, Описание: {x["description"]}')
                    print('')
        case '5':
            filter_choice = ''
            while filter_choice not in ['0', '1', '2', '3', '4']:
                filter_choice = input("Доступный анализ: 1 - Расходы по категориям, 2 - Топ категорий расходов, 3 - Соотношение доходов и расходов\n")
            print('')
            match filter_choice:
                case '1':
                    outcomes_cat = {}
                    for i in data:
                        if i["type"] == "Расходы":
                            outcomes_cat[i["category"]] = outcomes_cat.get(i["category"], 0) + int(i["sum"])
                    if outcomes_cat:
                        print("Расходы по категориям:")
                        for cat, summ in sorted(outcomes_cat.items(), key=lambda x: x[1], reverse=True):
                            print(f"    {cat}: {summ}")
                    print('')
                case '2':
                    outcomes_cat = {}
                    for i in data:
                        if i["type"] == "Расходы":
                            outcomes_cat[i["category"]] = outcomes_cat.get(i["category"], 0) + int(i["sum"])
                    if outcomes_cat:
                        print("Топ 3 категории расходов:")
                        for cat, summ in sorted(outcomes_cat.items(), key=lambda x: x[1], reverse=True)[:3]:
                            print(f"    {cat}: {summ}")
                    print('')
                case '3':
                    total_income = sum(int(i['sum']) for i in data if i['type'] == "Доход")
                    total_outcome = sum(int(i['sum']) for i in data if i['type'] == "Расходы")
                    ratio = (total_outcome / total_income) * 100 if total_income > 0 else 100
                    print(f"Соотношение расходов к доходам: {int(ratio + 0.5)}%\n")
            #Анализ. Подсчет расходов по категоориям. Топ категорий расходов. Соотношение доходов и расходов