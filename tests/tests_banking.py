import banking


def test_transaction():
    t=banking.Transaction(20)
    assert t.amount == 20


def test_transaction_repr():
    t=repr(banking.Transaction(40))
    assert t == 'Transaction(40)'
