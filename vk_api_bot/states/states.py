"""Модуль сохранения состояний пользователя"""

from transitions import Machine


class UserState:
    """
    Класс записи состояния пользователя
    """
    states = ["init", "main_menu", "viewing_category", "viewing_product"]

    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.current_category = None

    def set_category(self, category) -> None:
        """
        Функция класса сохраняет "категорию" в переменную
        """
        self.current_category = category

    def get_category(self) -> str:
        """
        Функция класса возвращает "категорию" из переменную
        """
        return self.current_category


def create_state_machine(user):
    """
    Создание машины состояний
    """
    machine = Machine(model=user, states=UserState.states, initial="init")
    machine.add_transition("start", "*", "main_menu")
    machine.add_transition("view_category", "*", "viewing_category")
    machine.add_transition("view_product", "*", "viewing_product")
    machine.add_transition("back_to_menu", "*", "init")
    return machine
