from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ...products.exceptions import ProductNotFound
from ..services.products import ProductService
from ..serializers import ProductSerializer, ProductCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProductListView(APIView):
    permission_classes = [AllowAny]
    product_service = ProductService()
    
    def get(self, request):
        """
        Get a list of all products.
        """
        products = self.product_service.get_all_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductView(APIView):
    permission_classes = [IsAuthenticated]
    product_service = ProductService()
    
    def post(self, request):
        """
        Create a new product.
        """
        product_data = request.data
        serializer = ProductCreateUpdateSerializer(data=product_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        """
        Get details of a specific product.
        """
        try:
            product = self.product_service.get_product_by_id(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ProductNotFound as e:
            return Response({'message': e.message}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk):
        """
        Update details of a specific product.
        """
        try:
            product = self.product_service.get_product_by_id(id=pk)
            serializer = ProductCreateUpdateSerializer(product, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProductNotFound as e:
            return Response({'message': e.message}, status=status.HTTP_404_NOT_FOUND)
        except PermissionError as e:
            return Response({'message': "User is not permitted"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'message': f'Something went wrong {e}'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a specific product.
        """
        try:
            is_deleted = self.product_service.delete_product(action_user=request.user ,id=pk)
            if is_deleted:
                return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'message': 'Something went wrong while deleting'}, status=status.HTTP_404_NOT_FOUND)
        except ProductNotFound as e:
            return Response({'message': e.message}, status=status.HTTP_404_NOT_FOUND)
        except PermissionError as e:
            return Response({'message': "User is not permitted"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'message': f'Something went wrong: {e}'}, status=status.HTTP_400_BAD_REQUEST)
