import stripe, os

stripe_keys = {
    'secret_key': os.getenv('STRIPE_SECRET_KEY'),
    'publishable_key': os.getenv('STRIPE_PUBLISHABLE_KEY')
}

stripe.api_key = stripe_kyes.get('secret_key')