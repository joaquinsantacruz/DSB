![](data:image/png;base64...)

Desarrollo de software para blockchain 2026

Clase 03

![](data:image/png;base64...)

Rust

![](data:image/png;base64...)

¿Qué es Rust?

Es un lenguaje de programación multiparadigma compilado de

código abierto que se centra en la seguridad, la concurrencia y el

rendimiento. Diseñado para ayudar a los desarrolladores a escribir

código seguro y eﬁciente, ofrece características únicas que

permiten un manejo de memoria seguro en tiempo de compilación

sin la necesidad de un recolector de basura.

![](data:image/png;base64...)

¿Qué es Rust? Algunas características

● Sistema de tipos: tiene un sistema de tipos estático y fuertemente tipado, lo

que signiﬁca que el tipo de cada variable debe ser conocido en tiempo de

compilación y no puede cambiar durante la ejecución del programa.

● Seguridad de memoria: garantiza la seguridad de memoria mediante un

sistema de propiedad y préstamos, que ayuda a prevenir errores comunes

como el uso después de liberar, doble liberación y corrupción de memoria.

● Rendimiento:  compila el código directamente a código de máquina nativo y

optimizado, lo que generalmente proporciona un alto rendimiento.

![](data:image/png;base64...)

¿Qué es Rust? Algunas características cont..

● Calidad y ayuda en los mensajes de errores: Los mensajes de error que arroja el compilador de rust

son muy descriptivos, detallados y en muchas oportunidades explican cómo subsanar el error.

● Gestión de errores: utiliza el tipo Result para manejar errores de manera explícita y segura. Esto

puede resultar en un código más seguro y fácil de razonar.

● Macros (metaprogramación):  admite macros para la generación de código en tiempo de

compilación, lo que permite la creación de abstracciones personalizadas y la generación de código

eﬁciente.

● Empaquetado y administración de dependencias:  incluye cargo, una herramienta de construcción y

administración de paquetes que facilita la gestión de dependencias y la construcción de proyectos.

![](data:image/png;base64...)

Un poco de historia

● Se comenzó a trabajar en rust por el 2006 y la versión 1.0 fue liberada

en el 2015 por eso es un lenguaje muy reciente.

● Inicialmente fue pensado para programación de sistemas (sistemas

operativos, browsers, engine de videojuegos)

● Fue creado por un grupo de desarrolladores de mozilla

![](data:image/png;base64...)

¿Para que se usa?

Aplicaciones de línea de comando

Sistemas operativos

Browser engine

Backend/Api

Escribir aplicaciones de bajo nivel para mejorar performance

Webassembly (wasm)

Sistemas embebidos, microcontroladores, iot

Blockchain

![](data:image/png;base64...)

¿Qué es cargo?

Es el administrador de paquetes de Rust como npm o pip por ej. y

también nos facilita la creación de proyectos.

![](data:image/png;base64...)

¿Como usar cargo?

cargo new nombre\_del\_proyecto

Esto nos creará un proyecto con la siguiente estructura:

-un archivo llamado Cargo.toml

-un directorio src

otros comandos: build, run, check

crates: https://crates.io

![](data:image/png;base64...)

Vs Code extensiones recomendadas

rust-analyzer

better-toml

crates

error lens

![](data:image/png;base64...)

¿Cómo ..

-hacer comentarios

-deﬁnir una variable

-inmutabilidad, mutabilidad

-deﬁnir una constante

![](data:image/png;base64...)

Tipos de datos

Tipado estático: el chequeo de los tipos de datos se hace

en tiempo de compilación.

Se dividen en scalar types y compound types.

![](data:image/png;base64...)

Tipos de datos (scalar types)

● Integer: con y sin signo

● Floating-Point(32 y 64 bits)

● Boolean

● Character

![](data:image/png;base64...)

Tipos de datos (scalar types)

Integer:

ej: let numero: u32 = 42;

![](data:image/png;base64...)

Tipos de datos (scalar types)

Integer literals:

ej: let num = 32\_500;

![](data:image/png;base64...)

Tipos de datos (scalar types)

Operaciones:

fn main() {

let suma = 7 + 3;

let resta = 95.5 - 4.3;

let producto = 4 \* 30;

let division = 56.7 / 32.2;

let division2 = -5 / 3; // Resultado -1

let resto = 43 % 5;

}

![](data:image/png;base64...)

Tipos de datos (scalar types)

Boolean

fn main() {

let t = true;

let f: bool = false; // con explicito tipo

}

operaciones: &, &&, |, || , == , ^ , > , < , >= , <= , ! , !=

![](data:image/png;base64...)

Tipos de datos (scalar types)

Character:

fn main() {

let c = 'z';

let z: char = 'ℤ'; // con tipo explicito

let gatito = '😻';

}

El tipo de char de Rust tiene un tamaño de cuatro bytes y representa un valor Unicode, lo que signiﬁca que puede representar

mucho más que solo ASCII. Las letras acentuadas; los caracteres chinos, japoneses, coreanos, emojis, etc.

![](data:image/png;base64...)

Tipos de datos (compound types)

● String

● Tuple

● Array

![](data:image/png;base64...)

Tipos de datos (compound types): strings

-str: Es un tipo de cadena de caracteres inmutable y de longitud ﬁja.

-String: Es un tipo de cadena de caracteres que es mutable y de longitud variable.

![](data:image/png;base64...)

Tipos de datos (compound types): strings

ejemplo:

fn main() {

let str\_fijo:&str = "Soy un string inmutable";

let mut str\_mutable:String = "Soy mutable".to\_string();

str\_mutable += " concateno" ;

println!("{}", str\_mutable);

}

![](data:image/png;base64...)

Tipos de datos (compound types): tuple

Es una forma de agrupar distintos valores y pueden tener distintos tipos.

fn main() {

let mut tupla:(String, f32, u8) = ("hola".to\_string(), 3.0, 3);

tupla.0 = "cambio valor".to\_string();

println!("{}", tupla.0);

println!("{:?}", tupla);

let(hola, flotante, entero) = tupla;

println!("{}", hola);

}

![](data:image/png;base64...)

Tipos de datos (compound types): arrays

Son de tamaño ﬁjo y tienen el mismo tipo de dato. ej:

fn main() {

let arreglo = [1,2,3,5];

println!("el tercer el elemento es: {}", arreglo[2]);

let arreglo2 :[char ;2]= ['1', '2'];

println!("el ultimo elemento es: {}", arreglo2.last().unwrap());

}

![](data:image/png;base64...)

Uso de libs

En rust podremos hacer uso de libs o módulos para determinada acción y hacer reutilización de código,

observemos el siguiente fragmento de código:

use std::io::stdin;

fn main() {

println!("Ingrese su nombre: " );

let mut nombre = String::new();

stdin().read\_line(&mut nombre).expect("Error al leer el nombre.");

println!("Hola, {}!", nombre);

}

En la línea 1 importamos stdin de la lib standar de rust para poder leer desde teclado información.

stdin().read\_line no devuelve un Result, ya lo veremos más adelante

el expect nos sirve para indicar en caso de que el Result tenga error

que mensaje arrojar al disparar un Panic!

![](data:image/png;base64...)

Estructuras de control

![](data:image/png;base64...)

Estructuras de control: if, if-else

if condicion\_booleana {

//hace algo porque condicion\_booleana es true

}

if condicion\_booleana {

//hace algo porque la condicion\_booleana es true

}else{

// hace algo porque la condicion\_booleana es false

}

![](data:image/png;base64...)

Estructuras de control: if-else if

if condicion\_booleana {

//hace algo porque la condicion\_booleana es true

}else if otra\_condicion{

// hace algo porque otra\_condicion es true

}else{

//hace algo porque otra\_condicion y condicion\_boleana son

false

}

![](data:image/png;base64...)

Estructuras de control: if con declaración let

let data = if condicion\_booleana{ 20 } else { 0};

![](data:image/png;base64...)

Estructuras de control: match

la forma de match es la siguiente:

match algun\_valor {

patron\_que\_cumple\_algun\_valor => //hace algo porque lo cumple,

otro\_patron => //hace algo porque lo cumple,

}

patrón puede ser:literals,  destructured arrays , enums, structs,  tuples, variables, wildcards,

placeholders

![](data:image/png;base64...)

Estructuras de control: match(con variables)

let number = 10;

match number {

3 => println!("es tres o hace algo porque es 3"),

7 => println!("es siete o hace algo porque es 7"),

other => println!("hace algo porque porque no es 3 ni 7"),

}

![](data:image/png;base64...)

Estructuras de control: match(variables-placeholder)

let number = 10;

match number {

3 => println!("es tres o hace algo porque es 3"),

7 => println!("es siete o hace algo porque es 7"),

\_ => println!("hace algo porque porque no es 3 ni 7"),

}

![](data:image/png;base64...)

Estructuras de control: match

let number = 10;

match number {

3 => println!("es tres o hace algo porque es 3"),

7 => println!("es siete o hace algo porque es 7"),

\_ => (),

}

![](data:image/png;base64...)

Estructuras de control: while

let mut number = 0;

while number < 10{

println!("{number}");

number +=2;

};

![](data:image/png;base64...)

Estructuras de control: for

let arreglo = [1, 2, 3, 4, 5];

for elemento in arreglo {

println!("el valor es: {elemento}");

}

![](data:image/png;base64...)

Estructuras de control: for

let limite = 5;

for i in 1..limite+1 {

println!("el valor es: {i}");

}

for i in (1..limite+1).rev() {

println!("el valor es: {i}");

}

![](data:image/png;base64...)

Funciones

![](data:image/png;base64...)

Funciones

Como se observó estuvimos viendo una función: main. La deﬁnición de una función se realiza con la

palabra reservada “fn” a continuación el nombre de la misma (snake case) y luego entre los paréntesis los

argumentos. Entre las llaves el código propio del scope de la función.

fn mi\_nueva\_funcion(arg1: tipo, arg2: tipo, arg\_n:tipo){

//codigo propio del scope de la función

}

![](data:image/png;base64...)

Funciones

fn mi\_funcion( data:i32){

println!("{data}");

}

fn mi\_funcion( data:[i32; 7]){

for i in data{

println!("{i}");

}

}

![](data:image/png;base64...)

Funciones: retornado valores

fn mi\_funcion( data:i32) -> i32{

println!("{data}");

return data

}

fn mi\_funcion( data:i32) -> i32{

println!("{data}");

data

}

![](data:image/png;base64...)

Ownership y Borrowing

![](data:image/png;base64...)

Ownership y borrowing

Para el manejo de memoria de los programas hay 2 enfoques que utilizan mucho

de los lenguajes más usados:

-Tener un garbage collector que busca periódicamente memoria que no se

use para limpiarla.

-Y otro enfoque donde se debe asignar y liberar memoria explícitamente.

Rust usa un tercer enfoque, la memoria se administra a través de un concepto de

propiedad.

El concepto de ownership reﬁere a un conjunto de reglas de como Rust maneja la

memoria

![](data:image/png;base64...)

Ownership y borrowing

Estas reglas son las siguientes:

1. Cada valor en Rust tiene un dueño.

2. Solo puede haber un dueño a la vez.

3. Cuando el dueño queda fuera del alcance, el valor se eliminará.

![](data:image/png;base64...)

Ownership y borrowing

Stack vs Heap:

La memoria stack es rápida, es liberada cuando se alcanza el ﬁn del scope: aqui

irán los datos de tipo de tamaño conocido en tiempo de compilación como por ej

i32.

La memoria heap es ﬂexible, tiene elevado costo en asignar y recuperar datos. Es

liberada cuando no tiene dueños. Aquí irán los datos de tipo de tamaño

desconocido en tiempo de compilación como ser String.

![](data:image/png;base64...)

Ownership y borrowing

fn main() {

let s1= 10;

let s2 = s1;

println!("{}", s1);

}

![](data:image/png;base64...)

Ownership y borrowing

fn main() {

let s1= String::from("hello");

let s2= s1;

println!("{}", s1);

}

![](data:image/png;base64...)

Ownership y borrowing

![](data:image/png;base64...)

Ownership y borrowing

Que tipos implementan el trait Copy:

● Todos los enteros

● Booleanos

● Punto ﬂotante

● Char

● Tupla que solo tengan los tipos que implementan Copy

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let mut dato1= 10;

mi\_funcion (dato1);

println!("{}", dato1);

}

fn mi\_funcion (mut data: i32){

data+=1;

println!("muestro data en la funcion:  {}", data);

}

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let mut dato1= 10;

mi\_funcion (&mut dato1);

println!("{}", dato1);

}

fn mi\_funcion (data: &mut i32){

\*data+=1;

println!("muestro data en la funcion:  {}", data);

}

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let dato1= String::from(" Seminario de: ");

mi\_funcion(dato1);

println!("{}", dato1);

}

fn mi\_funcion(data: String){

println!("muestro data en la funcion: {}", data);

}

![](data:image/png;base64...)

Ownership y borrowing: funciones

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let dato1= String::from(" Seminario de: ");

mi\_funcion(&dato1);

println!("{}", dato1);

}

fn mi\_funcion(data: &String){

println!("muestro data en la funcion: {}", data);

}

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let dato1= String::from(" Seminario de: " );

let dato1 = mi\_funcion(dato1);

println!("{}", dato1);

}

fn mi\_funcion(data: String) -> String{

println!("muestro data en la funcion:  {}", data);

data

}

![](data:image/png;base64...)

Ownership y borrowing: funciones

fn main() {

let mut dato1= String::from(" Seminario de: ");

mi\_funcion(&mut dato1);

println!("{}", dato1);

}

fn mi\_funcion(data: &mut String){

data.push\_str(" Rust!");

println!("muestro data en la funcion: {}", data);

}

![](data:image/png;base64...)

Lifetime

![](data:image/png;base64...)

Lifetime

Cada referencia en Rust tiene una vida útil, que es el alcance para el cual esa referencia es

válida.

La mayoría de las veces el tiempo de vida de las referencias se inﬁeren al igual que la

mayoría de las veces se inﬁeren los tipos.

Lifetime es la manera que tiene el compilador de Rust de asegurar que un lugar de memoria

es válido para una referencia.

![](data:image/png;base64...)

Lifetime: ejemplos

fn main() {

let dato1: &i32;

{

let otro\_scope = 2;

dato1 = &otro\_scope;

}

println!("{}", dato1);

}

![](data:image/png;base64...)

Lifetime: ejemplos

fn main() {

let d1 = "str1";

let d2 = "str2";

let r = crear(d1, d2);

println!("{}", r.as\_str());

}

fn crear(data1: &str, data2: &str)-> &String{

let resultado:String = data1.to\_string().add(data2);

&resultado

}

![](data:image/png;base64...)

Lifetime: ejemplos

use std::{ops::Add};

fn main() {

let d1 = "str1";

let d2 = "str2";

let r = crear(d1, d2);

println! ("{}", r);

}

fn crear<'a>(data1: &'a str, data2: &'a str)-> &'a str{

let d1 = data1.to\_string ();

let resultado :&str = d1.add(data2).as\_str();

&resultado

}

![](data:image/png;base64...)

Lifetime: ejemplos

fn main() {

let string1 = String::from("Seminario de:");

let string2 = "Rust!!!";

let result = mas\_largo(string1.as\_str(), string2);

println!("El mas largo es:{}", result);

}

fn mas\_largo(x: &str, y: &str) -> &str {

if x.len() > y.len() {

x

} else {

y

}

}

![](data:image/png;base64...)

Lifetime: ejemplos

fn main() {

let string1 = String::from("Seminario de:");

let string2 = "Rust!!!";

let result = mas\_largo(string1.as\_str(), string2);

println!("El mas largo es:{}", result);

}

fn mas\_largo<'a>(x: &'a str, y: &'a str) -> &'a str {

if x.len() > y.len() {

x

} else {

y

}

}

![](data:image/png;base64...)

Lifetime: sintaxis

&i32 // una referencia

&'a i32 // una referencia con explicito lifetime

&'a mut i32 // una referencia mutable con explicito lifetime

![](data:image/png;base64...)

Structs

![](data:image/png;base64...)

Structs: ¿Qué son?

Es un tipo de dato personalizado que permite empaquetar y nombrar valores

relacionados que forman un conjunto de datos. Son similares, en la

programación orientada a objetos al conjunto de atributos que tiene una

clase.

![](data:image/png;base64...)

Structs: ¿Cómo se deﬁnen?

Se deﬁnen con la palabra clave struct de la siguiente manera:

struct NombreDelStruct{

nombre\_atributo\_1: tipo1,

nombre\_atributo\_2: tipo2,

nombre\_atributo\_n: tipo\_n

}

![](data:image/png;base64...)

Structs: ¿Cómo se deﬁnen?

Su deﬁnición no necesariamente tiene que ser dentro de la función main

struct Persona{

nombre: String,

apellido : String,

dni: i32

}

fn main() {

let persona1 = Persona{

nombre:"Lionel".to\_string (),

apellido: "Messi".to\_string (),

dni:1,

};

println!("nombre:  {} apellido: {} dni:{}", persona1 .nombre, persona1 .apellido , persona1 .dni);

}

![](data:image/png;base64...)

Structs: init shorthand

fn main() {

let persona1= nueva\_persona(

"Lionel".to\_string(),

"Messi".to\_string(),

1

);

println!("nombre: {} apellido:{} dni:{}", persona1.nombre, persona1.apellido, persona1.dni);

}

fn nueva\_persona(nombre: String, apellido: String, dni: i32) -> Persona{

Persona {

apellido,

dni,

nombre,

}

}

![](data:image/png;base64...)

Structs: modiﬁcaciones

fn main() {

let mut persona1 = nueva\_persona (

"Lionel".to\_string (),

"Messi".to\_string (),

1

);

println!("nombre:  {} apellido: {} dni:{}", persona1 .nombre, persona1 .apellido , persona1 .dni);

persona1.dni = 99;

println!("nombre:  {} apellido: {} dni:{}", persona1 .nombre, persona1 .apellido , persona1 .dni);

}

![](data:image/png;base64...)

Structs: creando instancias desde data de otra instancia

fn main() {

let persona1 = nueva\_persona (

"Lionel".to\_string (),

"Messi".to\_string (),

1

);

let persona2  = Persona{

nombre:"Thiago".to\_string (),

.. persona1

};

println!("nombre:  {} apellido: {} dni:{}", persona2 .nombre, persona2 .apellido , persona2 .dni);

}

![](data:image/png;base64...)

Structs: Tuple struct

struct Coordenada(f64, f64);

fn main() {

let la\_plata = Coordenada (-34.9213094 , -57.9555699 );

println!("latitud: {} longirud:{}", la\_plata.0, la\_plata.1);

}

![](data:image/png;base64...)

Structs: Implementando métodos

struct Coordenada(f64, f64);

impl Coordenada {

fn es\_la\_plata(self) -> bool{

let (latitud,longitud) = (-34.9213094, -57.9555699);

if self.0==latitud && self.1 == longitud{

return true;

}

false

}

}

fn main() {

let la\_plata = Coordenada(-34.9213094, -57.9555699);

println!("es la plata? {}", la\_plata.es\_la\_plata());

}

![](data:image/png;base64...)

Structs: Implementando métodos, otro ej

struct Rectangulo  {

ancho: u32,

altura: u32,

}

impl Rectangulo {

fn area(self) -> u32{

self.ancho \* self.altura

}

}

fn main() {

let rec1 = Rectangulo {ancho:3, altura:7};

println!("el area del rectangulo es: {}", rec1.area());

}

![](data:image/png;base64...)

Structs: Implementando métodos, otro ej

fn main() {

let rec1 = Rectangulo{ancho:3, altura:7};

println!("rectangulo es:{}", rec1);

}

![](data:image/png;base64...)

Structs: Implementando métodos, otro ej

fn main() {

let rec1 = Rectangulo {ancho:3, altura:7};

println!("el area del rectangulo es: {:?}", rec1);

}

![](data:image/png;base64...)

Structs: Implementando métodos, otro ej

#[derive(Debug)]

struct Rectangulo {

ancho: u32,

altura: u32,

}

fn main() {

let rec1 = Rectangulo{ancho:3, altura:7};

println!("rectangulo es:{:?}", rec1);

}

![](data:image/png;base64...)

Structs: funciones asociadas

Todas las funciones deﬁnidas dentro de un bloque impl se denominan funciones asociadas. Están

asociadas con el tipo que lleva el nombre de impl.

Podemos deﬁnir funciones asociadas que no tienen self como su primer parámetro (y por lo tanto no son

métodos) porque no necesitan una instancia del tipo para trabajar.

Las funciones asociadas que no son métodos a menudo se usan como constructores por ej. que devolverán

una nueva instancia de la estructura. Estos a menudo se suelen deﬁnir como new, pero new no es un

nombre especial y no está integrado en el lenguaje.

![](data:image/png;base64...)

Structs: funciones asociadas ejemplos

impl Rectangulo {

fn area(&self) -> u32{

self.ancho \* self.altura

}

fn new(ancho: u32, altura: u32) -> Rectangulo {

Rectangulo  { ancho, altura}

}

}

fn main() {

let rec1 = Rectangulo ::new(3,7);

println!("rectangulo es: {:?}", rec1);

println!("el area del rectangulo es: {}", rec1.area());

}

![](data:image/png;base64...)

Enums

![](data:image/png;base64...)

Enums: enumeration

Es un tipo de dato que permite deﬁnir distintas variaciones.

Para deﬁnirlo se utiliza la siguiente sintaxis:

enum NombreEnum{

VARIACION1,

VARIACION2,

VARIACION3,

…

}

![](data:image/png;base64...)

Enums: ejemplos

enum Rol{

PADRE,

HIJO,

}

struct Persona{

nombre: String,

apellido: String,

dni: i32,

rol:Rol,

}

fn main() {

let per1 = Persona{nombre:"Lionel".to\_string(), apellido:"Messi".to\_string(), dni:1, rol: Rol::PADRE,};

println!("el rol de:{} es:{:?}", per1.nombre, per1.rol);

}

![](data:image/png;base64...)

Enums: ejemplos => con valores

enum Rol{

PADRE(i32),

HIJO(i32),

}

fn main() {

let per1 = Persona{

nombre:"Lionel".to\_string(),

apellido:"Messi".to\_string(),

dni:1,

rol: Rol::PADRE(5),

};

match per1.rol{

Rol::PADRE(valor) => println!("{}", valor),

\_ => (),

};

}

![](data:image/png;base64...)

Enums: ejemplos => con Struct

struct StructPadre{}

struct StructHijo{}

impl StructPadre {

fn hace\_algo(self){

println!("soy un padre que hace algo");

}

}

impl StructHijo {

fn hace\_algo(self){

println!("soy un hijo que hace algo");

}

}

![](data:image/png;base64...)

Enums: ejemplos => con Struct cont..

enum Rol{

PADRE(StructPadre),

HIJO(StructHijo),

}

impl Rol{

fn hace\_algo(self){

match self {

Rol::PADRE(instancia) => instancia.hace\_algo(),

Rol::HIJO(instancia) => instancia.hace\_algo(),

}

}

}

![](data:image/png;base64...)

Enums: ejemplos => con Struct cont..

fn main() {

let per1 = Persona{

nombre:"Lionel".to\_string(),

apellido:"Messi".to\_string(),

dni:1,

rol: Rol::PADRE(StructPadre{}),

};

per1.rol.hace\_algo();

}

![](data:image/png;base64...)

Option

![](data:image/png;base64...)

Option: ¿Qué es?

Option es un enum que está disponible es la lib standard

Este enum tiene 2 posibles variantes que son Some() y None

Rust nos obliga a que en caso de que tengamos algún campo que no sepamos el

valor, es decir vacío o nulo tenemos que manejar explícitamente y de manera

obligatoria en código el caso. De esta forma se evitan los errores del tipo Null

Pointer Exception de otros lenguajes.

![](data:image/png;base64...)

Option: Ejemplo I

struct Persona{

nombre: String,

apellido: String,

dni: Option<i32>,

rol:Rol,

}

impl Persona {

fn new(nombre:String, apellido:String, rol:Rol, dni:Option<i32>) -> Persona{

Persona{

nombre,

apellido,

dni,

rol

}

}

}

![](data:image/png;base64...)

Option: Ejemplo I cont.

fn main() {

let nombre = "Lionel".to\_string();

let apellido = "Messi".to\_string();

let rol = Rol::PADRE(StructPadre {});

let dni = None;

let per1 = Persona::new(nombre, apellido, rol, dni);

println!("la persona:{} tiene el dni:{:?}", per1.apellido, per1.dni);

}

![](data:image/png;base64...)

Option: Ejemplo I con valor

fn main() {

let nombre = "Lionel".to\_string();

let apellido = "Messi".to\_string();

let rol = Rol::PADRE(StructPadre {});

let dni = Some(1);

let per1 = Persona::new(nombre, apellido, rol, dni);

match per1.dni {

Some(valor) => println!("el dni de: {} es: {}", per1.apellido, valor),

None => println!("{} no tiene nro de dni registrado", per1.apellido)

}

}

![](data:image/png;base64...)

Option: Ejemplo II con otro struct

struct DNI{

tipo: char,

nro: u32,

}

struct Persona{

nombre: String,

apellido: String,

dni: Option<DNI>,

rol:Rol,

}

impl Persona {

fn new(nombre:String, apellido:String, rol:Rol, dni:Option<DNI>) -> Persona{

Persona{nombre, apellido, dni, rol}

}

}

![](data:image/png;base64...)

Option: Ejemplo II con otro struct cont.

fn main() {

let nombre = "Lionel".to\_string();

let apellido = "Messi".to\_string();

let rol = Rol::PADRE(StructPadre {});

let dni = Some(DNI{tipo:'A', nro:1});

let per1 = Persona::new(nombre, apellido, rol, dni);

match per1.dni {

Some(valor) => println!("el dni de: {} es: {}", per1.apellido, valor.nro),

None => println!("{} no tiene nro de dni registrado", per1.apellido)

}

}

![](data:image/png;base64...)

Option: Ejemplo II con otro struct cont.

fn main() {

let nombre = "Lionel".to\_string();

let apellido = "Messi".to\_string();

let rol = Rol::PADRE(StructPadre {});

let dni = Some(DNI{tipo:'A', nro:1});

let per1 = Persona::new(nombre, apellido, rol, dni);

if per1.dni.is\_none(){

println!("{} no tiene nro de dni registrado", per1.apellido);

}else{

println!("el dni de: {} es: {:?}", per1.apellido, per1.dni.unwrap());

}

}

![](data:image/png;base64...)

Option: if let

fn main() {

let nombre = "Lionel".to\_string();

let apellido = "Messi".to\_string();

let rol = Rol::PADRE(StructPadre {});

let dni = Some(DNI{tipo:'A', nro:1});

let per1 = Persona::new(nombre, apellido, rol, dni);

if let Some(data) = per1.dni {

println!("el dni de: {} es: {}", per1.apellido, data.nro);

}else{

println!("{} no tiene nro de dni registrado", per1.apellido);

}

}

![](data:image/png;base64...)

Collections: ¿Qué son?

Son estructuras de datos que permiten almacenar y organizar datos de una

manera ﬂexible y dinámica.

![](data:image/png;base64...)

Secuences: Vec

![](data:image/png;base64...)

Vec: creación y agregando elementos

fn main() {

//creacion

let mut vector = Vec::new();

//agregando elementos

for i in 1..7{

vector.push(i);

}

//recorriendolo

for j in vector{

println!("{j}");

}

}

![](data:image/png;base64...)

Vec: accediendo a elementos

fn main() {

let mut vector = Vec::new();

for i in 10..18{

vector.push(i);

}

// para acceder al primer elemento

let primero = vector.first();

if let Some(elemento) = primero {

println!("El primer elemento es: {}", elemento);

}

println!("Tambien puedo acceder desde el indice: {}", vector[0]);

}

![](data:image/png;base64...)

Vec: accediendo a elementos II

fn main() {

let mut vector = Vec::new();

for i in 10..18{

vector.push(i);

}

//para acceder al ultimo elemento

let ultimo = vector.last();

if let Some(elemento) = ultimo {

println!("El ultimo elemento es: {}", elemento);

}

println!("Tambien puedo acceder desde el indice: {}", vector[vector.len()-1]);

}

![](data:image/png;base64...)

Vec: agregando elementos II

fn main() {

let mut vector = Vec::new();

for i in 10..18{

vector.push(i);

}

//otra forma de agregar elementos

let arreglo = [1,2,3];

vector.extend(arreglo);

println!("el ultimo elemento es:{}", vector[vector.len()-1]);

}

![](data:image/png;base64...)

Vec: modiﬁcando elementos

fn main() {

let mut vector = Vec::new();

for i in 10..18{

vector.push(i);

}

println!("{:?}", vector);

//modificando elementos

for i in 1..vector.len(){

vector[i]+=4;

}

println!("{:?}", vector);

}

![](data:image/png;base64...)

Vec: eliminando elementos

fn main() {

let mut vector = Vec::new();

for i in 1..7{

vector.push(i);

}

println!("{:?}", vector);

//eliminado un elemento de determinado indice

vector.remove(1);

println!("{:?}", vector);

}

![](data:image/png;base64...)

Vec: otras maneras de instanciarlos

fn main() {

// otras formas de definirlos

let vector:Vec<i32> = vec![];

let otro\_vector = vec![1, 2, 3];

let otro\_mas\_vector = vec![0;5];

println!("{:?}", vector);

println!("{:?}", otro\_vector);

println!("{:?}", otro\_mas\_vector);

}

//más data: https://doc.rust-lang.org/std/vec/struct.Vec.html

![](data:image/png;base64...)

Maps: HashMap

![](data:image/png;base64...)

HashMap: creación y agregado de elementos

fn main(){

use std::collections::HashMap;

let mut balances = HashMap::new();

balances.insert(1, 10.0);

balances.insert(2, 0.0);

balances.insert(3, 150\_000.0);

balances.insert(4, 2\_000.0);

for (id, balance) in balances {

println!("{id} tiene $ {balance}");

}

}

![](data:image/png;base64...)

HashMap: obtener y modiﬁcar un elemento

fn main(){

let mut balances:HashMap<i32, f64> = HashMap::new();

balances.insert(1, 10.0);

balances.insert(2, 0.0);

let id = 2;

let balance:Option<&mut f64> = balances.get\_mut(&id);

match balance {

Some(balance) => \*balance = \*balance + 12.0,

\_ => ()

}

if let Some(balance)= balances.get(&id){

println!("{balance}");

}

}

![](data:image/png;base64...)

HashMap: otra forma de construir

fn main(){

let balances = HashMap::from([

(1, 10.0),

(2, 0.0),

]);

// obtener solo las claves

for id in balances .keys(){

println!("{id}");

}

//obtener solo los valores

for val in balances.values(){

println!("{val}");

}

}

![](data:image/png;base64...)

HashMap: otros métodos importantes

balances.remove(&3);// elimina la clave-valor y retona un Option con el valor

balances.values\_mut();// retorna los valores para poder modificarlos

balances.get\_key\_value(&1);// retorna un Option con el par clave-valor

balances.contains\_key(&5);// retorna un bool

balances.entry(5).or\_insert(0.0);// inserta la clave-valor solo si no existe

balances.len();

balances.is\_empty();

balances.clear();

//más data: https://doc.rust-lang.org/std/collections/hash\_map/struct.HashMap.html

![](data:image/png;base64...)

Generics

![](data:image/png;base64...)

Generics: ¿Para qué sirven?

El tipo generic se utiliza para generalizar

implementaciones, permite mayor ﬂexibilidad en el código

![](data:image/png;base64...)

Generics: ejemplo I

#[derive(Debug)]

struct Punto{

x:i32,

y:i32,

}

fn main(){

let p1 = Punto{x:1,y:2};

println! ("{:?}", p1);

}

![](data:image/png;base64...)

Generics: ejemplo I

#[derive(Debug)]

struct Punto{

x:i32,

y:i32,

}

fn main(){

let p1 = Punto{x:1,y:2};

let p2 = Punto{x:10.5,y:2};

println! ("{:?} {:?}", p1, p2);

}

![](data:image/png;base64...)

Generics: ejemplo I

struct Punto<T>{

x:T,

y:T,

}

fn main(){

let p1 = Punto{x:1,y:2};

let p2 = Punto{x:10.5,y:2.0};

}

![](data:image/png;base64...)

Generics: ejemplo I

struct Punto<T>{

x:T,

y:T,

}

fn main(){

let p1 = Punto{x:1,y:2};

let p2 = Punto{x:10.5,y:2};

}

![](data:image/png;base64...)

Generics: ejemplo I

struct Punto<T, V>{

x:T,

y:V,

}

fn main(){

let p1 = Punto{x:1,y:2};

let p2 = Punto{x:10.5,y:2};

}

![](data:image/png;base64...)

Generics: ejemplo I

#[derive(Debug)]

struct Punto<T>{

x:T,

y:T,

}

fn main(){

let p1 = Punto{x:1,y:2};

let p2 = Punto{x:10,y:2};

println!("{:?}", p1);

println!("{:?}", p2);

}

![](data:image/png;base64...)

Generics: ejemplo de caja

struct Caja {

dato:i32,

estado:bool,

}

impl Caja {

fn new(dato:i32) -> Caja{

Caja { dato, estado:false}

}

fn abrir(&mut self)->i32{

self.estado = true;

self.dato

}

fn cerrar(&mut self){

self.estado = false;

}

}

![](data:image/png;base64...)

Generics: otro ejemplo

fn main(){

let mut caja = Caja::new(9);

caja.abrir();

caja.cerrar();

}

![](data:image/png;base64...)

Generics: otro ejemplo

fn main(){

let mut listado\_de\_compras  = Vec::new();

listado\_de\_compras .push((1, "Jabon de manos" ));

listado\_de\_compras .push((2, "Detergente" ));

let mut caja = Caja::new(listado\_de\_compras );

caja.abrir();

caja.cerrar();

}

![](data:image/png;base64...)

Generics: otro ejemplo

struct Caja <T>{

dato:T,

estado:bool,

}

impl<T> Caja<T> {

fn new(dato:T) -> Caja<T>{

Caja { dato, estado:false}

}

fn abrir(&mut self)->&T{

self.estado = true;

&self.dato

}

fn cerrar(&mut self){

self.estado = false;

}

}

![](data:image/png;base64...)

Traits

![](data:image/png;base64...)

Trait ¿Qué es?

● Es una funcionalidad particular que tiene un tipo y puede compartir

con otros tipos.

● Podemos usar traits para deﬁnir comportamiento de manera abstracta.

● Se pueden usar traits como límites en tipos de datos genéricos para

determinada funcionalidad que el tipo genérico debe cumplir.

● Son similares a las interfaces llamadas en otros lenguajes pero con

algunas diferencias.

![](data:image/png;base64...)

Trait: ejemplo I

pub trait MulI32 {

fn mul(&self, other:i32) -> f64;// abstracto

fn hace\_algo\_concreto(&self){// por defecto

println!("hace\_algo\_concreto");

}

}

![](data:image/png;base64...)

Trait : ejemplo I

impl MulI32 for f64{

fn mul(&self, other:i32) -> f64{

self \* other as f64

}

}

fn main(){

let v1 = 2.8;

let v2 = 4;

let r = v1.mul(v2);

println!("{}", r);

}

![](data:image/png;base64...)

Trait : ejemplo II

struct Perro{}

struct Gato{}

fn main(){

let gato = Gato{};

let perro = Perro{};

println!("{} {}", gato.hablar(), perro.hablar());

}

![](data:image/png;base64...)

Trait : ejemplo II

pub trait Animal{

fn hablar(&self) -> String;

}

impl Animal for Perro{

fn hablar(&self) -> String{

"Guau!".to\_string()

}

}

impl Animal for Gato{

fn hablar(&self) -> String{

"Miau!".to\_string()

}

}

![](data:image/png;base64...)

Trait : limitando un generic

pub fn imprimir\_hablar<T: Animal>(animal: &T) {

println!("Hablo! {}", animal.hablar());

}

fn main(){

let gato = Gato{};

let perro = Perro{};

imprimir\_hablar(&gato);

imprimir\_hablar(&perro);

}

![](data:image/png;base64...)

Trait : como parámetro

pub fn imprimir\_hablar (animal1: &impl Animal, animal2: &impl Animal) {

println!("Hablando! {} {}", animal1.hablar(), animal2.hablar());

}

fn main(){

let gato = Gato{};

let perro = Perro{};

imprimir\_hablar (&gato, &perro);

}

![](data:image/png;base64...)

Trait : como parámetro

pub fn imprimir\_hablar(animal: &impl Animal) {

println!("Hablo! {}", animal.hablar());

}

fn main(){

let gato = Gato{};

let perro = Perro{};

imprimir\_hablar(&gato);

imprimir\_hablar(&perro);

}

![](data:image/png;base64...)

Trait : múltiples

pub fn imprimir\_hablar(animal: &(impl Animal + OtroTrait)) {

println!("Hablo! {}", animal.hablar());

}

fn main(){

let gato = Gato{};

imprimir\_hablar(&gato);

}

![](data:image/png;base64...)

Trait : múltiples con where

pub fn imprimir\_hablar<T>(animal: &T)

where

T: Animal + OtroTrait

{

println!("Hablo! {}", animal.hablar());

}

fn main(){

let gato = Gato{};

imprimir\_hablar(&gato);

}

![](data:image/png;base64...)

Manejo de errores

![](data:image/png;base64...)

Manejo de errores

Rust agrupa los errores en recuperables e irrecuperables.

Un error recuperable es por ejemplo un archivo no encontrado, donde tan solo se informará el error

pero la ejecución del programa continuará.

Los errores irrecuperables en cambio son siempre señales de bugs en nuestro código, como por

ejemplo acceder a una posición inválida de un arreglo.

En la mayoría de los lenguajes no hay distinción entre estos 2 tipos de errores y suelen manejarse

con excepciones.

Rust no tiene ni maneja excepciones, en su lugar tiene el tipo Result<T, E> para errores recuperables

y la macro panic! para errores irrecuperables.

![](data:image/png;base64...)

Manejo de errores: panic!

fn main() {

let v = vec![1, 2, 3];

v[v.len()];

}

![](data:image/png;base64...)

Manejo de errores: panic! export RUST\_BACKTRACE=1 cargo run

![](data:image/png;base64...)

Manejo de errores: call panic!

fn verify(data: Vec<Data>){

if data.is\_empty(){

panic!("No hay data para procesar y es obligatorio");

}

//hace mas cosas

}

![](data:image/png;base64...)

Manejo de errores: Result

enum Result<T, E> {

Ok(T),

Err(E),

}

![](data:image/png;base64...)

Manejo de errores: Result

fn main() {

use std::io::stdin;

let mut buf = String::new();

let result = stdin().read\_line(&mut buf);

match result {

Ok(i) => procesar\_entrada(i),

Err(e) => procesar\_error(e)

}

}

![](data:image/png;base64...)

Manejo de errores: Result

fn main() {

let a = "123".to\_string();

let result = a.parse::<i32>();

match result {

Ok(data) => println!("el parseo fue correcto: {}", data),

Err(e) => println!("String inválido para parsear a i32: {}", e)

}

}

![](data:image/png;base64...)

Alcance y visibilidad

Para deﬁnir a un elemento(fn, struct, enum, mod) como público se

utiliza la palabra clave pub

delante de su deﬁnición, y esto indica que puede accedido desde fuera de

donde fue declarado. En cambio si no se especiﬁca con pub el compilador de

rust hará que sea privado y solo puede accederse en donde fue deﬁnido.

![](data:image/png;base64...)

Alcance y visibilidad

//ejemplo.rs

mod crate\_helper\_module {

// esta función solo puede ser accedida en este rs

pub fn crate\_helper() {}

//esta funcion solo puede ser accedida desde el scope de crate\_helper\_module

fn implementation\_detail() {}

}

// es es una funcion publica que puede ser accedida desde cualquier lugar, incluso

externamente

pub fn public\_api() {}

![](data:image/png;base64...)

Alcance y visibilidad

//ejemplo.rs

// Igual a public\_api

pub mod submodule {

use crate::ejemplo::crate\_helper\_module;

pub fn my\_method() {

crate\_helper\_module::crate\_helper();

}

// solo puede accederse en el scope de submodule

fn my\_implementation() {}

#[cfg(test)]

mod test {

#[test]

fn test\_my\_implementation() {

// con super accedo jerarquicamente un nivel arriba de definiciones del módulo

super::my\_implementation();

}

}

}

![](data:image/png;base64...)

Tests

![](data:image/png;base64...)

Unit testing: en rust

#[test]

assert!(expresion);

assert\_eq!(v1, v2);

assert\_ne!(v1, v2);

![](data:image/png;base64...)

Unit testing: en rust

comandos:

cargo test

cargo test nombre\_del\_test

cargo test nombre\_con\_el\_que\_empieza

#[ignore]

#[should\_be\_panic(expected="mensaje del panic")]

![](data:image/png;base64...)

Unit testing: coverage

Es una métrica utilizada en el contexto de pruebas de software que indica el porcentaje de

código fuente que ha sido ejecutado durante la ejecución de las pruebas. Se utiliza para

evaluar la efectividad de las pruebas en términos de qué tan bien cubren el código y qué

áreas del código no están siendo probadas.

La cobertura de código tiene como objetivo identiﬁcar las áreas del código que no han sido

probadas y que podrían contener errores o comportamientos inesperados. Una alta

cobertura de código no garantiza la ausencia de errores, pero proporciona una mayor

conﬁanza en la calidad del software, ya que implica que se han realizado esfuerzos para

probar exhaustivamente el código.

![](data:image/png;base64...)

Unit testing: ventajas de coverage

★ Identiﬁcación de código no probado: La cobertura de código permite identiﬁcar las partes del código que no

han sido ejecutadas durante las pruebas, lo que indica áreas de riesgo potencial donde los errores podrían

estar presentes.

★ Guía para la creación de pruebas: La cobertura de código puede ayudar a guiar la creación de pruebas

adicionales al revelar las áreas que requieren una mayor cobertura. Esto asegura que las pruebas se

enfoquen en las partes críticas del código.

★ Medición de la calidad de las pruebas: La cobertura de código se utiliza como una métrica para evaluar la

calidad de las pruebas. Una alta cobertura indica que se han realizado esfuerzos para probar

exhaustivamente el código y puede indicar una mayor conﬁabilidad del software.

![](data:image/png;base64...)

Unit testing: coverage en rust

tarpaulin: https://crates.io/crates/cargo-tarpaulin

comandos:

cargo tarpaulin --target-dir src/coverage --skip-clean --exclude-ﬁles=target/debug/\*

cargo tarpaulin --target-dir src/coverage --skip-clean --exclude-ﬁles=target/debug/\*

--out html

![](data:image/png;base64...)