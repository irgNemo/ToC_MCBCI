# %% [markdown]
# #Variables globales

# %%
import re

file_name = "turing_correct.def"
f_regex = "(f)\s*=\s*{(\(.*\)->\(.*\)(,\(.*\)->\(.*\))*)}"
sigma_regex = "(sigma)\s*=\s*{([a-zA-Z0-9](,[a-zA-Z0-9])*)}"

regex_list = [f_regex, sigma_regex]

# %%
with open(file_name) as my_file:
    content_file = my_file.read()

turing_machine_tuples = {}
for regexp in regex_list:
    matcher = re.compile(regexp)
    match = matcher.search(content_file) # Observen como cambie el métdod match por el de search, para que lo busque en todo el contenido del documento
    print("Resultado de invocar el metodo groups() de match: ", match.groups()) # El método group() regresa todos los grupos formados en la expresion regular, en este caso el primero corresponde al nombre de la variable (sigma, f, ...) y el segundo al valor dentro de los corchetes ((q0 0)->(q1 X R),(q0 Y)->(q3 Y R), ...) o (0,1, ... )
    tuple_name = match.groups()[0]
    tuple_value = match.groups()[1]
    print("Nombre de la tupla: ", tuple_name, " Valor de la tupla: ", tuple_value)

    turing_machine_tuples[tuple_name] = tuple_value #Aqui genero un diccionario para poder acceder a la informacion que quiera por el nombre de la variable

print(turing_machine_tuples) #Imprime todo el diccionario
print(turing_machine_tuples["f"]) #Imprime el contenido de la llave f que esta en el diccionario

# A partir de aqui esta el código para separar funcion de transicion y poder accedes a ella por medio de un diccionario

f_string = turing_machine_tuples["f"]
f_list_by_coma = transition_string.split(",")
print(f_list_by_coma)
transition_matrix = {token.split("->")[0]: token.split("->")[1] for token in f_list_by_coma} # Separa los token en un diccionario para accederlo
print(transition_matrix) 

# Con el diccionario transition_matrix ustedes podran preguntar que hacer cuando estan en un estado y reciben un caracter de la cadena de prueba

test_string = "00"
current_state = "q0"
for character in test_string:
    new_key = "({0} {1})".format(current_state, character)
    print(new_key) # Imprime la llave creada para acceder al diccionario
    next_actions = transition_matrix[new_key] # Accede a los movimientos que se necesitan hacer en la cinta y en el estado actual
    print(next_actions)
    # Ya que tienen las demas acciones, tiene que ejecutar las acciones que indican, por ejemplo, pasar a un estado, escribir en la cinta y moverse a la derecha/izquierda

    


