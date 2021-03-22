
from django.urls import path
from .views import view_mobiles, view_details, user_registration, user_signin, \
    user_signout, place_order, view_orderline, view_orders, my_orders, create_mobiles, \
    admin_viewmobiles, update_mobiles,delete_mobiles, cancel_orders, check_status,\
    my_order, filter
urlpatterns = [
    path('register', user_registration, name='register'),
    path('create', create_mobiles, name='create'),
    path('view', view_mobiles, name='view'),
    path('detailed<int:id>', view_details, name='detailed'),
    path('signin', user_signin, name='signin'),
    path('signout', user_signout, name='signout'),
    path('order/<int:id>', place_order, name='order'),
    path('orders', view_orderline, name='orders'),
    path('vieworders/<int:id>', view_orders, name='vieworders'),
    path('my_order/<int:id>', my_orders, name='my_order'),
    path('myorder', my_order, name='myorder'),
    path('adminview', admin_viewmobiles, name='adminview'),
    path('edit<int:id>', update_mobiles, name='edit'),
    path('delete<int:id>', delete_mobiles, name='delete'),
    path('cancel/<int:id>', cancel_orders,name='cancel'),
    path('status/<int:id>', check_status, name='status'),
    path('filter', filter, name='filter')
]
