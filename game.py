import os
import random
import time

# нам нужна функция
# чтобы красиво в зависимости от последней цифры возраста писало "год", "года" или "лет"
# например, "21 год", "22 года", "26 лет"
def years_view(some_age: int) -> str:
    age_suffix_list = ('год', 'года', 'лет')
    if some_age % 10 == 1:
        return f'{some_age} год'
    elif some_age % 10 in (2, 3, 4):
        return f'{some_age} года'
    elif some_age % 10 in (0, 5, 6, 7, 8, 9):
        return f'{some_age} лет'

os.system('cls' if os.name == 'nt' else 'clear')

# начнём игру с вводных данных, о мой король
name = input('Как Вас зовут? - ')
print('Добро пожаловать на трон,', name)
print('Вам всего 20 лет, желаем удачи в управлении страной!')
print()
print('Через 5 секунд мы начинаем!')
time.sleep(5)

# задаём начальные значения ресурсов
ground = random.randint(80, 120)
corn = random.randint(150, 220)
people = random.randint(40, 60)
start_year = 1420
end_year = random.randint(1460, 1490)

# основной цикл игры
while start_year < end_year:
    # в начале года очистим экран и покажем текущий статус
    os.system('cls' if os.name == 'nt' else 'clear')
    current_age = start_year - 1400
    print(f'{name}, Вам {years_view(current_age)}')
    print(f'У Вас имеется:\nЗемли - {ground}\nПшеницы - {corn}\nЛюдей - {people}')
    print()
    
    # вспомогательные переменные, которые каждый цикл пересчитываются
    free_people = 0
    corn_in_ground = 0
    bad_ground = 0
    
    # считаем сколько посеем пшеницы и сколько останется после посева
    game_values = ground, corn, people,
    max_corn_to_ground = min(game_values)
    corn_to_ground = int(input('Сколько будем сеять в этом году? - '))
    if corn_to_ground > max_corn_to_ground:
        print(f'''Мы не можем посеять столько пшеницы. У Вас нет в таком количестве либо пшеницы,
        либо земли, либо людей! Мы посеем всё, что возможно - {max_corn_to_ground} пшеницы.''')
        free_people = people - max_corn_to_ground
        corn_in_ground = max_corn_to_ground
        corn -= corn_in_ground
    elif corn_to_ground <= max_corn_to_ground:
        print(f'Отлично! Мы посеяли {corn_to_ground} пшеницы.')
        free_people = people - corn_to_ground
        corn_in_ground = corn_to_ground
        corn -= corn_in_ground
    
    print()
        
    # считаем, сколько отправить (или не отправить) на войну к соседям
    if free_people == 0:
        print('Отлично! Мы будем мирными в этом году!')
        people_to_war = 0
    else:
        people_to_war = int(input(f'У вас есть {free_people} не занятых людей. Сколько пошлём на войну к соседям? - '))
        if people_to_war > free_people:
            print(f'У вас нет столько не занятых людей. Отправляем {free_people} человек!')
            people -= free_people
        else:
            print(f'Отлично! Мы отправили на войну {people_to_war} человек.')
            people -= people_to_war
    
    print()
    print(f'Год {start_year} заканчивается, посмотрим на результаты?')
    print()
    
    # результат завоевательной войны
    chance_to_win = random.randint(1, 100)
    if chance_to_win >= 40 and people_to_war > 0:
        ground_win_in_war = people_to_war * 2
        corn_win_in_war = people_to_war * 4
        people_died_in_war = int(round(people_to_war * 0.5, 0))
        print(f'Поздравляем с победой в войне! Вы получаете {corn_win_in_war} пшеницы и {ground_win_in_war} земли')
        print(f'Однако в боях вы потеряли {people_died_in_war} человек')
        ground += ground_win_in_war
        corn += corn_win_in_war
        people += int(people_died_in_war * 0.5)
    elif chance_to_win < 40 and people_to_war > 0:
        people_died_in_war = int(round(people_to_war * 0.8, 0))
        print(f'Ваша военная авантюра обернулась поражением. Вы потеряли в боях {people_died_in_war} людей')
        people += int(people_to_war * 0.2)
    else:
        print('В этом году мы не ходили воевать и это здорово!')
    
    print()
    
    # результаты года по пшенице
    corn_from_ground = corn_in_ground * random.randint(3, 6)
    corn += corn_from_ground
    print(f'Вы получили урожай в размере {corn_from_ground} пшеницы')
    
    # если пшеницы не хватило на всех жителей, лишние умирают
    if people * 2 > corn:
        people = int(corn // 2)
        print(f'Сир. В стране голод. У нас хватило пшеницы только на {people} человек')
        corn_that_people_ate = corn
    else:
        corn_that_people_ate = people * 2
        
    print(f'Ваши люди съели {corn_that_people_ate} пшеницы')
    
    corn -= corn_that_people_ate
    print(f'Итого на конец года у вас {corn} пшеницы')
    
    print()
    
    # естественный прирост населения
    people = int(people * 1.33)
    print(f'Сир, население в стране увеличилось. Теперь у нас есть {people} человек')
    
    print()
    
    # случайные события в конце года
    random_actions = 'nothing', 'mouses', 'nothing', 'epidemy', 'nothing', 'enemies', 'baby_boom',
    what_happened = random.choice(random_actions)
    if what_happened == 'mouses':
        corn_eaten_by_mouse = int(corn * random.random() // 2)
        print(f"Сир! Проклятые мыши сожрали часть пшеницы в амбарах! Вы потеряли {corn_eaten_by_mouse} пшеницы!")
        corn -= corn_eaten_by_mouse
        print(f'Итого на конец года у вас {corn} пшеницы')
    elif what_happened == 'epidemy':
        people_died_by_epidemy = int(people * random.random() // 3)
        print(f'Сир! В стране разразилась эпидемия, погибло {people_died_by_epidemy} человек!')
        people -= people_died_by_epidemy
    elif what_happened == 'enemies':
        print('Сир! На нас напали соседи! Мы должны дать отпор!')
        enemies = int(random.random() * people)
        print(f'Мы обнаружили врагов. Их {enemies} человек')
        chance_to_win_enemies = int(random.random() * 100)
        print(f'Шанс на победу {chance_to_win_enemies}%. Есть два варианта: откупиться зерном или воевать.')
        action_for_enemies = int(input('Введите 1, чтобы откупиться, введите 2, чтобы воевать: '))
        if action_for_enemies == 1:
            print('Хорошо, давайте откупимся. Враги забирают половину нашего зерна =(')
            corn -= corn // 2
        elif action_for_enemies == 2:
            print('Ваша храбрость беспримерна, Сир! Дадим врагу отпор!')
            if chance_to_win_enemies <= 50 and enemies > people // 2:
                print('К сожалению врагов было слишком много, Сир. Мы проиграли битву и должны выплатить дань')
                people_died_by_enemies = int(people * random.random() // 2)
                print(f'Мы потеряли в боях {people_died_by_enemies} человек =(')
                corn_to_enemies = int(corn * random.random() // 2)
                ground_to_enemies = int(ground * random.random() // 4)
                print(f'Мы отдали врагу выкуп - {corn_to_enemies} пшеницы и {ground_to_enemies} земли =(')
                print('Это огромное горе, Сир!')
            elif chance_to_win_enemies <= 50 and enemies < people // 2:
                slaves = int(enemies * random.random() // 2)
                people_died_by_enemies = int(people * random.random() // 3)
                print(f'Сир. Это была тяжелая битва, мы потеряли {people_died_by_enemies} человек, но мы победили и захватили {slaves} пленников, которые пополнят наше население')
                people = people + slaves - people_died_by_enemies
            elif chance_to_win_enemies > 50:
                print('Мы отбились, Сир. Это победа! Но день победы горечью пропах...')
                people_died_by_enemies = int(people * random.random() // 4)
                print(f'Мы потеряли в боях {people_died_by_enemies} человек, но к счастью сохранили все запасы зерна.')
    elif what_happened == 'baby_boom':
        people_by_baby_boom = int(people * 1.3)
        print(f'Сир, какое счастье! В стране бэби бум, население увеличилось на {people_by_baby_boom} человек')
        people += people_by_baby_boom
    elif what_happened == 'nothing':
        print('Год заканчивается спокойно, Сир. Без проишествий и неожиданностей. С Новым Годом, Сир!')
    
    print()
        
    start_year += 1
    
    print('Пауза 10 сек на отдых перед следующим годом!')
    time.sleep(10)

print(f'На {current_age + 1} году жизни вы тихо скончались в своём замке... Король умер!')
print()
print('Давайте подведём итоги вашего правления, итак:')
print()
print(f'Вы имеете {ground} земли')
print(f'Вы имеете {corn} пшеницы в амбарах')
print(f'У вас {people} населения')