def stocks(selling_price, purchase_price, quantity):
    """
    Help on function stocks in moudle __main__:

    stocks(selling_price, purchase_price, quantity)
        매수가격(pruchase_price)과 매도가격(selling_price), 수량(quantity)을 매개변수로 가지고
        총손이(total_profit_and_loss)과 수익률(rate_of_return)을 반환하는 stocks() 함수입니다.
    """
    total_profit_and_loss = (selling_price-purchase_price) * quantity
    rate_of_return = selling_price / purchase_price * 100 - 100

    return total_profit_and_loss, rate_of_return

help(stocks())