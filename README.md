# replace-tokens
Python module to replace tokens in file with properties file

# Example 1

$cat smaple_file.txt

image.name=@IMAGE.NAME@  
dev.url=@DEV.URL@  
smtp.replay.hostname=@SMTP.HOSTNAME@  
pod.name=@PROJECT.NAME@-@IMAGE.NAME@  
catalog.service.url=http://@CAT.HOST@/@CAT.SERVICE.ENDPOINT@  
catalog.service.host=@CAT.HOST@  
catalog.service.endpoint=@CAT.SERVICE.ENDPOINT@  


$cat catalog.properties

IMAGE.NAME=nginx  
DEV.URL=http://something/index.html  
SMTP.HOSTNAME=129.23.4.4  
PROJECT.NAME=cat  
CAT.HOST=192.168.2.3  
CAT.SERVICE.ENDPOINT=/catserivce/products?WSDL  


$python token-replace.py smaple_file.txt catalog.properties  

resulting sample_file.txt  
$cat sample_file.txt  
image.name=nginx  
dev.url==http://something/index.html  
smtp.replay.hostname=129.23.4.4  
pod.name=cat-nginx  
catalog.service.url=http://192.168.2.3/catserivce/products?WSDL  
catalog.service.host=192.168.2.3  
catalog.service.endpoint=/catserivce/products?WSDL  




