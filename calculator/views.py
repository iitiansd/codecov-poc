from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CalculatorView(APIView):
    def post(self, request):
        a = request.data.get('a')
        b = request.data.get('b')
        operation = request.data.get('operation')

        if a is None or b is None or operation is None:
            return Response({'error': 'Missing parameters.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return Response({'error': 'Invalid number format.'}, status=status.HTTP_400_BAD_REQUEST)

        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return Response({'error': 'Division by zero.'}, status=status.HTTP_400_BAD_REQUEST)
            result = a / b
        else:
            return Response({'error': 'Invalid operation.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'result': result})
