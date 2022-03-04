# Unit Testing con Python

Una compañía utiliza una API para recolectar la información de perfil de usuarios en Twitter. Las respuestas que reciben de la API llegan en formato JSON, estas respuestas se almacenan en una capa cruda dentro de un Data Lake y de ahí son sometidas a un proceso de ETL para extraer la información de valor y almacenarla en una base de datos relacional sin embargo, hace falta una etapa de validación previa para saber si los JSON que serán el input de este proceso ETL no generarán problemas.

Crea un script de Unit Testing que verifique lo siguiente:
1. Que _typename = User

2. Que id tenga una longitud de 32 caracteres

3. Que rest_id únicamente este conformado por números

4. Que name no sea un dato vacío

5. Que screen_name no sea un dato vacío

6. Que las siguientes columnas sean de tipo entero:
   - fast_followers_count
   - favourites_count
   - followers_count
   - friends_count
   - listed_count
   - media_count
   - normal_followers_count
   - Statuses_count

El archivo adjunto user_info.json es un ejemplo de los JSON que debes validar con tu Unit Testing.

# Answers

Importamos las librerias *unittest* y *json*

Esto nos permite cargar el archivo .json para poder acceder a sus valores, lo cual lo asignamos a un diccionario de nombre _**data_dict**_

 ```Python
import re
import unittest
import json

url_file = open('new_user_info.json', 'r', encoding='utf-8')
data_dict = json.load(url_file)

 ```
 

### Exercise #1 
R/ Mediante  *self.assertEqual* hacemos una igualdad si la columna typename  es igual a 'User' , nos devuelve un True o False


 ```Python
def test_type_name(self):
        self.assertEqual(data_dict['data']['user']['result']['__typename'], 'User')
 ```

### Exercise #2
R/ Accedemos al valor de id y mediante *len* contamos cuantos caracteres tiene y con  *self.assertEqual* hacemos una igualda del valor obtenido si igual a 32 


 ```Python
 def test_size_id(self):
        self.assertEqual(len(data_dict['data']['user']['result']['id']), 32)
 ```


### Exercise #3
R/ Importamos la libreria *re* para usar expresiones regulares. Usamos *self.assertRegex* para comparar el valor de la columna rest_id si esta formada de numeros. La expresion ^[0-9]+ no ayuda a definir que desde el comienzo de la cadena hasta el final debe contener solo numeros. 

 ```Python
    def test_number_rest_id(self):
        self.assertRegex(data_dict['data']['user']['result']['rest_id'], r'^[0-9]+')
 ```

### Exercise #4
R/Mediante *self.assertIsNotNone* podemos validar que la columna name no esta vacia y nos devulve un valor True o False

 ```Python
  def test_none_name(self):
        self.assertIsNotNone(data_dict['data']['user']['result']['legacy']['name'])
 ```

### Exercise #5
R/Mediante *self.assertIsNotNone* podemos validar que la columna screen_name no esta vacia y nos devulve un valor True o False

 ```Python
  def test_none_screen_name(self):
        self.assertIsNotNone(data_dict['data']['user']['result']['legacy']['screen_name'])
 ```

### Exercise #6
R/Mediante *type* podemos conocer que tipo de dato tiene cada columna y con *self.assertIs* verificamos que el valor de la columna sea int

 ```Python
  def test_int_fast_followers_count(self):
        self.assertIs(type(data_dict['data']['user']['result']['legacy']['fast_followers_count']), int)
 ```

# Results

Ejecumos cada test y obtenemos la respuesta exitosa


