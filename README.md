# Trujillo 🌍

Trujillo is an experimental software that combines IPFS and Apache to serve static content on the web as a Content Delivery Network.

The current theoretical configuration is as follows: 

## WEB <-----> Apache 2 <-----> IPFS
Apache 2 works as a reverse proxy between the web user and IPFS, thats because ipfs stores files on the network and indexes with a hash. 

Because when the static content is made available on the network, the filename is lost. Apache maps the hashes to its respective filenames so that the end user can still use its original filename to reach the file.
