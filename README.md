# Touristy - The Ultimate Travel Attraction API

Touristy is a comprehensive API for accessing information on tourist attractions around the world. With Touristy, you can easily search for attractions by location and category etc, making it the perfect tool for planning your next trip. Whether you're looking for museums, theme parks, or other activities, Touristy has you covered.

<img width="940" alt="redi_Touristy" src="https://user-images.githubusercontent.com/71856058/207550563-f631dba1-fb65-4aeb-b85f-d7711d3cf400.PNG">


## Features

- Search for attractions by location and category
- Access detailed information on each attraction
- View photos and ratings from other travelers
- Integrate with your own travel planning tools and applications

## Getting Started

Visit the API documentation and consume the API in your various applications free of charge. 


## Documentation

Visit [our website](https://touristy.azurewebsites.net/docs) for complete API documentation, including a reference guide and usage examples.

## Support

If you have any questions or need help getting started, please contact us at [agwaeuphemia21@gmail.com](mailto:agwaeuphemia21@gmail.com).

## Contributing

If you want to contribute, feel free to create a Pull request

## License

Touristy is licensed under the [MIT License](LICENSE).




## Frequent error observed

 - While connecting fast API with mongodb `# [PyMongo [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate](https://stackoverflow.com/questions/68123923/pymongo-ssl-certificate-verify-failed-certificate-verify-failed-unable-to-ge)` **Solution** - `Install Certifi` and  `client = motor.motor_asyncio.AsyncIOMotorClient(MONOGO_DETAILS, tlsCAFile=certifi.where())`
