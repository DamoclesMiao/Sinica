import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

