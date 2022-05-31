import json

class Solution:
    def getValue(self,data,user_product):

        prod_sales={'A':[0]*5,'B':[0]*5,'C':[0]*5,'D':[0]*5,'E':[0]*5}

        country_name=['UK','USA','India','France','Germany']

        for i in data['sales']:
        
            (prod,country,sales)=i.values()

            prod_sales[prod][country_name.index(country)]+=sales

        return country_name[prod_sales[user_product].index(max(prod_sales[user_product]))],max(prod_sales[user_product])

if __name__ == '__main__':

    f = open('input_ios.json')
    data = json.load(f)

    user_product=input("Enter a product from among the following\n\nA/B/C/D/E\n\n").capitalize()

    s=Solution()
    print(s.getValue(data,user_product))


    