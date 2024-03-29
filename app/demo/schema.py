import graphene

import core.schema


class Query(core.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
