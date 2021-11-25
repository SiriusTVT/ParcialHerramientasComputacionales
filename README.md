# ParcialHerramientasComputacionales

# Problema

# Para recuperarse un poco del tiempo en cuarentena, las cafeterías de la universidad se encuentran dando descuentos a la comunidad estudiantil y dependiendo si es estudiante o profesor, tienen descuentos diferentes. Se desea saber entonces por cada compra cuanto debe pagar el usuario en caja. Para ello:


# -	Pida por teclado la siguiente información para el cliente: 
cedula y rol: profesor o estudiante.

# -	Registrar el producto a comprar: código producto, cantidad de unidades y precio del producto.(un solo producto, varias unidades, por ejemplo: 
producto 076: gaseosa, 3 unidades).

# -	Los descuentos están dados de la siguiente forma: 
los estudiantes tienen un 50% de descuento mientras que los profesores tienen un 20% de descuento.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Al final el procedimiento por cada cliente debe imprimir el valor a pagar por sus productos de la forma:

”El Rol con cedula Numero, debe pagar Valor por el producto Código”

Ejemplo: ”El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076”.

# Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cedula de cada cliente y el código del producto llevado en el mensaje.

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Att Juan David Troncoso

Este problema que consiste en aplicar un descuento que ofrece la universidad a partir  de los productos que venden. Los cuales se le ofrece un descuento distinto a los diferentes roles presentados en el problema.

Este modelo permite tener un orden de venta con los datos de los consumidores y con el descuento correcto aplicado para los roles de los estudiantes y profesores.

# -	Datos de Entrada:
# Este programa recibe como entrada los datos de:
-	Cantidad de Casos (Número de veces que se ejecutara el programa)
-	Rol (Profesor y Estudiante)
-	Cedula (Números de la cedula)
-	Producto (Producto solicitado del diccionario existente)
-	Unidad (La cantidad solicitada del producto)

# -	Datos de salida:
# Este programa recibe como salida los datos la impresión de:
-	Rol (Profesor y Estudiante)
-	Cedula (Números de la cedula)
-	Producto (Producto solicitado del diccionario existente)
-	Unidad (La cantidad solicitada del producto)
-	Valor (Valor del producto aplicando la multiplicación de la unidad y el descuento del rol)

# - Como calcular la salida del valor del producto final:
-	Se debe almacenar los datos en listas independiste y luego empezar  un ciclo para comparar los datos del diccionario con los datos de entrada y a partir de condicionales filtrar el rol y el producto existente del diccionario. Luego realizar una operación parado en la posición del precio del producto por la unidad y por el descuento del rol como a continuación.

# Ejemplo:
# Respuesta =(unidad[i]*list2[a])*(0.5)

-	Llegando al final, cuando salga del siclo imprimir los valores solicitados por cada caso dentro de un ciclo de ciclos:

# Print('El', rol[i], 'con cedula', cedula[i], 'debe pagar', '$'+str(valor[i]), 'por el producto', list1[a])


