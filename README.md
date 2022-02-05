# Unit-Testing-Zophia-BootCamp-2022

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

![image](https://user-images.githubusercontent.com/46491988/152659538-f01a0bcd-d0e9-4fe9-9e25-8ac38a305aed.png)

### Exercise #1 
R/ Mediante  *self.assertEqual* hacemos una igualdad si la columna typename  es igual a 'User' , nos devuelve un True o False

![image](https://user-images.githubusercontent.com/46491988/152659617-bffee7aa-83e9-4cf4-a0b8-41bbfd45ec45.png)

### Exercise #2
R/ Accedemos al valor de id y mediante *len* contamos cuantos caracteres tiene y con  *self.assertEqual* hacemos una igualda del valor obtenido si igual a 32 

![image](https://user-images.githubusercontent.com/46491988/152659885-afa555b1-a303-455c-bc13-27fffecba523.png)

### Exercise #3
R/ Importamos la libreria *re* para usar expresiones regulares. Usamos *self.assertRegex* para comparar el valor de la columna rest_id si esta formada de numeros. La expresion ^[0-9]+ no ayuda a definir que desde el comienzo de la cadena hasta el final debe contener solo numeros. 

![image](https://user-images.githubusercontent.com/46491988/152659738-2304b1dc-9520-465e-b145-1e76ec97bff3.png)


### Exercise #4
R/Mediante *self.assertIsNotNone* podemos validar que la columna name no esta vacia y nos devulve un valor True o False

![image](https://user-images.githubusercontent.com/46491988/152659923-76702a2c-0d59-404f-b28e-73062b9904d0.png)

### Exercise #5
R/Mediante *self.assertIsNotNone* podemos validar que la columna screen_name no esta vacia y nos devulve un valor True o False

![image](https://user-images.githubusercontent.com/46491988/152659850-dac623ff-c2f8-431d-9a38-a2745775139a.png)


### Exercise #6
R/Mediante *type* podemos conocer que tipo de dato tiene cada columna y con *self.assertIs* verificamos que el valor de la columna sea int
![image](https://user-images.githubusercontent.com/46491988/152659999-3fecbad8-e3c9-469c-9052-d3656eb498db.png)


# Results

Ejecumos cada test y obtenemos la respuesta exitosa

![image](https://user-images.githubusercontent.com/46491988/152660048-65653a7b-f1a1-4a62-9041-e2bcf6a56f10.png)



