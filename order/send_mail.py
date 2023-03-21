from django.core.mail import send_mail

def send_order_confirmation_code(email, code, name, price):
    full_link = f'Привет, подтверди заказ на продукт {name} на сумму {price}\n\n http://34.141.58.26/order/confirm/{code}'
    
    send_mail(
    'Order from FreeHub shop',
    full_link,
    'kasimmashrapov@gmail.com',
    [email]
    )