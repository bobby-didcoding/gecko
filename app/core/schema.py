import graphene
from graphene_django import DjangoObjectType
from .models import Pool


class PoolType(DjangoObjectType):

    todo = graphene.String(source='todo')
    class Meta:
        model = Pool
        fields = "__all__"


class Query(graphene.ObjectType):
    pools = graphene.List(PoolType)

    def resolve_pools(self, info):
        """
        The resolve_pools function is a resolver. 
        It’s responsible for retrieving the pools from the database and returning them to GraphQL.

        :param self: Refer to the current instance of a class
        :param info: Pass along the context of the query
        :return: All pool objects from the database
        """
        return Pool.objects.all()


schema = graphene.Schema(query=Query)