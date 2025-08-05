
from rest_framework.views import APIView
from rest_framework.response import Response


@api_view(['GET'])
def get_menu(request):
    menu_data = [
        {
            'name':'Margherita Pizza'
            'description':'Classic pizza with tomato sauce,mozzarella, and basil',
            'price':1000
        },
        {
            'name' : 'Caesar Salad',
            'description':'Romaine lettuce,croutons.parmesan, and Caesar dressing',
            'price':700
        }
        {
            'name':"Pasta";
             'description':'Pasta with pancetta,egg,parmesan, and black pepper',
             'price':500
        }
    ]

    return Response(menu_data)