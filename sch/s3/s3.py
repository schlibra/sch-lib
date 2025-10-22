from typing import Union

from sch.logger import Logger


class S3:
    client = None
    bucket = None
    logger: Logger
    def __init__(self, config):
        self.logger = Logger('S3')
        try:
            import boto3
            from boto3.resources.base import ServiceResource
        except (ModuleNotFoundError, ImportError):
            self.logger.error('sch-lib[s3] is required for S3 support')
            exit(1)
        self.logger.info('Initializing S3 client')
        self.client = boto3.resource(
            's3',
            endpoint_url=config.get('s3.endpoint'),
            aws_access_key_id=config.get('s3.access_key'),
            aws_secret_access_key=config.get('s3.secret_key')
        )

    def list_buckets(self):
        self.logger.info('Listing S3 buckets')
        return [bucket.name for bucket in self.client.buckets.all()]

    def set_bucket(self, bucket_name: str):
        self.logger.info(f'Setting S3 bucket to {bucket_name}')
        self.bucket = self.client.Bucket(bucket_name)

    def read_file(self, key: str, decode: bool = True):
        try:
            self.logger.info(f'Reading file {key} from S3')
            _object = self.bucket.Object(key)
            _data = _object.get()['Body'].read()
            if decode:
                _data = _data.decode('utf-8')
            return _data
        except Exception as e:
            self.logger.error(f'Error reading file {key}: {e}')
            return False

    def write_file(self, key: str, data: Union[str, bytes]):
        self.logger.info(f'Writing file {key} to S3')
        _object = self.bucket.Object(key)
        _object.put(Body=data)
        self.logger.info(f'File {key} written to S3')

    def delete_file(self, key: str):
        self.logger.info(f'Deleting file {key} from S3')
        _object = self.bucket.Object(key)
        _object.delete()

