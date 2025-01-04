class Codec():
    _chars = 'abcdefghijklmnopqrstuvwxyz'
    _chars += _chars.upper()
    _chars += '0123456789'
    _chars += ' ,.;:"\'!@#$%^&*()_+={}[]|?/<>`~\n\t'
    
    def __init__(self):
        self._pass_phrase = 'a'

    @property
    def pass_phrase(self):
        return self._pass_phrase
    
    @pass_phrase.setter
    def pass_phrase(self, value):
        self._pass_phrase = value;
    
    def encode(self, message: str) -> str:
        return self._encode_decode(message, True)
    
    def decode(self, code: str) -> str:
        return self._encode_decode(code, False)
    
    def _encode_decode(self, text, encode) -> str:
        sign = 1 if encode else -1
        code = ''
        numchars = len(Codec._chars)
        for i in range(len(text)):
            index = Codec._chars.index(text[i])
            if index >= 0 and len(self._pass_phrase) > 0:
                ii = i % len(self._pass_phrase)
                offset = Codec._chars.index(self._pass_phrase[ii])
                new_index = (index + sign * offset + numchars) % numchars
                code += Codec._chars[new_index]
            else:
                code += text[i]
        return code
    
if __name__ == '__main__':
    codec = Codec()
    message = 'Hello, mother. May I have pie?'
    codec.pass_phrase = 'phrase0'
    print(codec.pass_phrase)
    code = codec.encode(message)
    print(code)
    print(codec.decode(code))