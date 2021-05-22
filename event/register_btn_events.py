from view.main_view import Ui_MainWindow
from util.db_util import SqliteUtil
import os


class GlobalObj:
    target = None
    main_window = None
    login_view = None


class RegisterBtnEvents:
    QUERY_SQL = "select username from users where username = '%s'"
    INSERT_SQL = "insert into users (username, password) values ('%s', '%s')"

    @staticmethod
    def register_btn_event():
        username = GlobalObj.target.usernameEdit.text()
        password = GlobalObj.target.passwordEdit.text()
        re_password = GlobalObj.target.rePasswordEdit.text()

        if password != re_password:
            print("应该弹框提示两次密码不同")
            return

        if len(password) < 6:
            print("应该弹框提示密码长度短")
            return

        # 这里查数据库，判断用户是否存在，若存在则弹框提示

        connection = SqliteUtil.get_connection(os.path.abspath('./db/pet.db'))
        record = SqliteUtil.query(RegisterBtnEvents.QUERY_SQL % username, connection)

        if record and len(record) > 0:
            print("用户已经存在")
            return

        count = SqliteUtil.execute(RegisterBtnEvents.INSERT_SQL % (username, password), connection)
        if count > 0:
            print("保存成功了")

        # 最后注册成功则打开主界面
        main_view = Ui_MainWindow()
        main_view.setupUi(GlobalObj.main_window)
        GlobalObj.main_window.show()
