#Juan David Troncoso 8967429 Programa de Descuento



def leerImprimir():
	dic={'076':[36000]}
	print('Productos disponible', dic)
	producto=[]
	cedula=[]
	unidad=[]
	valor=[]
	rol=[]

	list1=[]
	list2=[]

	i=0

	casos=int(input('Cuantos casos \n'))
	casos1=casos

	while i<casos:
		r=input(str('Rol \n'))
		rol.append(r)
		c=input(str('Cedula \n'))
		cedula.append(c)
		i+=1
	i=0
	while i<casos1:
		p=input(str('Producto \n'))
		producto.append(p)
		u=int(input('Unidad \n'))
		unidad.append(u)
		i+=1
	i=0	
		
	for key in dic.keys():
		list1.append(key)
	for val in dic:
		for elem in dic[val]:
			list2.append(int(elem))


	#print(rol, cedula, producto, unidad, list1, list2)		

	a=0

	while i<len(rol):
		while a<len(list1):
			if rol[i]=='Profesor':
				if producto[i]==list1[a]:
					resp=(unidad[i]*list2[a])*(0.2)

			elif rol[i]=='Estudiante':
				if producto[i]==list1[a]:		
					resp=(unidad[i]*list2[a])*(0.5)
			a+=1
		valor.append(resp)
		i+=1
		a=0
	i=0
	
	while i<len(rol):
		while a<len(list1):
			print('El', rol[i], 'con cedula', cedula[i], 'debe pagar', '$'+str(valor[i]), 'por el producto', list1[a])
			a+=1		
		i+=1	
		a=0
	i=0	


leerImprimir()