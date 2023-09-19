from rest_framework import viewsets
from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]