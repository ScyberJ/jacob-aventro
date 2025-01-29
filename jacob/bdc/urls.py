from django.urls import include, path
from .views import consult, exchange, hedge, index, transfer, travel

app_name = "bdc"

urlpatterns = [
    path("", index, name="home"),
    path('services/',
        include(
            [
                path("exchange", exchange, name="exchange"),
                path("transfer", transfer, name="transfer"),
                path("hedge", hedge, name="hedge"),
                path("travel", travel, name="travel"),
                path("consult", consult, name="consult"),
            ]
        )
    ),
]
