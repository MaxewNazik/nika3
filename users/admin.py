from django.contrib import admin
from orders.admin import OrderTabulareAdmin

from users.models import User

admin.site.register(User)

inlines = [OrderTabulareAdmin]