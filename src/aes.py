from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import codecs
import getopt, sys
 

class crypto_aes():
    def __init__(self):
        self.BLOCK_SIZE = 32  # Bytes
        self.key = None 
        self.path_text_file = 'files/text.txt'
        self.text=None
        self.path_decrypt_file = 'files/encrypted_text.txt'
        self.decrypt_text = None
        self.get_parameters()

    def get_parameters(self):
        try:
            argumentList = sys.argv[1:]

            # Options
            options = "hd:e:k:"
            
            # Long options
            long_options = ["key=","encrypt_text=","decrypt_text=", "encrypt_file=","decrypt_file=", "help"]
            
            # Parsing argument
            arguments, values = getopt.getopt(argumentList, options, long_options)
            
            # checking each argument
            for currentArgument, currentValue in arguments:
                if(currentValue is not None):
                    if currentArgument in ("-h", "--help"):
                        print ("Displaying Help")
                    elif currentArgument in ("-e", "--encrypt_text"):
                        self.text = currentValue
                    elif currentArgument in ("-d", "--decrypt_text"):
                        self.decrypt_text = currentValue  
                    elif currentArgument in ("--encrypt_file"):
                        self.path_text_file = currentValue
                    elif currentArgument in ("--decrypt_file"):
                        self.path_decrypt_file = currentValue
                    elif currentArgument in ("-k", "--key"):
                        self.key = currentValue
                    
        except getopt.error as err:
            # output error, and return with an error code
            print (str(err))

    def write_file(self,msg,path):
        cont = 0
        with open(path, "w+") as file:
            for b in msg:
                if (cont == 16):
                    cont = 0
                    file.write("\n")
                val = hex(b)[2:]
                if (len(val) == 1):
                    file.write(f"0{val}")
                else:
                    file.write(f"{val}")
                cont += 1

    def encrypt(self, key: str):
        if(self.text is not None):
            cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
            return cipher.encrypt(pad(self.text.encode(), self.BLOCK_SIZE))
        else:
            return None

    def encrypt_file(self,path: str,path_encrypt:str, key: str):
        with open(path, 'r') as file:
            self.text = file.read()
        msg = self.encrypt(key)
        self.write_file(msg,path_encrypt)
        print("Encripted file!")
        return msg

    def decrypt(self, key: str):
        if(self.decrypt_text is not None):
            decipher = AES.new(key.encode('utf8'), AES.MODE_ECB)
            msg_dec = decipher.decrypt(
                codecs.decode(
                    bytes(self.decrypt_text, encoding='utf-8'), "hex")
            )
            return unpad(msg_dec, self.BLOCK_SIZE)
        else:
            return None

    def decrypt_file(self,path: str, key: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.decrypt_text = file.read().replace("\n", "")
        print("Decripted file!")
        return self.decrypt(key)

    def run_encrypt(self):
        if(self.decrypt_text is None):
            if(self.text is not None):
                print("hex: "+self.encrypt(self.key).hex())
            else:
                self.encrypt_file(self.path_text_file,self.path_decrypt_file,self.key)

    def run_decrypt(self):
        if(self.decrypt_text is not None and self.text is None):
            print(self.decrypt(self.key))
        else:
            print(self.decrypt_file(self.path_decrypt_file,self.key))



