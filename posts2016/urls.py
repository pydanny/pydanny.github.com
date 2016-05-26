from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserBillingView.as_view(),
        name='user_subscription_detail'
    ),
    url(
        regex=r'^start/$',
        view=views.UserSubscriptionCreateView.as_view(),
        name='user_subscription_create'
    ),
    url(
        regex=r'^cancel/$',
        view=views.CancelUserSubscriptionView.as_view(),
        name='user_subscription_cancel'
    ),
    url(
        regex=r'^reactivate/$',
        view=views.ReactivateUserSubscriptionView.as_view(),
        name='user_subscription_reactivate'
    ),
    url(
        regex=r'^change/payment/method/$',
        view=views.ChangePaymentMethodView.as_view(),
        name='change_payment_method'
    ),
    url(
        regex=r'^pawefiafjkvld/$',
        view=views.StripeWebHookReceiver.as_view(),
        name='stripe_webhook_receiver'
    )
]
