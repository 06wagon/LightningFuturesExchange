from shared.shared import db


class EquityPrice(db.Model):
    equity_Id = db.Column(db.Integer, primary_key=True, nullable=False)
    equity_price_id = db.Column(db.Integer, primary_key=True, nullable=False)
    price = db.Column(db.BigInteger, nullable=False)
    price_date = db.Column(db.DateTime(), nullable=False)
