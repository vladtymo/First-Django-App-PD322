from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'pv321group' # Must be replaced by your <storage_account_name>
    account_key = 'your_azure_storage_key' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'pv321group' # Must be replaced by your storage_account_name
    account_key = 'your_azure_storage_key' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None