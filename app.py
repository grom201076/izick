import json
from flask import make_response,session
from flask_restful import Resource, Api, reqparse
from flask import Flask
from ledger import Ledger



def output_json(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""
    resp = make_response(json.dumps(data, ensure_ascii=False), code)
    resp.headers.extend(headers or {})

    return resp

class BankBalanceResource(Resource):
    def get(self, bank):
        balance = ledger.bank_balance(bank)
        return {"balance": balance}
class PersonBalanceResource(Resource):
    def get(self, person):
        balance = ledger.person_balance(person)
        return {"balance": balance}
class AccountBalanceResource(Resource):
    def get(self, account):
        balance = ledger.account_balance(account)
        return {"balance": balance}

class TransactionsResource(Resource):
    def get(self):
        return {"records": ledger.records}
class TransferResource(Resource):
    def post(self, person, account, bank, person_to, account_to, bank_to, amount):
        balance = ledger.transfer(person, account, bank, person_to, account_to, bank_to, amount)
        return {"status": "ok"}

class MyApi(Api):
    def __init__(self, *args, **kwargs):
        super(MyApi, self).__init__(*args, **kwargs)
        self.representations = {
            'application/json': output_json,
        }


class BanksApi:

    def __init__(self, app, ledger, *args, **kwargs):
        api = MyApi(app)
        api.add_resource(BankBalanceResource,'/api/bank/<string:bank>/balance')
        api.add_resource(PersonBalanceResource,'/api/person/<string:person>/balance')
        api.add_resource(AccountBalanceResource,'/api/account/<int:account>/balance')
        api.add_resource(TransactionsResource,'/api/transactions')
        api.add_resource(TransferResource,
                '/api/transfer/<string:person>/<string:account>/<string:bank>/to'+
                '/<string:person_to>/<int:account_to>/<string:bank_to>/amount/<int:amount>'
                )


ledger = Ledger()
ledger.records = [
    ("Joe", 1, "BigBag", 1000),
    ("Mick", 2, "MoneyPile", 1000),
    ("Bob", 3, "BigBag", 1000),
    ("Alice", 4, "MoneyPile", 1000),
    ]
if __name__ == '__main__':
    app = Flask(__name__)
    api = BanksApi(app, ledger)
    app.run()

