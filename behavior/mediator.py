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
        self.windows = dict.fromkeys(['main', 'setting', 'help'])

    def show(self, win):
        for window in self.windows.values():
            if window is not win:
                window.hide()
        win.show()

    def set_main(self, win):
        self.windows['main'] = win

    def set_setting(self, win):
        self.windows['setting'] = win

    def set_help(self, win):
        self.windows['help'] = win


main_win = MainWindow()
setting_win = SettingWindow()
help_win = HelpWindow()

med = WindowMediator()
med.set_main(main_win)
med.set_setting(setting_win)
med.set_help(help_win)
print('---')
main_win.show()  # Show MainWindow
print('---')
med.show(main_win)
# Hide SettingWindow
# Hide HelpWindow
# Show MainWindow
print('---')
med.show(setting_win)
# Hide MainWindow
# Hide HelpWindow
# Show SettingWindow
print('---')
med.show(help_win)
# Hide MainWindow
# Hide SettingWindow
# Show HelpWindow
