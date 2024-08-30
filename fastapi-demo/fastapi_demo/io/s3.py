import string
import boto3
import logging
import random


logger = logging.getLogger(__name__)

class S3Client(object):
    def __init__(self) -> None:
        logger.info('创建了 S3Client')
        self.s3 = boto3.client('s3')


    def download(self, bucket: str, key: str) -> str:
        """
        Copy the cloud file to local

        :param bucket:
        :param key:
        :return: the local file's name, which is a random string
        """
        local_file_path = self.create_temp_file_name()

        logger.info(f"开始下载文件：s3://{bucket}/{key} -> {local_file_path}")
        self.s3.download_file(bucket, key, local_file_path)
        logger.info("下载完毕")

        return local_file_path


    def create_temp_file_name(self) -> str:
        return ''.join(random.choices(string.digits + string.ascii_letters, k=10))
