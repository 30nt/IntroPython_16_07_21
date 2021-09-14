# стек (список)
# альтернатива рекурсии (множества)

# Шахматная доска 8х8. Конь. Стандартный ход. Старт "G2" Финиш "D5". Минимальное кол-во ходов.

def str_to_numb(position):
    letter = ord(position[0]) - ord("A") + 1
    number = int(position[1])
    return (letter, number)


def move(position): # Возвращает все возможные ходы из данной позиции с учетом размера доски.
    x, y = position
    m_1 = (x + 1, y + 2)
    m_2 = (x - 1, y + 2)
    m_3 = (x + 1, y - 2)
    m_4 = (x - 1, y - 2)
    m_5 = (x + 2, y + 1)
    m_6 = (x - 2, y + 1)
    m_7 = (x + 2, y - 1)
    m_8 = (x - 2, y - 1)
    points = [m_1, m_2, m_3, m_4, m_5, m_6, m_7, m_8]
    points = [point for point in points if (0 < point[0] < 9) and (0 < point[1] < 9)]
    return set(points)

start = "A1"
finish = "H3"
step = 0
colored_area = {str_to_numb(start), }  # Раскрашиваем первую клетку
new_points_to_move = colored_area
for step in range(1, 65):  # Считаем ходы. Костыль с for с ограничением количество ходов не больше чем размер нашей доски. Теоретически конь может ходить по кругу, а значит можем получить бесконечный цикл.
    after_move = set()     # Возможные позиции после хода будут скидываться в это множество
    for position in new_points_to_move:
        this_move = move(position)
        after_move.update(this_move)
    if str_to_numb(finish) in after_move:  # Если после этого хода мы попали в нужную точку - конец цикла.
        break
    new_points_to_move = after_move.difference(colored_area)  # Выбираем из полученных те позиции из которых еще не ходили
    colored_area.update(after_move)  # Красим все позиции, где побывал конь

print(step)






# def checkio(expression):
#     stack = []
#     pairs = {"(": ")", "[": "]",  "{": "}"}
#     for symbol in expression:
#         if symbol in pairs:
#             stack.append(symbol)
#         elif symbol in pairs.values():
#             if len(stack) == 0:
#                 return False
#             else:
#                 if pairs[stack[-1]] == symbol:
#                     stack.pop()
#                 else:
#                     return False
#     return len(stack) == 0
#
#
#
#
# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
#     assert checkio("((5+3)*2+1)") == True, "Simple"
#     assert checkio("{[(3+1)+2]+}") == True, "Different types"
#     assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
#     assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
#     assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
#     assert checkio("2+3") == True, "No brackets, no problem"
