# MediaFuneral
LSOFT ListServ Cookie Credential Leak PoC

## Issue Description
The WALOGIN cookie set on authentication to Listserv contains encoded user credentials - both username and password. The username is ASCII HEX encoded which is trivial to decode, while the password is encoded using XOR with the key `0xAA` then converted to hex. 

## Software Affected
LSOFT Listserv version 16.5 confirmed.
