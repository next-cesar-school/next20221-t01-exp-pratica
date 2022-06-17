def there_are_images (list_images):
     return not (list_images == None or len(list_images) == 0)

def there_is_token (file):
    token = 'NExT_'
    return file[:len(token)] == token