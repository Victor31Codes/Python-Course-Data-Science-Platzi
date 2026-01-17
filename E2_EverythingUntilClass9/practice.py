import numpy as np

months = np.array([
    'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
])

product_A = np.array([150, 200, 250, 300, 220, 210, 180, 190, 230, 240, 280, 300])
product_B = np.array([180, 210, 230, 250, 270, 260, 240, 250, 270, 290, 310, 330])
product_C = np.array([200, 220, 240, 260, 280, 300, 320, 340, 360, 380, 400, 420])

"""
El objetivo de este ejercicio es trabajar con arrays de NumPy para analizar y manipular
datos de ventas de tres productos a lo largo de un año. A través de diversas operaciones,
explorarás cómo usar NumPy para obtener estadísticas, realizar manipulaciones avanzadas y
aplicar técnicas de indexación para extraer información clave.
"""

print("Suma de ventas de Product A:", np.sum(product_A))
print("Suma de ventas de Product B:", np.sum(product_B))
print("Suma de ventas de Product C:", np.sum(product_C))

print ("El valor medio de ventas del producto A es:", np.mean(product_A))
print ("El valor medio de ventas del producto B es:", np.mean(product_B))
print ("El valor medio de ventas del producto C es:", np.mean(product_C))

print("Total de ventas de los tres productos por mes:")
total_sales = product_A + product_B + product_C
print(total_sales)
print("Enero: ", total_sales[0])
print("Febrero: ", total_sales[1])
print("Marzo: ", total_sales[2])
print("Abril: ", total_sales[3])
print("Mayo: ", total_sales[4])
print("Junio: ", total_sales[5])
print("Julio: ", total_sales[6])
print("Agosto: ", total_sales[7])
print("Septiembre: ", total_sales[8])
print("Octubre: ", total_sales[9])
print("Noviembre: ", total_sales[10])
print("Diciembre: ", total_sales[11])

max_sales_A = np.max(product_A)
max_sales_B = np.max(product_B)
max_sales_C = np.max(product_C)
print("Mes con mayores ventas de Product A:", months[np.argmax(product_A)], "con", max_sales_A, "ventas")
print("Mes con mayores ventas de Product B:", months[np.argmax(product_B)], "con", max_sales_B, "ventas")
print("Mes con mayores ventas de Product C:", months[np.argmax(product_C)], "con", max_sales_C, "ventas")

min_sales_A = np.min(product_A)
min_sales_B = np.min(product_B)
min_sales_C = np.min(product_C)
print("Mes con menores ventas de Product A:", months[np.argmin(product_A)], "con", min_sales_A, "ventas")
print("Mes con menores ventas de Product B:", months[np.argmin(product_B)], "con", min_sales_B, "ventas")
print("Mes con menores ventas de Product C:", months[np.argmin(product_C)], "con", min_sales_C, "ventas")

array_concatenated_ventas = np.concatenate((product_A, product_B, product_C))
print("Array concatenado de ventas de los tres productos:", array_concatenated_ventas)
reshaped_array = array_concatenated_ventas.reshape(3, 4, 3)
print("Array reshaped a 3D: \n", reshaped_array)

transposed_array = np.transpose(reshaped_array)
print("Array transpuesto: \n", transposed_array)

inverted_array = array_concatenated_ventas[::-1]
print("Array invertido de ventas concatenadas:", inverted_array)

inverted_product_A = product_A[::-1]
inverted_product_B = product_B[::-1] 
inverted_product_C = product_C[::-1]
print("Array invertido de ventas del producto A:", inverted_product_A)
print("Array invertido de ventas del producto B:", inverted_product_B)
print("Array invertido de ventas del producto C:", inverted_product_C)

flattened_array = reshaped_array.flatten()
print("Array aplanado de ventas concatenadas:", flattened_array)

unique_sales, counts = np.unique(array_concatenated_ventas, return_counts=True)
print("Valores únicos de ventas:", unique_sales)
print("Frecuencia de cada valor único de ventas:", counts)

sales_first_tree_months_product_A = product_A[:3] 
print("Ventas del primer trimestre del producto A: ", sales_first_tree_months_product_A)
sales_first_tree_months_product_B = product_B[:3] 
print("Ventas del primer trimestre del producto B: ", sales_first_tree_months_product_B)
sales_first_tree_months_product_C = product_C[:3] 
print("Ventas del primer trimestre del producto C: ", sales_first_tree_months_product_C)

boolean_flag = total_sales > 800
high_sales_months = months[boolean_flag]
print("Meses con ventas totales superiores a 800 unidades:", high_sales_months)