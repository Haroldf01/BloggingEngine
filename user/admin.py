from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib import admin

from .models import User
from .forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


class UserAdmin(BaseUserAdmin):
	# The forms to add and change user instances
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm

	# The fields to be used in displaying the User Model.
	# These override the definitions on the base UserAdmin
	# that references specific fields on the auth.User
	list_display = (User.fullname, 'email', 'admin')
	list_filter = ('staff', 'active', 'admin')
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal Info', {'fields': ('firstName', 'lastName', 'phone')}),
		('Permissions', {'fields': ('admin', 'staff')}),
	)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')
		})
	)

	search_fields = ('email', 'firstName', 'lastName')
	ordering = ('email', 'firstName')
	filter_horizontal = ()

	def get_inline_instance(self):
		if not obj:
			return list()
		return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)

# Remove group model
admin.site.unregister(Group)
