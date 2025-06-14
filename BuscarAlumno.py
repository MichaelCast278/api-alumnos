import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']

    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Búsqueda por llave compuesta
    response = table.get_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    # Verifica si existe
    if 'Item' in response:
        return {
            'statusCode': 200,
            'alumno': response['Item']
        }
    else:
        return {
            'statusCode': 404,
            'message': 'Alumno no encontrado'
        }
    