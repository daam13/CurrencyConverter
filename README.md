# Curency Converter

Currency Converter is a web application that translates a given amount of money from one currency to another. The currencies supported are USD, CRC, JYP, EUR, GBP, MXN, and VEF. 

The algorithm to make this translation receives three parameters: a string with an initial currency, a float with the amount of money desired to convert, and another string with the final currency. The default values are 'USD', 1.0, and 'USD ' respectively. 

This project aims to implement the use of concurrency, having multiple clients (individual threads) accessing at the same time and changing the shared log file successfully. In addition, this web application is uploaded as a Docker Image so it was necessary to create Dockerfile to build it.

## Getting Started
### *1.	Installation process*
#### Building your own image
First, change your working directory to the one that contains the Dockerfile. Then run 	the following command: 
```bash
		docker build -t <image-name> .
```

This will execute the steps defined in the Dockerfile, which will pull the necessary image and put the software dependencies of the WebApp inside the image. 

The advantage of this process is that you can modify the app’s source code and other resources as you need.

#### Pulling the image from Docker Hub
Of course, you can have a ready-to-deploy image by getting it from this [Docker Hub repository](https://hub.docker.com/r/albcarlos/currency_converter).
However, if you find it easier, just running the following command will pull the image:
```bash
		docker pull albcarlos/currency_converter:latest
```


#### Running the application
Once you have the image added through either of the mentioned methods, now you can run the app inside a container. To achieve this, use the following command:

```bash
		docker run -d -p 5000:5000 <image-name>
```
It is important to note that the *<image-name>* inserted must coincide with the one you created the image. The port `5000` must not be changed, because the app is designed to run in the default Flask Port which is 5000. For example, assuming the *“image name”* is ‘currency_converter’, this should run successfully:

```bash
		docker run -d -p 5000:5000 currency_converter
```
The service should be now exposed and the index page should be accessed by simply writing http://localhost:8000 in the browser.

### *2.	Software dependencies*
- Python
- Flask
- Docker

### *3.	API references*
The backend receives a request within the query parameters including the initial currency (“from”), the final currency (“to”), and the amount of money (“amount”). The response is a JSON formatted string with the amount resulting from the conversion.

## Tests  
Upon entering the application the following will be presented on the browser:
    
![MicrosoftTeams-image](https://user-images.githubusercontent.com/76136318/176325564-dadee04b-9768-43bc-a1f5-e7c7e66ae89b.png) 

*Fig. 1 - Basic view*
    
Select an option from the dropdown menus respectively (`from` and `to` currencies) and fill in the `amount` of money to convert.
    
    
After clicking on the *convert* button the response from the API will be shown below, as follows:
    
![MicrosoftTeams-image (1)](https://user-images.githubusercontent.com/76136318/176325562-5766abee-0685-4a56-a59c-10e7b76aba0a.png)


*Fig. 2 - Conversion result*

---    
To check that the access was correct it's possible to list the working directory to see that the log.txt exists and also to obtain the complete log of requests of the service with the following commands.

```bash
	docker exec -it <container-name | container-id> /bin/sh
	ls
	cat log.txt 
```
   
---
Team members:
- Carlos Albornoz
- Gianluca Gibellato
- Darla Albornoz

:tiger:
