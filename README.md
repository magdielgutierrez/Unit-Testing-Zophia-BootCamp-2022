# Unit-Testing-Zophia-BootCamp-2022

Una compañía utiliza una API para recolectar la información de perfil de usuarios en Twitter. Las respuestas que reciben de la API llegan en formato JSON, estas respuestas se almacenan en una capa cruda dentro de un Data Lake y de ahí son sometidas a un proceso de ETL para extraer la información de valor y almacenarla en una base de datos relacional sin embargo, hace falta una etapa de validación previa para saber si los JSON que serán el input de este proceso ETL no generarán problemas.


Crea un script de Unit Testing que verifique lo siguiente:
Que _typename = User
Que id tenga una longitud de 32 caracteres
Que rest_id únicamente este conformado por números
Que name no sea un dato vacío
Que screen_name no sea un dato vacío
Que las siguientes columnas sean de tipo entero:
fast_followers_count
favourites_count
followers_count
friends_count
listed_count
media_count
normal_followers_count
Statuses_count


El archivo adjunto user_info.json es un ejemplo de los JSON que debes validar con tu Unit Testing.
