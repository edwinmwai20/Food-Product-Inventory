class Product:
    def __init__(self, product_name, barcode, brand, ingredients, price, stock, id=None):
        self.id = id
        self.barcode = barcode
        self.product_name = product_name
        self.brand = brand
        self.ingredients = ingredients 
        self.price = price
        self.stock = stock
        self.is_deleted = False

    def to_dict(self):
        return {
            'id': self.id,
            'barcode': self.barcode,
            'product_name': self.product_name,
            'brand': self.brand,
            'ingredients': self.ingredients,
            'stock': self.stock,
            'price': self.price,
            'is_deleted': self.is_deleted
        }