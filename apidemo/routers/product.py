from django.shortcuts import get_object_or_404

from apidemo.schemas.product import ProductCreate, Product
from django.http import JsonResponse
import apidemo.models as models
from ninja_extra import api_controller ,route


@api_controller('/product', tags=['Product'], permissions=[])
class ProductController:
    @route.post("/", response=Product)
    def create_product(self,request, payload: ProductCreate):
        try:
            product = models.Product.objects.create(**payload.model_dump())
            return Product.model_validate(product)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    @route.get("/{product_id}", response=Product)
    def get_products(request, product_id: str):
        product = get_object_or_404(models.Product, pk=product_id)
        return Product.model_validate(product.first())

    @route.put("/{product_id}", response=Product)
    def update_product(request, product_id: str, payload: ProductCreate):
        product = get_object_or_404(models.Product, pk=product_id)
        for attr, value in payload.model_dump().items():
            setattr(product, attr, value)
        product.save()
        return Product.model_validate(product)

    @route.delete("/{product_id}")
    def delete_product(request, product_id: str):
        product = get_object_or_404(models.Product, pk=product_id)
        product.delete()
        return JsonResponse({"message": "Product deleted successfully."})






