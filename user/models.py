from django.db import models
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
	def create_user(self, email, password=None, is_staff=False, is_active=True, is_admin=False):
		if not email:
			raise ValueError('User must enter their email address')
		if not password:
			raise ValueError('User must enter a password')

		user_obj = self.model(
			email=email
		)

		user_obj.set_password(password)
		user_obj.staff = is_staff
		user_obj.admin = is_admin
		user_obj.active = is_active
		user_obj.save(using=self._db)
		
		return user_obj

	def create_staffuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
		)
		return user

	def create_superuser(self, email, password=None):
		user = self.create_user(
			email,
			password=password,
			is_staff=True,
			is_admin=True
		)
		return user


class User(AbstractBaseUser):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,14}$', message='phone number must be entered with country code without spaces.')
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	email = models.EmailField(max_length=254, unique=True)
	phone = models.CharField(validators=[phone_regex], max_length=15)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)
	active = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def fullname(self):
		if self.firstName and self.lastName:
			return self.firstName + self.lastName
		else:
			return self.email

	def __str__(self):
		return self.get_fullname, self.email

	def get_short_name(self):
		return self.firstName

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.staff

	@property
	def is_admin(self):
		return self.admin

	@property
	def is_active(self):
		return self.active
