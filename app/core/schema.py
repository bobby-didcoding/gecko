import graphene
from graphene_django import DjangoObjectType
from .models import Pool, Dex, Network, Token, TokenPair


class PoolType(DjangoObjectType):

    name = graphene.String(source='name')
    address = graphene.String(source='address')
    base_token_price_usd = graphene.String(source='base_token_price_usd')
    quote_token_price_usd = graphene.String(source='quote_token_price_usd')
    base_token_price_quote_token = graphene.String(source='base_token_price_quote_token')
    quote_token_price_base_token = graphene.String(source='quote_token_price_base_token')

    class Meta:
        model = Pool
        fields = "__all__"

class DexType(DjangoObjectType):

    class Meta:
        model = Dex
        fields = "__all__"

class NetworkType(DjangoObjectType):

    class Meta:
        model = Network
        fields = "__all__"

class TokenType(DjangoObjectType):

    name = graphene.String(source='name')
    address = graphene.String(source='address')
    symbol = graphene.String(source='symbol')

    class Meta:
        model = Token
        fields = "__all__"

class TokenPairType(DjangoObjectType):

    class Meta:
        model = TokenPair
        fields = "__all__"


class Query(graphene.ObjectType):
    pools = graphene.List(PoolType)
    dexes = graphene.List(DexType)
    networks = graphene.List(NetworkType)
    pairs = graphene.List(TokenPairType)
    tokens = graphene.List(TokenType)

    def resolve_pools(self, info):
        """
        The resolve_pools function is a resolver. 
        It’s responsible for retrieving the pools from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All pool objects from the database
        """
        return Pool.objects.all()
    
    def resolve_dexes(self, info):
        """
        The resolve_dexes function is a resolver. 
        It’s responsible for retrieving the dexes from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All dexes objects from the database
        """
        return Dex.objects.all()
    
    def resolve_networks(self, info):
        """
        The resolve_networks function is a resolver. 
        It’s responsible for retrieving the networks from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All networks objects from the database
        """
        return Network.objects.all()
    
    def resolve_base_tokens(self, info):
        """
        The resolve_base_tokens function is a resolver. 
        It’s responsible for retrieving the base_tokens from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All base_tokens objects from the database
        """
        return Token.objects.all()
    
    def resolve_quote_tokens(self, info):
        """
        The resolve_quote_tokens function is a resolver. 
        It’s responsible for retrieving the quote_tokens from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All quote_tokens objects from the database
        """
        return Token.objects.all()
    
    def resolve_pairs(self, info):
        """
        The resolve_pairs function is a resolver. 
        It’s responsible for retrieving the pairs from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All pairs objects from the database
        """
        return TokenPair.objects.all()


schema = graphene.Schema(query=Query)