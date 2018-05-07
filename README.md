# Website-Status

A simple project for checking my website status.
This repo contains 3 tests:

1. Simple HTML test (Web hosting)
2. Simple PHP test (PHP echo function test)
3. Wordpress Test (parse a string from a wordpress page)


### How to Use
1. Put files in Server folder to your server
2. If you have wordpress, create a "page" with context `Test3: OK`, then publish
3. Modify `config.json`, you should setup the URL for test pages
4. If you have IFTTT account, then you can use a webhook to app notification applet
5. Fill IFTTT trigger URL and key
6. Setup crontab on your server
7. Done!

### If my server is totally down?
So I host the client script on another server.
