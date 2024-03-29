import json
from graphene_django.utils.testing import GraphQLTestCase
from core.models import Pool, Network

class PoolTestCase(GraphQLTestCase):

    GRAPHQL_URL = "/graphql/"

    def test_pool_query(self):
        response = self.query(
            '''
            query{
                pools{
                    externalId
                    name
                    address
                    baseTokenPriceUsd
                    quoteTokenPriceUsd
                    baseTokenPriceQuoteToken
                    quoteTokenPriceBaseToken
                    dex{
                    externalId
                    }
                    network{
                    externalId
                    }
                }
            }
            ''',
            operation_name=None
        )
        self.assertResponseNoErrors(response)


class PairsTestCase(GraphQLTestCase):

    GRAPHQL_URL = "/graphql/"

    def test_pairs_query(self):
        response = self.query(
            '''
            query{
                pairs{
                    baseToken{
                    externalId
                    }
                    quoteToken{
                    externalId
                    }
                }
            }
            ''',
            operation_name=None
        )
        self.assertResponseNoErrors(response)
