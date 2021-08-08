Algoritmo velocidad_carro_distancia
	Escribir "digite la velocidad del carro 1(kh/h)"
	Leer velocidad_1
	Escribir "digite la velocidad del carro 2(kh/h)"
	Leer velocidad_2
	Escribir "digite la distancia entre los dos carros"
	Leer distancia
	tiempo_encontrado = distancia / (velocidad_1 - velocidad_2)
	tiempo_minutos= tiempo_encontrado * 60
	Escribir " lo alcanza en:", tiempo_minutos
FinAlgoritmo
