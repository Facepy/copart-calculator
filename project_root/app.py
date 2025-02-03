from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "مرحبًا بك في آلة حساب العمولة - الموقع يعمل بشكل جيد!"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# هياكل بيانات العمولات والرسوم
standard_vehicle_fees = [...]
heavy_vehicle_fees = [...]
fixed_fees = {"gate_fee": 95.0, "title_shipping_fee": 20.0, "environmental_fee": 15.0}
virtual_bid_fees = [...]


@app.route('/')
def index():
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    bid_price = float(request.form['bid_price'])
    vehicle_type = request.form['vehicle_type']
    bid_type = request.form['bid_type']

    # حساب العمولة بناءً على النوع
    fees = standard_vehicle_fees if vehicle_type == "standard" else heavy_vehicle_fees
    commission = 0
    for start, end, fee in fees:
        if start <= bid_price <= end:
            commission = fee if fee < 1 else bid_price * fee
            break

    # حساب الرسوم الثابتة ورسوم المزايدة الافتراضية
    total_fixed_fees = sum(fixed_fees.values())
    virtual_fee = next((fee for start, end, fee in virtual_bid_fees if start <= bid_price <= end), 0)

    # حساب التكلفة الإجمالية
    total = bid_price + commission + total_fixed_fees + virtual_fee

    return render_template('result.html', total=total, bid_price=bid_price,
                           commission=commission, fixed_fees=total_fixed_fees, virtual_fee=virtual_fee)


if __name__ == '__main__':
    app.run(debug=True)
