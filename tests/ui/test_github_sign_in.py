def test_failed_login(github_ui_client):
    login_page = github_ui_client.LoginPage

    login_page.go_to()
    login_page.try_sign_in('username', 'password')
    login_page.check_error_message()


    #github_ui_client.go_to_login_page()

    #github_ui_client.try_login_to_login_page()

    #github_ui_client.check_error_message()
