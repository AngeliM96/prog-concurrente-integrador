# Trabajo práctico integrador - Programación Concurrente
## Enunciado
Elegir o inventar un problema donde usar concurrencia sea beneficioso y/o necesario. Si están presentes las dos cosas mucho mejor.

- En general, cuanto más compleja la situación mejor, pero no es una regla inviolable sino un hilo conductor de la tarea.

- En general, cuanto más original la situación respecto de lo visto en la cursada mejor, pero no es una regla inviolable sino un hilo conductor de la tarea.

- La tarea es individual.

- Se entrega código, enunciado del problema y explicación de beneficios y/o necesidades de la concurrencia.
Puede haber un anexo con cosas, quizás un tanto al margen, que deseen incluir.

- Citar material, sitios, bibliografía, etc. utilizados, en caso de corresponder, tanto para elegir el problema, como para realizar el código y las explicaciones de beneficios y/o necesidades de la concurrencia.
Poner las citas explicitando la o las partes utilizadas y explicando brevemente para qué fueron usadas.

- La claridad, simpleza, coherencia, honestidad intelectual, ortografía, argumentaciones y producciones propias de la entrega, serán muy tenidas en cuenta.

- Se pueden usar herramientas y/o lenguajes no vistos durante la cursada, pero utilizar lo visto esta perfecto.

La fecha máxima de entrega es el Domingo 13/Dic 23:59 hs.

# Problema inventado basado en Star Wars
Estaba viendo de nuevo las películas de Star Wars y se me ocurrió que podía utilizarlo para aplicar la concurrencia, mi idea es la siguiente:
Tenemos a los Jedi, unos guerreros místicos que se encargan de mantener la paz de la galaxia. Estos guerreros tienen templos en los que entrenan a niños para enseñarles a combatir y a utilizar la fuerza (la fuerza siendo una energía que existe alrededor de todos los seres a lo largo de todo el universo, la cual les otorga varios poderes distintos que no vienen al caso).

## El programa
La idea es que haya un Gran Maestro Jedi que va aceptando, o rechazando, a los niños que llegan. Cuando se acepta a un candidato se lo pasa a llamar padawan, un aprendiz de Jedi, y se le avisa a un maestro para que lo entrene. Cada maestro puede entrenar solo a un padawan a la vez y puede entrenar a una cantidad aleatoria antes de ser reemplazado por otro maestro. Para decidir si se puede entrenar a un candidato, hay ciertas condiciones.

## Condiciones
### Ser sensibles a la fuerza
Esto significa, que sus midiclorianos (los midiclorianos son, a nivel celular, lo que les permite la conexión con la fuerza) sean mayores a 2500. Un humano común y corriente posee entre 2000 y 2500 midiclorianos. Cuantos más midiclorianos tenga el ser vivo, más poderoso con la fuerza es. Una persona con 5000 midiclorianos apenas es sensible a la fuerza. Para ser reclutado se tiene que tener al menos cuatro veces más midiclorianos que una peprsona normal, asi que digamos que para ser aceptado tiene que tener unos 8000 midiclorianos.
### No tener sentimientos negativos
No se puede entrenar a alguien que tiene sentimientos negativos porque hay un gran riesgo de que se pase al lado oscuro (osea, que se convierta en malo, básicamente). Sentimientos negativos sería que una persona sea propenso a la ira o tenga miedos de algo (como dijo el Gran Maestro Yoda, "El miedo es el camino hacia el Lado Oscuro. El miedo lleva a la ira, la ira lleva al odio, el odio, lleva al sufrimiento"). Esto lo podemos representar con un valor del 1 al 10, si se excede de 6, se considera al niño como "Propenso al lado oscuro".
### Excepción
Si un niño tiene una cantidad de midiclorianos mucho más alta que lo normal, se puede hacer una excepción. Esto sería si sus midiclorianos son mayores a 18000.
