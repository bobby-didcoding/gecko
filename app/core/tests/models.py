from django.test import TestCase
from core.models import (
    Pool,
    Network,
    Dex,
    Token
)

class DexModelTestCase(TestCase):

    def setUp(self):

        self.network = Network.objects.create(
            external_id = "base",
            type="network"
        )

        self.obj = Dex.objects.create(
            external_id = "uniswap-v3-base",
            type="dex",
            network = self.network 
        )

    def test_dex_creation(self):
        obj = self.obj
        self.assertTrue(isinstance(obj, Dex))
        self.assertEqual(obj.__str__(), "uniswap-v3-base")
        self.assertEqual(obj.status, 1)


class NetworkModelTestCase(TestCase):

    def setUp(self):

        self.obj = Network.objects.create(
            external_id = "base",
            type="network"
        )

    def test_network_creation(self):
        obj = self.obj
        self.assertTrue(isinstance(obj, Network))
        self.assertEqual(obj.__str__(), "base")
        self.assertEqual(obj.status, 1)


class TokenModelTestCase(TestCase):

    def setUp(self):

        self.network = Network.objects.create(
            external_id = "base",
            type="network"
        )

        self.dex = Dex.objects.create(
            external_id = "uniswap-v3-base",
            type="dex",
            network = self.network 
        )

        self.obj = Token.objects.create(
            type="token",
            dex=self.dex,
            network=self.network,
            external_id="base_0x4ed4e862860bed51a9570b96d89af5e1b0efefed"
        )

    def test_token_creation(self):
        obj = self.obj
        self.assertTrue(isinstance(obj, Token))
        self.assertEqual(obj.__str__(), "base_0x4ed4e862860bed51a9570b96d89af5e1b0efefed")
        self.assertEqual(obj.status, 1)

class PoolModelTestCase(TestCase):

    def setUp(self):

        self.network = Network.objects.create(
            external_id = "base",
            type="network"
        )
        self.obj = Pool.objects.create(
            external_id="base_0xc9034c3e7f58003e6ae0c8438e7c8f4598d5acaa",
            type="pool",
            attributes={"name": "DEGEN / WETH 0.3%", "address": "0xc9034c3e7f58003e6ae0c8438e7c8f4598d5acaa", "fdv_usd": "854357408", "volume_usd": {"h1": "1020957.50044389", "h6": "5410347.38290187", "m5": "23944.4038803586", "h24": "33934027.7244474"}, "transactions": {"h1": {"buys": 534, "sells": 147, "buyers": 429, "sellers": 131}, "m5": {"buys": 24, "sells": 9, "buyers": 22, "sellers": 8}, "h24": {"buys": 11491, "sells": 5383, "buyers": 6646, "sellers": 2799}, "m15": {"buys": 120, "sells": 28, "buyers": 99, "sellers": 25}, "m30": {"buys": 261, "sells": 65, "buyers": 211, "sellers": 60}}, "market_cap_usd": "287902872.856545", "reserve_in_usd": "11374526.3591", "pool_created_at": "2024-01-07T19:30:45Z", "base_token_price_usd": "0.0231121473908398", "quote_token_price_usd": "3496.61", "price_change_percentage": {"h1": "-2.05", "h6": "-1.29", "m5": "0.78", "h24": "10"}, "base_token_price_quote_token": "0.00000661", "quote_token_price_base_token": "151292", "base_token_price_native_currency": "0.00000660971320317256", "quote_token_price_native_currency": "1.0"},
            relationships={"dex": {"data": {"id": "uniswap-v3-base", "type": "dex"}}, "network": {"data": {"id": "base", "type": "network"}}, "base_token": {"data": {"id": "base_0x4ed4e862860bed51a9570b96d89af5e1b0efefed", "type": "token"}}, "quote_token": {"data": {"id": "base_0x4200000000000000000000000000000000000006", "type": "token"}}}
        )

    def test_pool_creation(self):
        obj = self.obj
        self.assertTrue(isinstance(obj, Pool))
        self.assertEqual(obj.__str__(), "base_0xc9034c3e7f58003e6ae0c8438e7c8f4598d5acaa")
        self.assertEqual(obj.status, 1)

