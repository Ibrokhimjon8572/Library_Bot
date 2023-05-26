from django.contrib import admin
"""from .models import BotSettings, Post, TelegramUser, Channel, Transaction
from django.db.models import Sum
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter, AllValuesFieldListFilter
)






class TelegramUserAdmin(admin.ModelAdmin):
    model = TelegramUser
    list_display = ('phone', 'username', 'fullname', 'step', 'user_role', 'warning_time', 'referred_by', 'balance')
    fields =('id', 'user_id', 'fullname', 'username', 'phone', 'step', 'user_role', 'referal_code', 'referred_by', 'balance', 'warning_time')
    readonly_fields = ['id', 'user_id', 'username', 'fullname', 'language', 'referal_code', 'referred_by']
    search_fields = ('fullname', 'phone')
    list_filter = (
        ('user_role', DropdownFilter),
        ('referred_by', RelatedDropdownFilter),
        ('warning_time', DropdownFilter),
        ('balance', DropdownFilter),
    )

    def has_add_permission(self, request):
        return False

class ChannelAdmin(admin.ModelAdmin):
    model = Channel
    list_filter = ('is_active',)

class TransactionAdmin(admin.ModelAdmin):
    model = Transaction
    list_display = ('user', 'amount', 'time', 'status')
    # list_filter = ('status', 'user', 'time')
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('user', RelatedDropdownFilter),
        ('time', DropdownFilter),
    )
    readonly_fields = ['user', 'status']
    change_list_template = 'admin/custom_change_list.html'
    def get_total(self):
        #functions to calculate whatever you want...
        total = Transaction.objects.filter(status='accepted').aggregate(tot=Sum('amount'))['tot']
        return total

    def changelist_view(self, request, extra_context=None):
        my_context = {
            'total': self.get_total(),
        }
        return super(TransactionAdmin, self).changelist_view(request,
            extra_context=my_context)

class PostAdmin(admin.ModelAdmin):
    model = Post

class BotSettingsAdmin(admin.ModelAdmin):
    model = BotSettings

    def has_add_permission(self, request):
        return False
    

admin.site.register(TelegramUser, TelegramUserAdmin)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(BotSettings)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Post, PostAdmin)
"""
