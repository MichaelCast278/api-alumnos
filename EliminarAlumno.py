import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']

    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Eliminar por clave compuesta
    response = table.delete_item(
        Key={
            'tenant_id': tenant_id,
            'alumno_id': alumno_id
        }
    )

    # Salida
    return {
        'statusCode': 200,
        'message': f'Alumno {alumno_id} eliminado correctamente',
        'response': response
    }
