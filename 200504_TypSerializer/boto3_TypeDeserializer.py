from boto3.dynamodb.types import TypeDeserializer
import pprint,json

type_deserializer = TypeDeserializer()
pp = pprint.PrettyPrinter()

some_item_json = '{"id": {"N": "12345"}, "name": {"S": "TanakaTaro"}, "Map": {"M": {"map_id": {"N": "54321"}}}, "List": {"L": [{"S": "A"}, {"S": "B"}, {"S": "C"}]}}'

# String to Json
some_item = json.loads(some_item_json)

result = {}
for key in some_item:
    result[key] = type_deserializer.deserialize(some_item[key])

pp.pprint(result)

# Result
# {
#   'List': ['A', 'B', 'C'],
#   'Map': {'map_id': Decimal('54321')},
#   'id': Decimal('12345'),
#   'name': 'TanakaTaro'}