def stocks(selling_price, purchase_price, quantity):
    total_profit_and_loss = (selling_price-purchase_price) * quantity
    rate_of_return = selling_price / purchase_price * 100 - 100

    return total_profit_and_loss, rate_of_return


print(stocks(724, 780, 100))