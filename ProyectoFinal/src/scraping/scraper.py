import requests # Importar el modulo requests para hacer las solicitudes HTTP
from bs4 import BeautifulSoup # Importamos BeautifulSoup para analizar los documentos HTML
import pandas as pd # Importamos pandas para manejar datos en los DataFrames

def fetch_page(url):
    """Obtenemos el contenido de una pagina."""
    response= requests.get(url) # Realizamos una solicitud GET a la URL proporcionada.
    if response.status_code == 200: # Comparamos el status code con el 200 que significa que fue una peticion exitosa
        return response.content # Devolvemos el contenido de la pagina si la solicitud fue exitosa
    else:
        raise Exception(f"Failed to fetch page: {url}") # Lanzamos una excepcion por la solicitud falla
    
def parse_product(product):
    """Analizamos los detalles de un producto"""
    img= product.find("img",class_="img-fluid")['src'].strip() # Encontramos y obtenemos la url de la imagen del producto
    title= product.find("a",class_="title").text.strip() # Econtramos y obtenemos el titulo del producto
    description= product.find("p",class_="description").text.strip() # Entramos y obtenemos la descripcion del producto
    price= product.find("h4",class_="price").text.strip() # Encontramos y obtenemos el precio del producto
    review= product.find("p",class_="review-count").text.strip().split()[0] # Encontramos y obtenemos los reviews del producto
    return{ # Retornamos un diccionario con el titulo, la descripcion y el precio del producto
        "title":title, 
        "description":description,
        "price":price,
        "review-count":review,
        "img_url":img,
    }
 
def get_total_pages(soup):
    """Obtiene el número total de páginas a partir de la paginación."""
    pagination = soup.find("ul", class_="pagination")
    if pagination:
        pages = pagination.find_all("li")
        last_page = pages[-2].text.strip()  # La penúltima página suele ser el número total de páginas
        return int(last_page)
    return 1

def scrape(url):
    """Función principal del scraping."""
    products_data = []  # Inicializamos una lista para almacenar los datos de los productos.
    page_num = 1
    
    while True:
        page_url = f"{url}?page={page_num}"
        page_content = fetch_page(page_url)  # Obtenemos el código base de la página.
        soup = BeautifulSoup(page_content, "html.parser")  # Analizamos el contenido de la página con BeautifulSoup.
        products = soup.find_all("div", class_="thumbnail")  # Encontramos todos los elementos div con la clase "thumbnail" que representa productos.
        
        if not products:
            break  # Si no se encuentran productos, hemos llegado al final de la paginación.

        for product in products:
            product_info = parse_product(product)  # Analizamos cada producto encontrado.
            products_data.append(product_info)  # Agregamos los datos del producto a la lista.

        page_num += 1  # Pasamos a la siguiente página.
        
    return pd.DataFrame(products_data)  # Devolvemos un DataFrame con los datos de los productos.

# Definimos la URL base para el scraping.
base_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Llamamos a la función scrape para obtener los datos de los productos.
df = scrape(base_url)

# Imprimimos el DataFrame resultante.
print(df)

# Guardamos los datos en un archivo CSV sin incluir el índice.
df.to_csv('data/raw/products_laptops.csv', index=False)