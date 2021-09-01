Algoritmo sueldo_base
	Escribir "digite el sueldo base"
	Leer sb
	Escribir "Digite el precio de la primera venta"
	Leer v1
	Escribir "Digite el precio de la segunda venta"
	Leer v2
	Escribir "Digite el precio de la tercera venta"
	Leer v3
	
	tot_vta<-v1+v2+v3
	com = tot_vta*0.1
	tpag<- sb + com
	
	Escribir "su comision es:", com
	Escribir "su total de pago es:", tpag
FinAlgoritmo
