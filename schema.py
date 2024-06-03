import graphene
from post_3.schema import Query as PostQuery, Mutation as PostMutation

class Query(PostQuery, graphene.ObjectType):
    pass

class Mutation(PostMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)