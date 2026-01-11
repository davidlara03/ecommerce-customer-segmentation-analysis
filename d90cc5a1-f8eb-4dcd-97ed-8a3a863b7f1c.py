#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-block alert-warning">
# <b>Comentario general del revisor</b> <a class="tocSkip"></a><br />
# Status del proyecto: <b>Aprobado</b>
#     
# Hubo algunas correcciones que he hecho en el proyecto, por favor revisalas, más allá de eso, me parece que es un buen trabajo el que entregas, continúa con el buen trabajo y mucho éxito en el siguiente Sprint!
# </div>
# 

# ¡Hola!<br />
# Soy **Francisco Cortés**, estoy contento de revisar tu proyecto y ser parte de tu proceso de aprendizaje.
# A lo largo del texto, haré algunas observaciones sobre mejoras en el código y también haré comentarios sobre tus percepciones sobre el tema. Si existe algún error en el código, no te preocupes, estoy aquí para ayudarte a mejorarlo, en la primera iteración te lo señalaré para que tengas la oportunidad de corregirlo, pero si aún no encuentras una solución para esta tarea, te daré una pista más precisa en la próxima iteración y también algunos ejemplos prácticos. Estaré abierto a retroalimentación y discusiones sobre el tema.<br />
# Encontrarás mis comentarios a continuación - **por favor no los muevas, modifiques o borres**.
# Revisaré cuidadosamente tu código para comprobar que se han cumplido con los requisitos y te proporcionaré mis comentarios en cajas verdes, amarillas o rojas como esta:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si la ejecución fue perfecta succesfully.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si existe alguna recomendación para que tu código mejore.
# </div>
# 
# <div class="alert alert-block alert-danger">
# 
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Si existen correcciones necesarias para cumplir con los requisitos. El trabajo no puede ser aceptado si hay alguna caja roja.
# </div>
# 
# Puedes responderme de la siguiente manera:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>
# </div>

# 
# 
# Como parte del equipo de análisis, lo primero que debes hacer es evaluar la calidad de una muestra de datos recopilados y prepararla para analizarla posteriormente. Después, en la segunda parte de este proyecto en el segundo sprint, desarrollarás más tus habilidades y harás tu primer análisis completo, respondiendo a las necesidades del cliente.

# Estos son los datos que el cliente nos proporcionó. Tienen el formato de una lista de Python, con las siguientes columnas de datos:
# 
# - **user_id:** Identificador único para cada usuario.
# - **user_name:** El nombre del usuario.
# - **user_age:** La edad del usuario.
# - **fav_categories:** Categorías favoritas de los artículos que compró el usuario, como 'ELECTRONICS', 'SPORT' y 'BOOKS' (ELECTRÓNICOS, DEPORTES y LIBROS), etc.
# - **total_spendings:** Una lista de números enteros que indican la cantidad total gastada en cada una de las categorías favoritas.
# 

# In[1]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


# # Paso 1
# 
# Store 1 tiene como objetivo garantizar la coherencia en la recopilación de datos. Como parte de esta iniciativa, se debe evaluar la calidad de los datos recopilados sobre los usuarios y las usuarias. Te han pedido que revises los datos recopilados y propongas cambios. A continuación verás datos sobre un usuario o una usuaria en particular; revisa los datos e identifica cualquier posible problema.
# 

# In[2]:


user_id = '32415'
user_name = ' mike_reed '
user_age = 32.0
fav_categories = ['ELECTRONICS', 'SPORT', 'BOOKS']


# **Opciones:**
# 
# 1. Se debe cambiar el tipo de dato de `user_id` de cadena a entero.
#     
# 2. La variable `user_name` contiene una cadena que tiene espacios innecesarios y un guion bajo entre el nombre y el apellido.
#     
# 3. El tipo de dato de `user_age` es correcto y no hay necesidad de convertirlo.
#     
# 4. La lista `fav_categories` contiene cadenas en mayúsculas. En lugar de ello, debemos convertir los valores de la lista en minúsculas.
# 

# Para cada una de las opciones, escribe en la siguiente celda markdown si la identificaste como un problema real en los datos o no. Justifica tu razonamiento. Por ejemplo, si crees que la primera opción es correcta, escríbelo y explica por qué piensas que es correcta.

# **Escribe tu respuesta y explica tu argumentación:**
# considero que la primera y la tercera opcion que en mi opinion pueden causar problemas ya que si se quieren de alguna forma crear listas o realizar operaciones aritmeticas , y si la variable no se encuentra bien definida pues podria provocar errores, por lo que considero que el dato user_id debe ser un entero y el user_age igual creo que manejar la edad como un flotante podria no ser lo mas adecuado 

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Bien hecho, las respuestas que has dado son correctas<br/>
# 
# 
# </div>
# 

# # Paso 2
# 
# Vamos a implementar los cambios que identificamos. Primero, necesitamos corregir los problemas de la variable `user_name` Como vimos, tiene espacios innecesarios y un guion bajo como separador entre el nombre y el apellido; tu objetivo es eliminar los espacios y luego reemplazar el guion bajo con el espacio.
# 

# In[3]:


user_name = ' mike_reed '
user_name = user_name.replace("_"," ")# escribe tu código aquí
user_name =user_name.strip() # escribe tu código aquí

print(user_name)


# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto!<br/>
# Buen uso de los métodos strip() y replace()
# </div>
# 

# ********Hint********
# 
# Existe un método, `strip()`, que puede eliminar espacios al principio y al final de una cadena. Además, el método `replace()` se puede usar para reemplazar una parte de una cadena. En este caso, queremos reemplazar los guiones bajos (`_`) con espacios.
# 

# # Paso 3
# 
# Luego, debemos dividir el `user_name` (nombre de usuario o usuaria) actualizado en dos subcadenas para obtener una lista que contenga dos valores: la cadena para el nombre y la cadena para el apellido.

# In[4]:


user_name = 'mike reed'
name_split = user_name.split( )# escribe tu código aquí

print(name_split)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto!<br/>
# Buen uso del método split()
# </div>

# ********Hint********
# 
# El método `split()` se utiliza para dividir una cadena. Por defecto, utiliza un espacio como separador.
# 

# # Paso 4
# 
# ¡Genial! Ahora debemos trabajar con la variable `user_age`. Como ya mencionamos, esta tiene un tipo de datos incorrecto. Arreglemos este problema transformando el tipo de datos y mostrando el resultado final.
# 

# In[16]:


user_age = 32.0
#user_age = user_age.int( ) # escribe tu código aquí

# Código del revisor
user_age = int(user_age)


print(user_age)


# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Cuidado!<br/>
# 
# La forma correcta de cambiar el dato a entero es usando `int()` como función, te he ayudado a corregir el código para que entiendas como usarlo
# </div>
# 

# In[ ]:





# ********Hint********
# 
# ¿Qué tipo de datos eliminará la parte de coma flotante? todos los datos despues del punto
# 

# # Paso 5
# 
# Como sabemos, los datos no siempre son perfectos. Debemos considerar escenarios en los que el valor de `user_age` no se pueda convertir en un número entero. Para evitar que nuestro sistema se bloquee, debemos tomar medidas con anticipación.
# 
# Escribe un código que intente convertir la variable `user_age` en un número entero y asigna el valor transformado a `user_age_int`. Si el intento falla, mostramos un mensaje pidiendo al usuario o la usuaria que proporcione su edad como un valor numérico con el mensaje: `Please provide your age as a numerical value.` (Proporcione su edad como un valor numérico.)

# In[15]:


user_age = 'treinta y dos'

try:
    usar_age_new= int(user_age)
    print(user_age_new)
except:
    #print("please provide your age as a numerical value."# escribe tu código aquí
    print("please provide your age as a numerical value.")


# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Cuidado!<br/>
# 
# Había un error en el código, faltaba cerrar el parentesis del print, te he ayudado a corregirlo
# </div>
# 

# ********Hint********
# 
# Utiliza un bloque `try-except` para intentar la conversión; si falla, proporciona un mensaje claro indicando que la entrada debe ser numérica.

# # Paso 6
# 
# El equipo de dirección de Store 1 te pidió ayudarles a organizar los datos de sus clientes para analizarlos y gestionarlos mejor.
# 
# Tu tarea es ordenar esta lista por ID de usuario de forma ascendente para que sea más fácil acceder a ella y analizarla.
# 

# In[14]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]

users.sort()# escribe tu código aquí

print(users)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto!<br/>
# Buena manera de utilizar el método sort()
# </div>
# 

# ********Hint********
# 
# Puedes utilizar el método `sort()` en la lista de usuarios para ordenarla de forma ascendente.
# 

# # Paso 7
# 
# Tenemos la información de los hábitos de consumo de nuestros usuarios, incluyendo la cantidad gastada en cada una de sus categorías favoritas. La dirección está interesada en conocer la cantidad total gastada por el usuario.
# 
# 
# Calculemos este valor y despleguémoslo.
# 

# In[8]:


fav_categories_low = ['electronics', 'sport', 'books']
spendings_per_category = [894, 213, 173]

total_amount = sum(spendings_per_category)# escribe tu código aquí

print(total_amount)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Bien hecho!<br/>
#     
# Correcto uso de la función `sum()`<br/>
# 
# </div>

# ********Hint********
# 
# ¿Cuáles son los tres métodos que se pueden aplicar a una lista para calcular sus valores mínimo, máximo y total?
# 

# # Paso 8
# 
# La dirección de la empresa nos pidió pensar en una manera de resumir toda la información de un usuario. Tu objetivo es crear una cadena formateada que utilice información de las variables `user_id`, `user_name` y `user_age`.
# 
# Esta es la cadena final que queremos crear: `User 32415 is mike who is 32 years old.` (El usuario 32415 es Mike, quien tiene 32 años).
# 

# In[10]:


user_id = '32415'
user_name = ['mike', 'reed']
user_age = 32

user_info = "user {} is {} who is {} years old".format(user_id,user_name[0],user_age)# escribe tu código aquí
print(user_info)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto!<br/>
# Buena manera de escribir una cadena personalizada
# </div>

# ********Hint********
# 
# Para crear una cadena, puedes utilizar el método `format()` o f-string. Para extraer el nombre de la lista `user_name`, puedes utilizar la segmentación.
# 

# # Paso 9
# 
# La dirección también quiere una forma fácil de conocer la cantidad de clientes con cuyos datos contamos. Tu objetivo es crear una cadena formateada que muestre la cantidad de datos de clientes registrados.
# 
# Esta es la cadena final que queremos crear: `Hemos registrado datos de X clientes`.
# 

# In[11]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['CLOTHES', 'ELECTRONICS', 'BEAUTY'], [299, 679, 85]],
    ['32984', 'David White', 41.0, ['BOOKS', 'HOME', 'SPORT'], [234, 329, 243]],
    ['33001', 'emily brown', 26.0, ['BEAUTY', 'HOME', 'FOOD'], [213, 659, 79]],
    ['33767', ' Maria Garcia', 33.0, ['CLOTHES', 'FOOD', 'BEAUTY'], [499, 189, 63]],
    ['33912', 'JOSE MARTINEZ', 22.0, ['SPORT', 'ELECTRONICS', 'HOME'], [259, 549, 109]],
    ['34009', 'lisa wilson ', 35.0, ['HOME', 'BOOKS', 'CLOTHES'], [329, 189, 329]],
    ['34278', 'James Lee', 28.0, ['BEAUTY', 'CLOTHES', 'ELECTRONICS'], [189, 299, 579]],
]


user_info = len(users)
mensaje = "We have registered data on {} clients".format(user_info)# escribe tu código aquí
print(mensaje)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Correcto!<br/>
# 
# Buena manera de usar `len()` para contar los elementos dentro de la lista<br/>
# </div>

# ********Hint********
# 
# Para crear una cadena, puedes utilizar el método `format()` o f-string. Para extraer la cantidad de clientes en la lista, puedes utilizar la función que devuelve la longitud de la lista.
# 

# # Paso 10
# 
# Apliquemos ahora todos los cambios a la lista de clientes. Para simplificar las cosas, te proporcionaremos una más corta.
# Debes:
# 1. Eliminar todos los espacios iniciales y finales de los nombres, así como cualquier guion bajo.
# 2. Convertir todas las edades en números enteros.
# 3. Separar todos los nombres y apellidos en una sublista.
# 
# Guarda la lista modificada como una nueva lista llamada `users_clean` y muéstrala en la pantalla.
# 

# In[12]:


users = [
    ['32415', ' mike_reed ', 32.0, ['ELECTRONICS', 'SPORT', 'BOOKS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['CLOTHES', 'BOOKS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRONICS', 'HOME', 'FOOD'], [459, 120, 99]],
]

users_clean = []


# Procesa al primer usuario
user_name_1 = users[0][1].strip().replace("_"," ")# escribe tu código aquí
user_age_1 = int(users[0][2])# escribe tu código aquí
user_name_1 = user_name_1.split(" ")# escribe tu código aquí
users_clean.append([users[0][0], user_name_1, user_age_1, users[0][3], users[0][4]])# escribe tu código aquí

# Procesa al segundo usuario
user_name_2 = users[1][1].strip() # escribe tu código aquí
user_age_2 = int(users[1][2])# escribe tu código aquí
user_name_2 = user_name_2.split(" ")# escribe tu código aquí
users_clean.append([users[1][0], user_name_2, user_age_2, users[1][3], users[1][4]])# escribe tu código aquí

# Procesa al tercer usuario
user_name_3 = users[2][1].strip()# escribe tu código aquí
user_age_3 = int(users[2][2])
user_name_3 = user_name_3.split(" ") # escribe tu código aquí
users_clean.append([users[2][0], user_name_3, user_age_3, users[2][3], users[2][4]])# escribe tu código aquí



print(users_clean)


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a><br />
# Bien hecho!<br/>
# 
# Has logrado agregar los datos limpios a una lista nueva de manera apropiada
# 
# </div>

# ********Hint********
# 
# Para procesar a cada usuario, comienza por acceder a los elementos requeridos de la lista de usuarios. Utiliza el método `strip()` para eliminar los espacios iniciales y finales y el método `replace('_',' ')` para reemplazar los guiones bajos por espacios en los nombres. Convierte la edad a un número entero utilizando `int()`. Separa el nombre completo en nombre y apellido utilizando el método `split()`. Por último, `append` (agrega) los datos limpios a la lista `users_clean`.
# 

# ----------
# 
