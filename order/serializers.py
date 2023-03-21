from rest_framework import serializers
from order.models import Order
from order.send_mail import send_order_confirmation_code, send_order_owner_post

class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Order
        fields = '__all__'
    
    def create(self, validated_data):        
        order = Order.objects.create(**validated_data) # amout product
        send_order_confirmation_code(order.owner.email, order.activation_code, order.product.title, order.total_price)
        send_order_owner_post(order.product.owner, order.product.title, order.phone_number)
        return order
        
