setup:

```
    cd <source folder>
    virtualenv -p python3 env
    source env/bin/activate
    pip install -r requirements.txt
```

run:

```
    python app.py
```

test:

```
    python test.py
```

test endpoints:

```
    curl -X POST http://localhost:5000/api/transfer/Joe/1/BigBag/to/Mick/2/MoneyPile/amount/1
    curl http://localhost:5000/api/account/1/balance
    curl http://localhost:5000/api/person/Mick/balance
    curl http://localhost:5000/api/bank/BigBag/balance
    curl http://localhost:5000/api/transactions
```




Assumptions and things out of scope:

* ledger records is not optimized or indexed - out of scope, easy to implement
* do not check account binding to bank - out of scope, easy to implement
* banks, accounts, persons are not classes - no reason in scope of task. 
    These entities have no responsibilities. They are just categories of record
* not all test are written - out of scope (time)
* no blackbox tests (api level). Couple of curl commands at the moment.
* transfer is done by url parameters. Could be made via for params. Depends on situation
* no option to explicitly create person / account / bank. That was not in the task.
    However person+Account+bank can be created implicitly via transfer

