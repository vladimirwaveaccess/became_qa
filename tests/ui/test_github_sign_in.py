def test_failed_login(github_ui_client):
    github_ui_client.go_to_login_page()

    github_ui_client.try_login_to_login_page()

    github_ui_client.check_error_message()
