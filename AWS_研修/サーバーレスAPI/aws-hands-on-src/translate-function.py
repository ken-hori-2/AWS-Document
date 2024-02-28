import json
import boto3

def lambda_handler(event, context):

    translate = boto3.client('translate') # インスタンスを呼び出す
    input_text = '順調ですか？'

    response = translate.translate_text(
        Text=input_text,
        SourceLanguageCode='ja', # 日本語から
        TargetLanguageCode='en' # 英語に翻訳
    )

    output_text = response['TranslatedText']

    return {
        'statusCode': 200,
        'body': json.dumps({
            'output_text': output_text
        })
    }
