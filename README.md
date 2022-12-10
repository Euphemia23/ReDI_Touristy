# ReadMe for the backend

## About Touristy
Touristy is an application that provides a guide for tourists to potential tourist attractions they want to visit. This application is still under development. Feel free to watch the journey of the development. Contribution guide can also be found.  



## Frequent error observed

 - While connecting fast API with mongodb `# [PyMongo [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate](https://stackoverflow.com/questions/68123923/pymongo-ssl-certificate-verify-failed-certificate-verify-failed-unable-to-ge)` **Solution** - `Install Certifi` and  `client = motor.motor_asyncio.AsyncIOMotorClient(MONOGO_DETAILS, tlsCAFile=certifi.where())`
