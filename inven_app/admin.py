from django.contrib import admin

# Register your models here.

from .models import Question
from .models import Choice
from .models import Request
from .models import Location
from .models import Department
from .models import Status
from .models import Vendor
from .models import Purchase
from .models import Product
from .models import Approver
from .models import Post

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Request)
admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(Vendor)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Approver)
admin.site.register(Post)