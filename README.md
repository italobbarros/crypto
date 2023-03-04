# Commands for use that API.


| cmd | cmd long | type |  description |
|:-:|:-:|:-:|:-:|
| -h | --help | None | print the options
| -k | --key | string | key used for encrypt your data
| -e | --encrypt_text | string | text to go use for encrypt
| -d | --decrypt_text | string | hex string used for decrypt
| None | --encrypt_file | string | path with contain on text to go use for encrypt
| None | --decrypt_file | string | path with contain on hex string used for decrypt

> [!INFO]
> python .\cryto.py --key "keyArgumentValid" --encrypt_file "text.txt" --decrypt_file "encrypted_text.txt"

equal is

> python .\cryto.py --key "keyArgumentValid" 

Using text in command line for encrypt:

> python .\cryto.py --key "keyArgumentValid" -e "encrypt this text!"

Result:

> hex: ef1010cb4b381d77aeb9d3fbff524e72c52323de08138968fdb7876658781102

Using hex in command line for decrypt:

> python .\cryto.py --key "keyArgumentValid" -d "ef1010cb4b381d77aeb9d3fbff524e72c52323de08138968fdb7876658781102"

Result:

> b'encrypt this text!'
