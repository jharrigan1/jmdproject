from flask import Flask, render_template, request
from Amazonprices import getAmazonNamePrice
from Costcoprices import getCostcoNamePrice
from Walmartprices import getWalmartPrice

app = Flask(__name__)

app.config['DEBUG'] = True

# @app.route('/', methods=['GET', 'POST'])
# def index():
    # return 'hello, world'

# @app.route('/amazon/', methods=['GET', 'POST'])
# def amazon_price():
#     if request.method == 'POST':
#         itemname = request.form['item']
#         aurl = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords={itemname}" .format(itemname=itemname)
        
#         iteminfo = getAmazonNamePrice(aurl)
        
#         if iteminfo is not None:
#             return render_template('results.html', item_info=iteminfo)
#         else:
#             return render_template('UI.html', error=True)
#     return render_template('UI.html', error=None)

@app.route('/', methods=['GET', 'POST'])
def costco_price():
    if request.method == 'POST':
        itemname = request.form['item']
        curl = "https://www.costco.com/CatalogSearch?dept=All&keyword={itemname}&pageSize=96" .format(itemname=itemname)        
        aurl = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords={itemname}" .format(itemname=itemname)
        wurl = "https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname)

        costconame, costcoinfo = getCostcoNamePrice(curl)
        itemname, iteminfo = getAmazonNamePrice(aurl)
        walmartinfo, walmartname = getWalmartPrice(wurl) 
        if costcoinfo and iteminfo is not None:
            return render_template('results.html', costconame=costconame, costco_info=costcoinfo, itemname=itemname, item_info=iteminfo, walmartname = walmartname, walmart_info =walmartinfo)
        else:
            return render_template('UI.html', error=True)
    return render_template('UI.html', error=None)

# @app.route('/walmart/', methods=['GET', 'POST'])
# def Walmart_price():
#     if request.method == 'POST':
#         itemname = request.form['item']
#         wurl = "https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname)
        
#         Walmartinfo = getWalmartPrice(wurl)
        
#         if Walmartinfo is not None:
#             return render_template('results.html', item_info=Walmartinfo)
#         else:
#             return render_template('UI.html', error=True)
#     return render_template('UI.html', error=None)

# @app.route('/compare/', methods=['GET', 'POST'])
# def all_prices():
#     if request.method == 'POST':
#         itemname = request.form['item']
#         curl = "https://www.costco.com/CatalogSearch?dept=All&keyword={itemname}&pageSize=96" .format(itemname=itemname)        
#         aurl = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=srs%3D7301146011%26search-alias%3Dpantry&field-keywords={itemname}" .format(itemname=itemname)
#         wurl = "https://www.walmart.com/search/?query={itemname}&cat_id=0" .format(itemname=itemname)
#         a_info = getAmazonNamePrice(aurl)
#         w_info = getWalmartPrice(wurl)
#         c_info = getCostcoNamePrice(curl)

#         item_list = [a_info,w_info, c_info]
#         price_list = [] 
#         item_price_dict = {}       
#         if item_list is not None:
#             return render_template('price_comparison.html', results=item_price_dict)
#         else:
#             return render_template('UI.html', error=True)
#     return render_template('UI.html', error=None)



if __name__ == '__main__':
    app.run()