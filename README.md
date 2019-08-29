# poll-with-djangorest: Django poll with Django Rest

**Objetivos**:

   - Usar DjangoRest
   - Enteder que DjangoRest no sea magia negra
   - Tener autenticacion con JWT. 

## Descargando el repo.  

Descargar el repositorio con

```
$ git clone https://github.com/matiaslee/poll-with-djangorest.git
```
En la carpeta raiz del repo crear el virtualenv y levantarlo:

```
$ cd poll-with-djangorest/
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Hacer checkout del tag `part1.polls.app`:

```
$git checkout part1.polls.app
``` 

Levantar el server local de django e ingresar al admin: 

```
./manage.py runserver
```
Entrar a http://localhost:8000/admin

Usuario y password: `ingenieria` 



## Notas para la parte 1 de djangorest. 

Parte 1: https://www.django-rest-framework.org/tutorial/1-serialization/

Temas: Serializer. ModelSerializer.  Una api a mano. 

Hacer checkout del tag `part2.djangorest.part1`:

```
$git checkout part2.djangorest.part1
``` 

## Notas para la parte 2 de djangorest. 

Parte 2: https://www.django-rest-framework.org/tutorial/2-requests-and-responses/

Temas: Request Objects, Reponse Objects and Status Code. Api Browsability.

Hacer checkout del tag `part3.djangorest.part2`:

```
$git checkout part3.djangorest.part2
``` 


Comparando cambios principales: 
```
git diff 8e6dfe6d1959fdeaf3d8982746d9b2a1e16072d6 08327b31cd3d2ac1f2c95c4f09aabd73a142a6a7  views.py
```

## Notas para la parte 3 de djangorest. 

parte 3: https://www.django-rest-framework.org/tutorial/3-class-based-views/

Temas: Class Based Views, Mixins, Generic Class Based Views.

Hacer checkout del tag `part4.djangorest.part3.class_based_views`:

```
$git checkout part4.djangorest.part3.class_based_views
``` 

Hacer checkout del tag `part4.djangorest.part3.mixins`:

```
$git checkout part4.djangorest.part3.mixins
``` 

Hacer checkout del tag `part4.djangorest.part3.generic_class_based_views`:

```
$git checkout part4.djangorest.part3.generic_class_based_views
``` 

## Parte 4: Autenticación usando JWT. 

Tutorial: https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html

Temas: Autenticación usando JWT. 

 - Notar que en en la sección Further Reading hay un link que explica como usar JWT con react&redux. 

## Más

El tutorial de DjangoRest sigue. En la parte 4 se ve como filtrar contenido por usuario y otras formas de autenticación.:
 
https://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/