def vernam_criptografar(mensagem, chave):
    if len(mensagem) != len(chave):
        raise ValueError("A chave deve ter o mesmo comprimento que a mensagem.")

    mensagem_bytes = mensagem.encode('utf-8')
    chave_bytes = chave.encode('utf-8')

    texto_cifrado_bytes = bytearray(len(mensagem_bytes))
    for i in range(len(mensagem_bytes)):
        texto_cifrado_bytes[i] = mensagem_bytes[i] ^ chave_bytes[i]

    return texto_cifrado_bytes.hex()

def vernam_descriptografar(mensagemCifrada, chave):
    mensagemCifradabytes = bytearray.fromhex(mensagemCifrada)
    chave = chave.encode('utf-8')

    if len(mensagemCifradabytes) != len(chave):
        raise ValueError("A chave deve ter o mesmo comprimento que o texto cifrado.")

    mensagemDescriptografada = bytearray(len(mensagemCifradabytes))
    for i in range(len(mensagemCifradabytes)):
        mensagemDescriptografada[i] = mensagemCifradabytes[i] ^ chave[i]

    return mensagemDescriptografada.decode('utf-8')

mensagem = "vocevaiseratacado"
chave = "XMCKLUEAOPWUNFTRW"

mensagemCifrada = vernam_criptografar(mensagem, chave)
print(f"Texto cifrado: {mensagemCifrada}")

mensagemDecifrada = vernam_descriptografar(mensagemCifrada, chave)
print(f"Texto decifrado: {mensagemDecifrada}")
