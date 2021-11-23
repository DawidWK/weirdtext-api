# WEIRDTEXT API

## ENDPOINTS:

- encode: /api/v1/encode
- decode: /api/v1/decode

### ENCODE

Make get request to ENCODE endpoint, with sentecne param

```
import requests
URL = "https://weirdtext-api-dawidwk.herokuapp.com/api/v1/decode"
params = {
    "sentence": "This is a long looong test sentence,\nwith some big (biiiiig) words!"
}
r = requests.get(url=URL, params=params)
```

### DECODE

Make get request to DECODE endpoint, with encoded_sentence and orginal_words params (both are required)

```
import requests
URL = "https://weirdtext-api-dawidwk.herokuapp.com/api/v1/decode"
params = {
    "encoded_sentence": "\n—weird—\nTihs is a lnog loonog tset setncene, wtih smoe big (biiiiig) wdros!\n—weird—\n",
    "orginal_words": "long looong sentence some test This with words"
}
r = requests.get(url=URL, params=params)
```
