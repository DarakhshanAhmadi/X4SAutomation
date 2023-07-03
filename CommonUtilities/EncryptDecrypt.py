from base64 import b64encode, b64decode

from Crypto.Cipher import AES


class EncrptDecrpt:
    key = 'RrAutomateEncDec'

    def __init__(self, salt='SlTKeYOpHygTYkP3'):
        self.salt = salt.encode('utf8')
        self.enc_dec_method = 'utf-8'

    def encrypt(self, str_to_enc=None):
        try:
            aes_obj = AES.new(self.key.encode('utf-8'), AES.MODE_CFB, self.salt)
            hx_enc = aes_obj.encrypt(str_to_enc.encode('utf8'))
            mret = b64encode(hx_enc).decode(self.enc_dec_method)
            print(f'Encrypted: {mret}')
            return mret
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Encryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Encryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)

    def decrypt(self, enc_str=None):
        try:
            aes_obj = AES.new(self.key.encode('utf8'), AES.MODE_CFB, self.salt)
            str_tmp = b64decode(enc_str.encode(self.enc_dec_method))
            str_dec = aes_obj.decrypt(str_tmp)
            mret = str_dec.decode(self.enc_dec_method)
            return mret
        except ValueError as value_error:
            if value_error.args[0] == 'IV must be 16 bytes long':
                raise ValueError('Decryption Error: SALT must be 16 characters long')
            elif value_error.args[0] == 'AES key must be either 16, 24, or 32 bytes long':
                raise ValueError('Decryption Error: Encryption key must be either 16, 24, or 32 characters long')
            else:
                raise ValueError(value_error)


"""
The main method will be required if some modification is required in this file for example if we need to change key then after changing the key we need to uncomment the main to generate the exe file.
"""
# if __name__ == '__main__':
#     test_crpt = EncrptDecrpt()
#     option = input("Enter 1-Encrypt and 2-Decrypt. Enter your choice? ")
#     if int(option.strip()) == 1:
#         text_to_encrypt = input("Enter the key/password to encrypt ")
#         test_enc_text = test_crpt.encrypt(text_to_encrypt)
#     else:
#         test_enc_text = input("Enter the text to decrypt ")
#         try:
#             test_dec_text = test_crpt.decrypt(test_enc_text)
#         except:
#             print("Exception occur during derypt")
# """
