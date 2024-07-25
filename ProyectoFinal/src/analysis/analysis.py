import pandas as pd # Importamos la libreria pandas para manejar y analizar datos
import os # Importamos el modulo OS para interactuar con el sistema operativo.
from ..decorators.decorators import timeit, logit

@logit
@timeit
def load_data(data_path):
    """Cargar los datos desde un archivo CSV o excel , en nuestro caso el archivo "products.csv"""
    
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path) # Cargamos los datos del archivo CSV
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path) # Cargamos los datos del archivo excel
    else:
        raise ValueError("Unsupported file format") # Lanzamos un error si el formato del archivo NO es compatible
    print("Data loaded successfully") # Imprimimos un mensaje indicando que nos datos se cargaron correctamente
    return df # Devolvemos el DataFrame con los datos cargados

@logit
@timeit
def clean_data(df):
    """Limpiamos los datos"""
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float) #Limpiamos y convertimos la columna de precios a tipo float
    print("Data cleaned successfully")
    return df # Devolvermos el DataFrame con los datos formateados

@logit
@timeit
def analyze_data(df):
    """Realizamos un analisis basico de datos"""
    print("Basic Data Analysis:") # Imprimimos un encabezado para el análisis de datos.
    print(df.describe()) # Imprimimos un resumen estadistico de los datos.
    print ("\nProducts with highest prices: ") # Imprimimos un encabezado con los productos con los precios mas altos
    highestPrices=df.nlargest(5,"price")
    print(highestPrices) # Imprimimos los 5 productos con los precios mas altos.
    return highestPrices

@logit
@timeit
def review_analysis(df):
    """Realizamos un analisis la cantidad de reviews."""
    print("Review Analysis:") # Imprimimos un encabezado para el análisis de reviews.
    print(df['review_count'].describe()) # Imprimimos un resumen estadistico de las reviews.
    most_reviewed = df.nlargest(5, 'review_count')
    print("\nProducts with the most reviews:") # Imprimimos un encabezado con los productos con más reviews.
    print(most_reviewed) # Imprimimos los 5 productos con más reviews.
    return most_reviewed

@logit
@timeit
def extreme_prices(df):
    """Realizamos un analisis de los productos mas caros y de los productos mas baratos."""
    print("\nMost Expensive Products:") # Imprimimos un encabezado mostrar los productos mas caros.
    most_expensive = df.nlargest(5, 'price')
    print(most_expensive) # Imprimimos los 5 productos más caros.
    
    print("\nLeast Expensive Products:") # Imprimimos un encabezado mostrar los productos mas baratos.
    least_expensive = df.nsmallest(5, 'price')
    print(least_expensive) # Imprimimos los 5 productos más baratos.
    return most_expensive, least_expensive

@logit
@timeit
def save_clean_data(df,outputch_path):
    """Guardamos los datos limpios en un archivo CSV"""
    if outputch_path.endswith(".csv"):
        df.to_csv(outputch_path,index=False) # Guardamos los datos en el archivo CSV
    elif outputch_path.endswith(".xlsx"):
        df.to_excel(outputch_path,index=False) # Guardamos los datos en un archivo excel
    else:
        raise ValueError("Unsupported file format") # Lanzamos un error si el formato del archivo NO es compatible
    print(f"Clean data saved to{outputch_path}") # Imprimimos un mensaje indicando que nos datos se cargaron correctamente
    
if __name__ == "__main__": # Permitimos que el screap solo se ejecute en este archivo
    data_path = "data/raw/products_laptops.csv" # Definimos la ruta del archivo de datos SIN procesar.
    outputh_path = "data/processed/cleaned_products_laptops.csv" #Definimos la ruta del archivo de los datos procesados
    
    df = load_data(data_path) # Cargamos los datos de un archivo especifico
    df = clean_data(df) # Limpiamos los datos cargados
    
    # Análisis básicos
    analyze_data(df)
    review_analysis(df)
    extreme_prices(df)
 
    os.makedirs("data/processed", exist_ok=True) #Creamos el directorio para los datos procesados si no existe
    save_clean_data(df,outputh_path) # Guardamos los datos limpios en el archivo especifico
    