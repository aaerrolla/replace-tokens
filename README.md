# replace-tokens
Python module to replace tokens in file with properties file


### Example 1

`$cat smaple_file.txt`

`image.name=@IMAGE_NAME@`  
`dev.url=@DEV_URL@`  
`smtp.replay.hostname=@SMTP_HOSTNAME@`  
`pod.name=@PROJECT_NAME@-@IMAGE_NAME@`  
`catalog.service.url=http://@CAT_HOST@/@CAT_SERVICE_ENDPOINT@`  
`catalog.service.host=@CAT_HOST@`  
`catalog.service.endpoint=@CAT_SERVICE_ENDPOINT@`   


`$cat catalog.properties`  

`IMAGE_NAME=nginx`  
`DEV_URL=http://something/index.html`  
`SMTP_HOSTNAME=129.23.4.4`  
`PROJECT_NAME=cat`  
`CAT_HOST=192.168.2.3`  
`CAT_SERVICE_ENDPOINT=/catserivce/products?WSDL`  
`

`$python token-replace.py smaple_file.txt catalog.properties`   

`resulting sample_file.txt`  
`$cat sample_file.txt`  
`image.name=nginx`  
`dev.url==http://something/index.html`  
`smtp.replay.hostname=129.23.4.4`  
`pod.name=cat-nginx`  
`catalog.service.url=http://192.168.2.3/catserivce/products?WSDL`  
`catalog.service.host=192.168.2.3`  
`catalog.service.endpoint=/catserivce/products?WSDL`  
