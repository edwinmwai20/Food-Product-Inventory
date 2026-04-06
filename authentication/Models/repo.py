class InventoryRepo:
    def __init__(self):
        self.store = {} 

    def add(self, product):
        new_id = len(self.store) + 1
        product.id = new_id
        self.store[new_id] = product
        return product

    def get_all(self):
        # Uses .is_deleted to match the Product class
        return [p.to_dict() for p in self.store.values() if not p.is_deleted]

    def get_by_id(self, p_id):
        try:
            product = self.store.get(int(p_id))
            return product if product and not product.is_deleted else None
        except ValueError:
            return None

    def delete(self, p_id):
        product = self.get_by_id(p_id)
        if product:
            product.is_deleted = True
            return True
        return False