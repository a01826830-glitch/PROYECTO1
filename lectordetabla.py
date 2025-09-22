import pandas as pd

from figuras import rectangulo
from figuras import triangulo
from figuras import circulo
df = pd.read_csv("figuras.csv")
print("El archivo ha sido leido")
for index, row in df.iterrows():
   print("---------------------------------------------------------------------------")
   print(f"Fila {index}: FIGURA={row['FIGURA']}, MEDIDA1={row['MEDIDA1']},MEDIDA2={row['MEDIDA2']}")
   if row['FIGURA'] == 'r':        
     a, p = rectangulo(row['MEDIDA1'],row['MEDIDA2'])
     print("El area del rectangulo es: ",a )
     print("El perimetro del rectangulo es: ",p ) 
   elif  row['FIGURA'] == 't':
     a, p = triangulo(row['MEDIDA1'],row['MEDIDA2'])
     print("El area del triangulo es: ",a )
     print("El perimetro del triangulo es: ",p )
   else :
     a, p = circulo(row['MEDIDA1'])     
     print("El area del circulo: ",a )
     print("El perimetro del circulo es: ",p )

     