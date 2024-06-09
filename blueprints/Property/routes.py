from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
import re 

from HAEstates.forms import FilterPropertyForm
from HAEstates.queries import get_property_by_filters
from HAEstates.utils.search_data import df

Property = Blueprint('Property', __name__)

@Property.route("/properties", methods=['GET', 'POST'])
def property():
    form = FilterPropertyForm()
    title = 'Our properties!'
    property = []
    if request.method == 'POST':
        property = get_property_by_filters(type=form.p_type.data, beds=form.beds.data, baths=form.baths.data, stories=form.stories.data, sold_by=form.sold_by.data, price=form.price.data)
        title = f'Our {request.form.get("type")}!'
    return render_template('pages/properties.html', property=property, form=form, title=title)

@Property.route("/Search", methods=['GET'])
def search():
    query = request.args.get('query','')
    results = search_dataset(query)
    if query != '':
        return render_template('pages/results.html', query=query, results=results)
    else:
        return render_template('pages/search.html', query=query)

def search_dataset(query):
    pattern = re.compile(query, re.IGNORECASE)

    results = df[df['text'].str.contains(pattern)]

    return results.to_dict('records')