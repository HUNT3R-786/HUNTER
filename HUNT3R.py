# Compiled By Mr Mafia | Muhammad Muzammil
# Github :  https://github.com/Muzammil-404

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))