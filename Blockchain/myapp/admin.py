from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.urls import reverse
from django.utils.html import format_html

# 🔴 Unregister default admin for User and Group
admin.site.unregister(User)
admin.site.unregister(Group)

# 🔧 Custom Delete Link Formatter (Red Button Style)
def red_delete_button(url):
    return format_html(
        '<a style="color: white; background-color: #dc3545; padding: 4px 10px; '
        'border-radius: 4px; text-decoration: none;" href="{}">Delete</a>', url
    )

# ✅ Custom User Admin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'last_login', 'delete_link')
    actions = ['custom_delete_selected_users']

    def delete_link(self, obj):
        url = reverse('admin:auth_user_delete', args=[obj.pk])
        return red_delete_button(url)
    
    delete_link.short_description = 'Delete'

    def custom_delete_selected_users(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} user(s) deleted successfully.")
    
    custom_delete_selected_users.short_description = "🗑️ Delete selected users"

# ✅ Custom Group Admin
@admin.register(Group)
class CustomGroupAdmin(GroupAdmin):
    list_display = ('name', 'delete_link')
    actions = ['custom_delete_selected_groups']

    def delete_link(self, obj):
        url = reverse('admin:auth_group_delete', args=[obj.pk])
        return red_delete_button(url)
    
    delete_link.short_description = 'Delete'

    def custom_delete_selected_groups(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"{count} group(s) deleted successfully.")

    custom_delete_selected_groups.short_description = "🗑️ Delete selected groups"
