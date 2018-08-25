# coding: utf-8

"""
Посредник (Mediator) - паттерн поведения объектов.

Определяет объект, инкапсулирующий способ взаимодействия множества объектов.
Посредник обеспечивает слабую связанность системы, избавляя объекты от
необходимости явно ссылаться друг на друга и позволяя тем самым независимо
изменять взаимодействия между ними.
"""


class WindowBase(object):
    def show(self):
        raise NotImplementedError()

    def hide(self):
        raise NotImplementedError()


class MainWindow(WindowBase):
    def show(self):
        print('Show MainWindow')

    def hide(self):
        print('Hide MainWindow')


class SettingWindow(WindowBase):
    def show(self):
        print('Show SettingWindow')

    def hide(self):
        print('Hide SettingWindow')


class HelpWindow(WindowBase):
    def show(self):
        print('Show HelpWindow')

    def hide(self):
        print('Hide HelpWindow')


class AboutWindow(WindowBase):
    def show(self):
        print('Show AboutWindow')

    def hide(self):
        print('Hide AboutWindow')


class WindowMediator(object):
    """
    Набор окон, из которых видимо всегда только одно
    """
    def __init__(self):
        self.windows = list()

    def show(self, window_for_showing):
        """
        Показывает окно, предварительно скрывая остальные
        """
        for window in self.windows:
            if window is not window_for_showing:
                window.hide()
        window_for_showing.show()

    def add_windows(self, *windows):
        """
        Добавляет любое окно, если оно наследник от WindowBase
        """
        for window in windows:
            if isinstance(window, WindowBase):
                self.windows.append(window)


main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()
about_win = AboutWindow()

med = WindowMediator()
med.add_windows(main_win, setting_win, help_win, about_win)

print('--- Пример независимого показа окна (MainWindow)')
main_win.show()  # Show MainWindow

print('--- Теперь показ через Медиатор:')
print('- MainWindow (остальные окна скрываются Медиатором)')
med.show(main_win)
# Hide SettingWindow
# Hide HelpWindow
# Show MainWindow
print('- SettingWindow (остальные окна скрываются Медиатором)')
med.show(setting_win)
# Hide MainWindow
# Hide HelpWindow
# Show SettingWindow
print('- HelpWindow (остальные окна скрываются Медиатором)')
med.show(help_win)
# Hide MainWindow
# Hide SettingWindow
# Show HelpWindow
