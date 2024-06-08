from flask import render_template, request, Blueprint
from flask_login import login_required, current_user

from HAEstates.forms import FilterPropertyForm, AddProduceForm, BuyProduceForm, RestockProduceForm
from HAEstates.models import Produce as ProduceModel, ProduceOrder
from HAEstates.queries import insert_produce, get_produce_by_pk, Sell, \
    insert_sell, get_all_produce_by_farmer, get_produce_by_filters, insert_produce_order, update_sell, \
    get_orders_by_customer_pk

Property = Blueprint('Property', __name__)


@Property.route("/properties", methods=['GET', 'POST'])
def produce():
    form = FilterPropertyForm()
    title = 'Our properties!'
    produce = []
    if request.method == 'POST':
        produce = get_produce_by_filters(category=request.form.get('category'),
                                         item=request.form.get('item'),
                                         variety=request.form.get('variety'),
                                         farmer_name=request.form.get('sold_by'),
                                         price=request.form.get('price'))
        title = f'Our {request.form.get("category")}!'
    return render_template('pages/properties.html', produce=produce, form=form, title=title)

@Property.route("/Search Properties", methods=['GET', 'POST'])
def property():
    form = FilterPropertyForm()
    title = 'Our properties!'
    produce = []
    if request.method == 'POST':
        produce = get_produce_by_filters(category=request.form.get('category'),
                                         item=request.form.get('item'),
                                         variety=request.form.get('variety'),
                                         farmer_name=request.form.get('sold_by'),
                                         price=request.form.get('price'))
        title = f'Our {request.form.get("category")}!'
    return render_template('pages/search.html', produce=produce, form=form, title=title)

