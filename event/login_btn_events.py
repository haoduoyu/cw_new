from view.main_view import Ui_MainWindow
from view.register_view import Ui_RegisterWindow


class GlobalObj:
    target = None
    main_window = None


class LoginBtnEvents:
    def login_btn_event(self):
        main_view = Ui_MainWindow()
        main_view.setupUi(GlobalObj.main_window)
        GlobalObj.main_window.show()

    def register_btn_event(self):
        register_view = Ui_RegisterWindow()
        register_view.set_login_view(LoginBtnEvents)
        register_view.setupUi(GlobalObj.main_window)
        GlobalObj.main_window.show()
