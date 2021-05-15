from cabin.models import *
from django.db.models import F, Func, Q, Count, Sum


def query_0(x):
    q = Driver.objects.filter(rating__gt=x)
    return q


def query_1(x):
    q = Payment.objects\
        .filter(ride__car__owner_id=x)\
        .aggregate(Sum('amount'))
    return {'payment_sum': q['amount__sum']}


def query_2(x):
    q = Ride.objects.filter(request__rider_id= x)
    return q


def query_3(t):
    q = Ride.objects\
        .annotate(duration = F('dropoff_time') - F('pickup_time'))\
        .filter(duration__gt= t).count()
    return q


def query_4(x, y, r):
    q = Driver.objects\
        .annotate(distance= Func((F('x') - x)**2 + (F('y') - y)**2, function='SQRT'))\
        .filter(distance__lte= r, active= True)
    return q


def query_5(n, c):
    q = Driver.objects\
        .annotate(num_rides= Count('car__ride'))\
        .filter(Q(car__color= c) | Q(car__car_type= 'A'), num_rides__gte= n)
    return q


def query_6(x, t):
    q = 'your query here'
    return q


def query_7():
    q = 'your query here'
    return q


def query_8():
    q = 'your query here'
    return q


def query_9(n, t):
    q = 'your query here'
    return q


def query_10():
    q = 'your query here'
    return q
