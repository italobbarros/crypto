# Commands for use that API.


| cmd | cmd long | type |  description |
|:-:|:-:|:-:|:-:|
| -h | --help | None | print the options
| -k | --key | string | key used for encrypt your data
| -e | --encrypt_text | string | text to go use for encrypt
| -d | --decrypt_text | string | hex string used for decrypt
| None | --encrypt_file | string | Path containing file with string to encrypt
| None | --decrypt_file | string | Path containing file with hex string to decrypt

## Without Docker
> python .\app.py --key "keyArgumentValid" --encrypt_file "text.txt" --decrypt_file "encrypted_text.txt"

equal a

> python .\app.py --key "keyArgumentValid" 

Using text in command line for encrypt:

> python .\app.py --key "keyArgumentValid" -e "encrypt this text!"

Result:

> hex: ef1010cb4b381d77aeb9d3fbff524e72c52323de08138968fdb7876658781102

Using hex in command line for decrypt:

> python .\app.py --key "keyArgumentValid" -d "ef1010cb4b381d77aeb9d3fbff524e72c52323de08138968fdb7876658781102"

Result:

> b'encrypt this text!'

## With Docker

### Build a docker image
> docker build -t crypto:0.1 .

### Run a docker container
> docker run -d -t --name crypto -it crypto:0.1

### Run command in docker container
> docker exec b59f3486b44a python app.py --key "keyArgumentValid" -e "encrypt this text!"