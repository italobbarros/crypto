from src.aes import crypto_aes

def main():
    try:
        crypt = crypto_aes()
        crypt.run_encrypt()
        crypt.run_decrypt()
    except Exception as e:
        print(e)

if (__name__ == "__main__"):
    main()