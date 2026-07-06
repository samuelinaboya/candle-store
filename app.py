import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# Mock database of the products shown in HOME PAGE.pdf and PRODUCT PAGE.pdf
PRODUCTS = {
    "eucalyptus": {
        "name": "Eucalyptus Stack 7 OZ Candle",
        "price": 28.00,
        "description": "Breathe in the crisp, refreshing aroma of eucalyptus. This clean and calming scent fills your space with notes of fresh greenery and cool botanicals...",
        "brings_out": "Freshness, clarity, and relaxation"
    },
    "sandalwood": {
        "name": "Sandalwood Stack 7 OZ Candle",
        "price": 32.00,
        "description": "Rich, warm, and woody notes to ground your space.",
        "brings_out": "Warmth, comfort, and sophistication"
    },
    "golden-mandarin": {
        "name": "Golden Mandarin Stack 7 OZ Candle",
        "price": 28.00,
        "description": "Bright, vibrant citrus blended with subtle cozy undertones.",
        "brings_out": "Energy, brightness, and warmth"
    }
}

@app.route('/')
def home():
    # Renders the homepage layout from "HOME PAGE.pdf"
    return render_template('home.html', products=PRODUCTS)

@app.route('/product/<id>')
def product(id):
    # Renders the individual product layout from "PRODUCT PAGE.pdf"
    product_data = PRODUCTS.get(id)
    if not product_data:
        return "Product not found", 404
    return render_template('product.html', product=product_data, product_id=id)

@app.route('/checkout')
def checkout():
    # Renders the checkout form from "PRODUCT PAGE-1.pdf"
    return render_template('checkout.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)