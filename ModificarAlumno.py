import boto3

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['tenant_id']
    alumno_id = event['alumno_id']
    alumno_datos = event['alumno_datos']

    # Conexión a DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')

    # Registro actualizado
    alumno_actualizado = {
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'alumno_datos': alumno_datos
    }

    # Reemplaza si existe
    response = table.put_item(Item=alumno_actualizado)

    # Respuesta
    return {
        'statusCode': 200,
        'message': 'Alumno modificado correctamente',
        'response': response
    }
