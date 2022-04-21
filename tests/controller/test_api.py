class TestApi:
    def test_create_new_account(self, client):
        request_payload = {
            'user_id': '572ac805-aea8-4039-aaac-ee028e97b827',
            'deposit': 100.0
        }
        response = client.post("/accounts/create", json=request_payload)

        assert response.status_code == 200

    def test_create_new_account_missing_user_id(self, client):
        request_payload = {}
        response = client.post("/accounts/create", json=request_payload)

        assert response.status_code == 400

    def test_create_new_account_unknown_user(self, client):
        request_payload = {'user_id': '1'}
        response = client.post("/accounts/create", json=request_payload)

        assert response.status_code == 404

    def test_create_new_account_no_deposit(self, client):
        request_payload = {'user_id': '572ac805-aea8-4039-aaac-ee028e97b827'}
        response = client.post("/accounts/create", json=request_payload)

        assert response.status_code == 200

    def test_create_new_account_invalid_deposit(self, client):
        request_payload = {
            'user_id': '572ac805-aea8-4039-aaac-ee028e97b827',
            'deposit': -100.0
        }
        response = client.post("/accounts/create", json=request_payload)

        assert response.status_code == 400

    def test_get_balances_no_accounts(self, client):
        request_payload = {'user_id': '3c6289e7-1653-4f6e-a6c5-88b00d5c8a07'}
        response = client.get("/balances", json=request_payload)
        result = response.get_json()

        assert response.status_code == 200
        assert result is not []

    def test_get_balances(self, client):
        request_payload = {'user_id': '572ac805-aea8-4039-aaac-ee028e97b827'}
        response = client.get("/balances", json=request_payload)

        assert response.status_code == 200
        assert [acc['id'] in ['1', '2'] for acc in response.json]
        assert [acc['balance'] in ['250.0', '100.0'] for acc in response.json]

    def test_transfer(self, client):
        request_payload = {
            'from_id': '1',
            'to_id': '2',
            'amount': '100'
        }
        response = client.post("/accounts/transfer", json=request_payload)

        assert response.status_code == 200

    def test_transfer_invalid_payload(self, client):
        request_payload = {
            'from_id': '1',
            'amount': '100'
        }
        response = client.post("/accounts/transfer", json=request_payload)

        assert response.status_code == 400

    def test_transfer_invalid_amount(self, client):
        request_payload = {
            'from_id': '1',
            'to_id': '2',
            'amount': '-999'
        }
        response = client.post("/accounts/transfer", json=request_payload)

        assert response.status_code == 400
