Iniciar o projeto Django

```
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
```

Configurar o git

```
git config --global user.name 'glauberdevlop'
git config --global user.email 'glaubercold53@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Adicionar comentarios'
git remote add origin URL_DO_GIT
```

Migrando a base de dados do Django

```
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário Django

```

python  manage.py createsuperuser
python manage.py changepassword USERNAME
```