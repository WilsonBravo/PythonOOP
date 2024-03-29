# Python Object-Oriented Programming (OOP)

Aquí se encuentran una serie de proyectos para aprender Orientación a Objetos (OOP) en Python. Cada proyecto tiene una descripción básica y un paso a paso junto con los conceptos clave que abarcan.

## 1. **Calculadora Simple:**
   - **Descripción:** Crea una clase `Calculadora` que tenga métodos para realizar operaciones básicas como suma, resta, multiplicación y división. Utiliza objetos de esta clase para realizar cálculos simples.<br><br>

   - **Conceptos de OOP:** *Clases, métodos, atributos.*
        1. **Clases:** Las clases son plantillas para crear objetos que encapsulan datos y comportamientos relacionados. En este proyecto, la clase `Calculadora` representa una calculadora con métodos para realizar operaciones matemáticas.
        2. **Métodos:** Los métodos son funciones asociadas a una clase que pueden realizar operaciones específicas sobre los objetos de esa clase. En este caso, los métodos de la clase `Calculadora` realizan las operaciones de suma, resta, multiplicación y división.
        3. **Atributos:** Los atributos son variables asociadas a un objeto que representan su estado. En este proyecto, la calculadora puede tener atributos como el último resultado calculado.
        4. **Encapsulación:** La encapsulación es el proceso de ocultar la implementación interna de un objeto y solo exponer una interfaz pública para interactuar con él. En este proyecto, los métodos de la clase `Calculadora` encapsulan la lógica para realizar operaciones matemáticas.<br><br>

   - **Pasos a seguir:**
        1. Define una clase `Calculadora` con métodos para las operaciones básicas (suma, resta, multiplicación, división).
        2. Implementa métodos para realizar cada operación.
        3. Crea objetos de la clase `Calculadora` y realiza cálculos simples.

## 2. **Gestor de Contactos:**
   - **Descripción:** Desarrolla una clase `Contacto` que represente a una persona con atributos como nombre, apellido, número de teléfono, y dirección de correo electrónico. Crea una clase `Agenda` que permita agregar, eliminar, buscar y mostrar contactos.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación.*
        1. **Herencia:** La herencia es un mecanismo en el que una clase puede heredar atributos y métodos de otra clase. En este proyecto, podrías crear una clase base `Persona` y hacer que la clase `Contacto` herede de ella para reutilizar sus atributos como nombre y apellido.
        2. **Métodos de Clase:** Los métodos de clase son funciones que se definen en una clase y se relacionan con la clase en lugar de con instancias individuales de la clase. En este proyecto, podrías definir métodos de clase en la clase `Agenda` para buscar contactos por criterios específicos.
        3. **Polimorfismo:** El polimorfismo es la capacidad de objetos de diferentes clases de responder al mismo mensaje de diferentes maneras. En este proyecto, podrías implementar métodos para mostrar información de contactos que se comporten de manera diferente según el tipo de contacto.<br><br>

   - **Pasos a seguir:**
     1. Define una clase `Contacto` con atributos como nombre, apellido, número de teléfono y correo electrónico.
     2. Crea métodos para agregar, eliminar, buscar y mostrar contactos en la clase `Agenda`.
     3. Implementa la lógica para realizar estas operaciones utilizando objetos de las clases `Contacto` y `Agenda`.


## 3. **Lista de Tareas:**
   - **Descripción:** Crea una clase `Tarea` con atributos como descripción, fecha de vencimiento y estado (pendiente, en progreso, completada). Desarrolla una clase `ListaTareas` que permita agregar, eliminar y mostrar tareas, así como marcarlas como completadas.
   <br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación.*
        1. **Encapsulación:** En este proyecto, la encapsulación se utiliza para ocultar la implementación interna de las tareas y la lista de tareas, y solo exponer métodos para interactuar con ellas.
        2. **Métodos Especiales:** Los métodos especiales, como `__init__` para inicialización de objetos y `__str__` para representación de cadenas, se pueden utilizar para definir el comportamiento específico de las clases en Python. En este proyecto, podrías implementar `__str__` en la clase `Tarea` para mostrar información sobre la tarea.
        3. **Composición:** La composición es un principio de diseño en el que los objetos complejos se construyen a partir de objetos más simples. En este proyecto, la lista de tareas se puede componer de objetos de la clase `Tarea`.<br><br>

   - **Pasos a seguir:**
     1. Define una clase `Tarea` con atributos como descripción, fecha de vencimiento y estado.
     2. Crea una clase `ListaTareas` con métodos para agregar, eliminar, mostrar y marcar tareas como completadas.
     3. Implementa la lógica para gestionar las tareas utilizando objetos de las clases `Tarea` y `ListaTareas`.


## 4. **Juego de Cartas:**
   - **Descripción:** Implementa clases para representar un juego de cartas, incluyendo cartas individuales y una baraja. Desarrolla métodos para barajar las cartas, repartirlas a los jugadores y determinar el ganador.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación.*
        1. **Polimorfismo:** En este proyecto, el polimorfismo se puede utilizar para definir comportamientos específicos de diferentes tipos de cartas, como cartas de jugador y cartas de la baraja.
        2. **Herencia:** La herencia se puede utilizar para representar diferentes tipos de cartas, como cartas de corazón, diamante, pica y trébol, que heredan de una clase base `Carta`.
        3. **Métodos de Instancia vs. Métodos de Clase:** Los métodos de instancia operan en instancias individuales de una clase, mientras que los métodos de clase operan en la clase misma. En este proyecto, podrías implementar métodos de clase para barajar y repartir cartas.<br><br>

   - **Pasos a seguir:**
     1. Define clases para representar cartas individuales y una baraja.
     2. Implementa métodos para barajar las cartas, repartirlas a los jugadores y determinar el ganador.
     3. Desarrolla la lógica del juego utilizando objetos de las clases definidas.


## 5. **Sistema de Gestión de Biblioteca:**
   - **Descripción:** Crea clases para representar libros, usuarios y la biblioteca en sí. Implementa métodos para que los usuarios puedan tomar prestados libros, devolverlos y buscar libros disponibles.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación, herencia.*
        1. **Herencia:** La herencia se puede utilizar para representar diferentes tipos de usuarios, como estudiantes y profesores, que comparten atributos y comportamientos comunes de la clase base `Usuario`.
        2. **Métodos Estáticos:** Los métodos estáticos son funciones asociadas a una clase en lugar de a instancias de esa clase. En este proyecto, podrías definir un método estático en la clase `Libro` para buscar libros por categoría.
        3. **Métodos de Clase vs. Métodos de Instancia:** Los métodos de clase se definen con `@classmethod` y operan en la clase misma, mientras que los métodos de instancia operan en instancias individuales de la clase. En este proyecto, podrías usar métodos de clase para calcular estadísticas sobre los libros de la biblioteca.<br><br>

   - **Pasos a seguir:**
     1. Define clases para representar libros, usuarios y la biblioteca.
     2. Implementa métodos para tomar prestados libros, devolverlos y buscar libros disponibles.
     3. Utiliza la herencia para crear diferentes tipos de usuarios (por ejemplo, estudiantes y profesores) con comportamientos específicos.


## 6. **Simulador de Banco:**
   - **Descripción:** Desarrolla clases para representar cuentas bancarias, clientes y el banco en sí. Implementa métodos para realizar depósitos, retiros y transferencias entre cuentas.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación, herencia.*
        1. **Encapsulación:** La encapsulación se puede utilizar para ocultar la implementación interna de las cuentas bancarias y solo exponer métodos para realizar operaciones como depósitos, retiros y transferencias.
        2. **Polimorfismo:** En este proyecto, el polimorfismo se puede utilizar para definir diferentes tipos de cuentas bancarias con comportamientos específicos, como cuentas de ahorro y cuentas corrientes.
        3. **Métodos Especiales:** Los métodos especiales, como `__init__` para inicialización de objetos y `__str__` para representación de cadenas, se pueden utilizar para definir el comportamiento específico de las clases en Python. En este proyecto, podrías implementar `__str__` en la clase `CuentaBancaria` para mostrar información sobre la cuenta.<br><br>

   - **Pasos a seguir:**
     1. Define clases para representar cuentas bancarias, clientes y el banco.
     2. Implementa métodos para realizar depósitos, retiros y transferencias entre cuentas.
     3. Utiliza la herencia para manejar diferentes tipos de cuentas (por ejemplo, cuentas de ahorro y cuentas corrientes) con comportamientos específicos.

## 7. **Tienda en Línea:**
   - **Descripción:** Crea clases para representar productos, carritos de compra y usuarios. Implementa métodos para agregar productos al carrito, procesar compras y calcular el total.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación, herencia.*
        1. **Herencia:** La herencia se puede utilizar para representar diferentes tipos de productos, como libros y electrónicos, que comparten atributos y comportamientos comunes de la clase base `Producto`.
        2. **Polimorfismo:** En este proyecto, el polimorfismo se puede utilizar para definir métodos específicos de cada tipo de producto, como el cálculo del precio total teniendo en cuenta el descuento para algunos productos.
        3. **Composición:** La composición se puede utilizar para construir objetos complejos a partir de objetos más simples, como un carrito de compra que contiene objetos de la clase `Producto`.<br><br>

   - **Pasos a seguir:**
     1. Define clases para representar productos, carritos de compra y usuarios.
     2. Implementa métodos para agregar productos al carrito, procesar compras y calcular el total.
     3. Utiliza la herencia para manejar diferentes tipos de productos (por ejemplo, libros y electrónicos) con comportamientos específicos.


## 8. **Gestor de Proyectos:**
   - **Descripción:** Desarrolla clases para representar proyectos, tareas y empleados. Implementa métodos para asignar tareas a empleados, hacer un seguimiento del progreso del proyecto y generar informes.<br><br>

   - **Conceptos de OOP:** *Clases, atributos, métodos, encapsulación, composición.*
        1. **Encapsulación:** La encapsulación se puede utilizar para ocultar la implementación interna de los proyectos, tareas y empleados, y solo exponer métodos para interactuar con ellos.
        2. **Composición:** La composición se puede utilizar para relacionar objetos de diferentes clases, como asignar tareas a proyectos y empleados.
        3. **Métodos de Clase vs. Métodos de Instancia:** Los métodos de clase se definen con `@classmethod` y operan en la clase misma, mientras que los métodos de instancia operan en instancias individuales de la clase. En este proyecto, podrías utilizar métodos de clase para generar informes sobre el progreso del proyecto. <br><br>

   - **Pasos a seguir:**
     1. Define clases para representar proyectos, tareas y empleados.
     2. Implementa métodos para asignar tareas a empleados, hacer un seguimiento del progreso del proyecto y generar informes.
     3. Utiliza la composición para relacionar objetos de diferentes clases, como asignar tareas a proyectos y empleados.
