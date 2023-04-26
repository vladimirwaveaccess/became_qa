from datetime import datetime


def test_failed_login(github_ui_client):
    login_page = github_ui_client.LoginPage

    login_page.go_to()
    user_name = "username" + str(datetime.now().minute) + str(datetime.now().second)
    login_page.try_sign_in(user_name, 'password')
    assert login_page.get_error_message().strip() == "Incorrect username or password."


def test_successful_login(github_ui_client):
    login_page = github_ui_client.LoginPage

    login_page.go_to()
    login_page.try_sign_in('vladimirwaveaccess', 'password')
    sign_up_page = login_page.open_sign_up_page()
    sign_up_page.click_avatar()
    assert sign_up_page.get_user_name() == "vladimirwaveaccess"


def test_go_to_forgot_password_page(github_ui_client):
    login_page = github_ui_client.LoginPage

    login_page.go_to()
    login_page.click_to_forgot_pass_page()
    forgot_password_page = login_page.open_forgot_password_page()
    assert forgot_password_page.get_title_page().strip() == "Reset your password"
