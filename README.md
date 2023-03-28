# MediaFuneral
LSOFT ListServ Cookie Credential Leak PoC

# Suggested Description
The WALOGIN cookie set on authentication to Listserv contains encoded user credentials - both username and password. The username is ASCII HEX encoded which is trivial to decode, while the password is encoded using XOR with the key `0xAA`, then hex encoded.
This compromises account credentials and allows account takeover.

## Software Affected
LSOFT Listserv version <=16.0, 16.5 where `WA_USE_INSECURE_COOKIE=1` is set in config file.

## Attack Type
Remote

## Impact
Information Disclosure

## Affected Components
"WALOGIN" session cookie.

## Attack Vectors
If session cookie is exposed, weak encoding of username and password in cookie allows for trivial decoding. 


## How to Use the script
The WALOGIN Cookie is generated in the format:
`75736572406578616d706c652e636f6d-DACBD9D9DDC5D8CE9B9899-AoM`
The first section is the ASCII Hex encoded username.
The second section is the encoded password, delimited by `-`.
This tool is designed to encode and decode this second section of the cookie.

### Syntax
`mediafuneral.py (-e | -d) credential`

argument | Description
--- | ---
`-e`, `--encode` | encodes the input credential to be placed in a cookie
`-d`, `--decode` | decodes the supplied cookie back to plaintext
`credential` | either the plaintext password to be encoded, or the encoded password to be recovered


### Example
```
.\media-funeral.py -d DACBD9D9DDC5D8CE9B9899
Mode: Decoding
Input: DACBD9D9DDC5D8CE9B9899
Output: password123
```

![Media-Funeral-Screenshot](https://user-images.githubusercontent.com/126897012/228221538-5cfb251c-5a17-4f93-8c3e-5db6187fbbc0.png)




## Discoverers
Matthew McKechnie & Kirk Preston
