from django.db import models

# Create your models here.

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UsuarioManager(BaseUserManager):

    #metodo para criação de usuarios
    def create_user(self, email, password=None):
        #variavel que set email de forma correta
        usuario = self.model(
            email=self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario


    #metodo para criação de superusuarios
    def create_superuser(self, email, password):
         #variavel que set email de forma correta
         usuario = self.create_user(
             email=self.normalize_email(email),
             password=password, 
         )
        
         usuario.is_active = True
         usuario.is_staff = True
         usuario.is_superuser = True

         usuario.set_password(password)

         usuario.save()

         return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name="E-mail do usuário", max_length=194, unique=True)

    is_active = models.BooleanField(verbose_name="O usuário esta ativo", default=True)

    is_staff = models.BooleanField(verbose_name="Usuário é da equipe de desenvolvimento", default=False)

    is_superuser = models.BooleanField(verbose_name="Usuário é um super usuario", default=False)

    USERNAME_FIELD  = "email"   

    objects = UsuarioManager() #direcionando o UsuarioManager para o AUTH_USER_MODEL no settings

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.email


