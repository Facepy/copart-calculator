# الرسوم الثابتة
GATE_FEE = 95.00
TITLE_SHIPPING_FEE = 20.00
ENVIRONMENTAL_FEE = 15.00

# الرسوم المتغيرة للسيارات العادية
STANDARD_VEHICLES = [
    # تفاصيل الرسوم المتغيرة للسيارات العادية
]

# الرسوم المتغيرة للسيارات الثقيلة
HEAVY_VEHICLES = [
    # تفاصيل الرسوم المتغيرة للسيارات الثقيلة
]

# الرسوم الافتراضية للعروض
PRE_BID = [...]  # رسوم Pre-Bid
LIVE_BID = [...]  # رسوم Live Bid


# دالة حساب الرسوم
def calculate_fee(bid_amount, brackets, extra_fee=None):
    # المنطق الداخلي للحساب
    ...


# دوال مخصصة للسيارات العادية والثقيلة
def calculate_standard(bid_amount):
    ...


def calculate_heavy(bid_amount, is_clean_title):
    ...


def calculate_virtual_fee(bid_amount, bid_type):
    ...


def calculate_total_fees(bid_amount, is_heavy=False, is_clean_title=True, bid_type='pre'):
    ...
