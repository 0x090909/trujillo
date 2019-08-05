# Trujillo 🌍

Trujillo is an experimental software that combines IPFS and Apache to serve static content on the web as a Content Delivery Network.

The current theoretical configuration is as follows: 

## WEB <-----> Apache 2 <-----> IPFS
Apache 2 works as a reverse proxy between the web user and IPFS, thats because ipfs stores files on the network and indexes with a hash. 

Because when the static content is made available on the network, the filename is lost apache is needed to map the hashes to its respective filenames so that the end user can still use its original filename to reach the file.

### Generate content mapping
```bash
python map_generator.py /path/to/static/content
```
This command generates a file `map_file.txt` similar to this :

```bash
uno.jpg QmR4JyPyhaMYfD6HsNg89ptB2mYm87xhY5wtZiruWQA8Jb
due.jpg QmWfY9tBZ3QioKQbZF3ZvwWb4MFu1n18b3cVtDAQA9kmXo
dieci.jpeg QmeHC4FjiQmEKuSVSxo2R7k4GyJAGmbV1WbcJruTjKKz6R
tre.jpg QmR2zCfJTderfnPjjCECWJW6GdYMKN5H3hT3G7rRE1n7k7
undici.png QmNgpGQQee7a88M7vUGWaJ5iSGC4zg7FBwdeyUN3V7QVsK
quattro.jpg QmYzvpftG55xbE4SsZG3mEvSJFm5y5NkLHtKPsiyP9aG8U
cinque.jpg QmZHPsXzjPbGa2XVgoDAgHeQYs247GCpKk4VFDDZqJhWvS
```

`map_file.txt` will be then used in the VirtualHost file to configure the reverse proxy.



