# Thread manager for dummies
This is an incredibly stupid tool to get around a series of problems that I was having. I was using a crude front end load testing tool in order to test something, however the test service requires multiple users. 

I set this tool up so that I can have a single page hosted locally that will spool out a series of ordered users so that the the test threads won't step on eachother. 

Normally this should be handled internall to the testing tool, however that was not an option

## To run
`docker build --tag state-tool .`

`docker run -d -p 8000:5000 state-tool`

- open localhost:8000/thread (or whatever you chose)
- every subsquent hit to this page will return the jsonified version of the next row on the linked CSV file. This is an api an can be called from the load testing thread, assuming your tool is running locally 

