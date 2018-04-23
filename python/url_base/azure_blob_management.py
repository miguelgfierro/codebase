from azure.storage.blob import BlockBlobService


def _check_container(service, container_name):
    if not service.exists(container_name):
        service.create_container(container_name)


def _check_blob(service, container_name, blob_name):
    if not service.exists(container_name):
        raise ValueError("Container {} does not exist".format(container_name))
    if not service.exists(container_name, blob_name):
        raise ValueError("Blob {} does not exist".format(blob_name))


def upload_file_to_blob(account_name,
                        account_key,
                        container_name,
                        local_filepath,
                        remote_filepath):
    service = BlockBlobService(account_name=account_name,
                               account_key=account_key)
    _check_container(service, container_name)
    service.create_blob_from_path(container_name,
                                  remote_filepath,
                                  local_filepath)


def upload_folder_to_blob(account_name,
                          account_key,
                          container_name,
                          local_filepath,
                          remote_filepath):
    pass


def download_file_from_blob(account_name,
                            account_key,
                            container_name,
                            local_filepath,
                            remote_filepath):
    service = BlockBlobService(account_name=account_name,
                               account_key=account_key)
    _check_blob(service, container_name, remote_filepath)
    service.get_blob_to_path(
        container_name, remote_filepath, local_filepath)


def download_folder_from_blob(account_name,
                              account_key,
                              container_name,
                              local_filepath,
                              remote_filepath):
    pass


if __name__ == "__main__":
    import os
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('account_name', type=str)
    parser.add_argument('account_key', type=str)
    parser.add_argument('container_name', type=str)
    parser.add_argument('local_filepath', type=str)
    parser.add_argument('remote_filepath', type=str)
    parser.add_argument('--action', type=str,
                        help="Options: upload_file, upload_folder, download_file, download_folder")
    args = parser.parse_args()
    if args.action == 'upload_file':
        upload_file_to_blob(args.account_name,
                            args.account_key,
                            args.container_name,
                            args.local_filepath,
                            args.remote_filepath)
    elif args.action == 'download_file':
        download_file_from_blob(args.account_name,
                                args.account_key,
                                args.container_name,
                                args.local_filepath,
                                args.remote_filepath)
    else:
        raise ValueError("Incorrect action {}".format(args.action))
