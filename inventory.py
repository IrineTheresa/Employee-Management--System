stocks=[15,3,0,22,8,1]
for stock in stocks:
    if stock==0:
        print(stock, "- Out of Stock")
    elif stock>=1 and stock<=5:
        print(stock, "- Restock Immediately")