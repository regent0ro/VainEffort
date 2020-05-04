from boto3.dynamodb.types import TypeSerializer

some_item = {
    "id" : 12345,
    "name" : "TanakaTaro",
    "Map" : {"map_id" : 54321},
    "List" : ["A", "B", "C"]
}

type_serializer = TypeSerializer()
result = type_serializer.serialize(some_item)
print(result)

# Result
# {'M': 
#     {
#         'id': {'N': '12345'},
#         'name': {'S': 'TanakaTaro'},
#         'Map': {
#             'M': {
#                 'map_id': {'N': '54321'}
#             }
#         },
#         'List': {
#             'L': [{'S': 'A'}, {'S': 'B'}, {'S': 'C'}]
#         }
#     }
# }