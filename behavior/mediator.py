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


class WindowMediator(object):
    def __init__(self):
        self.windows = list()

    def show(self, win):
        for window in self.windows:
            if window is not win:
                window.hide()
        win.show()

    def add_window(self, window):
        self.windows.append(window)


main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

med = WindowMediator()
med.add_window(main_win)
med.add_window(setting_win)
med.add_window(help_win)

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
