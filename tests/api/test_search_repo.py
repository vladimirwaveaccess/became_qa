import uuid



def test_existing_repo_can_be_found(github_api_client):
    body = github_api_client.search_repo('become')
    print(f'Verification for total_count value, value is {body["total_count"]}')
    assert body['total_count'] > 0


def test_non_existing_repo_cannot_be_found(github_api_client):
    body = github_api_client.search_repo(uuid.uuid4())
    print(f'Verification for total_count value, value is {body["total_count"]}')
    assert body["total_count"] == 0


def test_search_not_working_without_q(github_api_client):
    body = github_api_client.search_repo_without_param()
    print("Check that request is not passed")
    assert body["message"] == 'Validation Failed'
