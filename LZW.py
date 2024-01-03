def compress(plainText):

    # sözlük oluşturma.
    dictionary_size = 256
    dictionary = dict((chr(i), i) for i in range(dictionary_size))

    word = ""
    result = []
    for char in plainText:
        wordchar = word + char
        if wordchar in dictionary:
            word = wordchar
        else:
            result.append(dictionary[word])
            # wordchar sözlüğe ekle
            dictionary[wordchar] = dictionary_size
            dictionary_size += 1
            word = char

    if word:
        result.append(dictionary[word])
    return result


def decompress(compressedText):
    from io import StringIO

    # sözlüğü oluştur
    dictionary_size = 256
    dictionary = dict((i, chr(i)) for i in range(dictionary_size))
    result = StringIO()
    word = chr(compressedText.pop(0))
    result.write(word)
    for k in compressedText:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dictionary_size:
            entry = word + word[0]
        else:
            raise ValueError('Bad compression k: %s' % k)
        result.write(entry)

        dictionary[dictionary_size] = word + entry[0]
        dictionary_size += 1

        word = entry
    return result.getvalue()


# Derste verilen örneği test edelim
compressedText = compress('ABABBABCABABBA')
print (compressedText)
decompressedText = decompress(compressedText)
print (decompressedText)