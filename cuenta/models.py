from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

def get_profile_image_filepath(self):
    return f'profile_images/{self.pk}/{"profile_image.png"}'

def get_default_profile_image():
    return "virtuoso/static/images/home.png"

class Cuenta(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(verbose_name="usuario", max_length=30, unique=True)
    name = models.CharField(verbose_name="nombre", max_length=50)
    date_joined = models.DateTimeField(verbose_name="fecha de union", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="ultimo ingreso", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255,upload_to=get_profile_image_filepath,null=True, blank=True, default=get_default_profile_image)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    

    def __str__(self):
        return self.username
    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True

