from .s3 import S3Client


def read():
    client = S3Client()
    print('Start ...')
    client.download(
        'cfex-dev-se-settlement', 
        'ml/haystack_wind_generation_prediction_15mins_feature_names.json'
        )
    
    print('Complete')

if __name__ == '__main__':
    read()