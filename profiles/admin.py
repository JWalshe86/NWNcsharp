from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, UserAddress
from checkout.models import Order, OrderItems

# Register your models here.

"""
Admin configuration for managing User Profile model.
"""

# Define UserAddressInline to include UserAddress fields in the UserProfile admin
class UserAddressInline(admin.StackedInline):
    model = UserAddress
    extra = 1  # Number of empty address forms to display
    can_delete = True

# Inline admin for OrderItems
class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    readonly_fields = ('order_items_total',)
    extra = 0  # Number of empty forms to display

# Inline admin for Orders
class OrderInline(admin.TabularInline):
    model = Order
    inlines = [OrderItemsInline]
    extra = 0
    readonly_fields = ('order_number', 'order_date', 'delivery_charge', 'product_total', 'order_total', 'user_profile')
    can_delete = False
    verbose_name_plural = 'Orders'
    fields = ('order_number', 'order_date', 'delivery_charge', 'product_total', 'order_total')

# Define UserProfileInline to include UserProfile fields in the User admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    inlines = [UserAddressInline, OrderInline]  # Include inlines for addresses and orders

# Define UserProfileAdmin to include UserAddress and Orders
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [UserAddressInline, OrderInline]  # Include inlines for addresses and orders

    readonly_fields = ('user_id', 'phone', 'wishlist')

    list_display = ('user_id', 'phone')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('addresses', 'orders')

# # Unregister the default UserAdmin
admin.site.unregister(User)

# # Extend the UserAdmin class to include UserProfileInline
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)

# # Register the UserAdmin
admin.site.register(User, CustomUserAdmin)

# Register other models in the admin site
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserAddress)