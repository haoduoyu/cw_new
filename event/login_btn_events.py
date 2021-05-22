from view.main_view import Ui_MainWindow
from view.register_view import Ui_RegisterWindow
from util.db_util import SqliteUtil
import os


class GlobalObj:
    target = None
    main_window = None


class LoginBtnEvents:
    QUERY_SQL = "select username from users where username = '%s' and password = '%s'"

    def login_btn_event(self):
        username = GlobalObj.target.usernameEdit.text()
        password = GlobalObj.target.passwordEdit.text()

        connection = SqliteUtil.get_connection(os.path.abspath('./db/pet.db'))
        record = SqliteUtil.query(LoginBtnEvents.QUERY_SQL % (username, password), connection)

        # 验证错误提示框弹出
        if not record or len(record) < 1:
            print("用户名或密码错误")
            return

        main_view = Ui_MainWindow()
        main_view.setupUi(GlobalObj.main_window)
        GlobalObj.main_window.show()

    def register_btn_event(self):
        register_view = Ui_RegisterWindow()
        register_view.set_login_view(LoginBtnEvents)
        register_view.setupUi(GlobalObj.main_window)
        GlobalObj.main_window.show()
