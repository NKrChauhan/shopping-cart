class ProductNotFound(Exception):
    def __init__(self, product_id, *args: object):
        self.message = f"Product not found {product_id}"
        super().__init__(*args)