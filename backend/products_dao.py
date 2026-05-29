from sql_connection import get_sql_connection

def get_all_products(connection):
    """
    Retrieves all products from the grocery_store database, including their unit of measure details.

    Returns:
        list: A list of dictionaries, each containing product_id, name, uom_id, price_per_unit, and uom_name.
    """

    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name " 
            "from products inner join uom on products.uom_id=uom.uom_id")

    cursor.execute(query)

    response = []
    for(product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name
        })

    return response

def insert_new_product(connection, product):
    """
    Inserts a new product into the products table.

    Args:
        name (str): The name of the product.
        uom_id (int): The unit of measure ID for the product.
        price_per_unit (float): The price per unit of the product.

    Returns:
        int: The ID of the newly inserted product.
    """

    cursor = connection.cursor()
    query = ("INSERT INTO products "
            "(name, uom_id, price_per_unit)" 
            "VALUES (%s, %s, %s)")
    
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    """
    Deletes a product from the products table based on the provided product ID.

    Args:
        product_id (int): The ID of the product to be deleted.
    """
    cursor = connection.cursor()
    query = ("delete from products where product_id =" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.rowcount

if __name__=="__main__":
    connection = get_sql_connection()
    #print(insert_product(connection, "Milk", 1, 2.5))
    print(delete_product(connection, 2))