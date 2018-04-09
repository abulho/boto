import boto3

def upload_s3(file_name, bucket_name, key):
    '''
    uploads a file into an existing amazon s3 bucket

    Parameters:
    ----------
    [str] file_name   : file name, including the path, to upload into the s3
    [str] bucket_name : the name of the s3 bucket to load the file into
    [str] key         : the name to be called when the file gets uploaded to s3 (can be same as file_name)

    Returns:
    -------
    This function does not return anything
    It uploads a given file to the stated AWS s3 bucket

    '''
    s3 = boto3.client('s3')
    s3.upload_file(file_name, bucket_name, key)

if __name__ == '__main__':
    file_name = input('file name:')
    bucket_name = input('bucket name:')
    key = input('key:')
    upload_s3(file_name, bucket_name, key)
