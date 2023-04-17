```


   ,---,           ,---,        ,---,       ,---,  .--.--.                             ,-.----.       ,---,.               ,---,    ,---,.           .---. 
  '  .' \        .'  .' `\    .'  .' `\  ,`--.' | /  /    '.                           \    /  \    ,'  .' |       ,---.,`--.' |  ,'  .' |          /. ./| 
 /  ;    '.    ,---.'     \ ,---.'     \ |   :  :|  :  /`. /             ,---,.        ;   :    \ ,---.'   |      /__./||   :  :,---.'   |      .--'.  ' ; 
:  :       \   |   |  .`\  ||   |  .`\  |:   |  ';  |  |--`            ,'  .' |        |   | .\ : |   |   .' ,---.;  ; |:   |  '|   |   .'     /__./ \ : | 
:  |   /\   \  :   : |  '  |:   : |  '  ||   :  ||  :  ;_            ,---.'   ,        .   : |: | :   :  |-,/___/ \  | ||   :  |:   :  |-, .--'.  '   \' . 
|  :  ' ;.   : |   ' '  ;  :|   ' '  ;  :'   '  ; \  \    `.         |   |    |        |   |  \ : :   |  ;/|\   ;  \ ' |'   '  ;:   |  ;/|/___/ \ |    ' ' 
|  |  ;/  \   \'   | ;  .  |'   | ;  .  ||   |  |  `----.   \        :   :  .'         |   : .  / |   :   .' \   \  \: ||   |  ||   :   .';   \  \;      : 
'  :  | \  \ ,'|   | :  |  '|   | :  |  ''   :  ;  __ \  \  |        :   |.'           ;   | |  \ |   |  |-,  ;   \  ' .'   :  ;|   |  |-, \   ;  `      | 
|  |  '  '--'  '   : | /  ; '   : | /  ; |   |  ' /  /`--'  /        `---'             |   | ;\  \'   :  ;/|   \   \   '|   |  ''   :  ;/|  .   \    .\  ; 
|  :  :        |   | '` ,/  |   | '` ,/  '   :  |'--'.     /                           :   ' | \.'|   |    \    \   `  ;'   :  ||   |    \   \   \   ' \ | 
|  | ,'        ;   :  .'    ;   :  .'    ;   |.'   `--'---'                            :   : :-'  |   :   .'     :   \ |;   |.' |   :   .'    :   '  |--"  
`--''          |   ,.'      |   ,.'      '---'                                         |   |.'    |   | ,'        '---" '---'   |   | ,'       \   \ ;     
               '---'        '---'                                                      `---'      `----'                        `----'          '---"      
                                                                                                                                                           



```
                                                                                                                                                           
# ADDIS-REVIEW     
__a website where you can review foods in addis__
#

## Description
[`Addis-RevieW`](http://18.205.104.232:5000/) is a food rating and commenting website made for those who live in Ethiopia, near Addis Ababa
> ##
> You can find [YT Demo Video here 🔗](https://youtu.be/fqli-IG-bbQ)
> ##
> You can find [WebSite link here 🔗](http://18.205.104.232:5000/)
> ##
> You can find [GitHub Source code 🔗](https://github.com/rawidaniel/AddisReview/)
> ##

### How does it work?
The website lists top restaurant in the capital city of Ethiopia and makes it easy for visitors, food travlers and tourists to chose where to dine before going there.
The user can read reviews and see the average rate of the food which makes it easy for choosing restaurant that is best in town ! The user can also create an account and
 write review and rate the foods he chose.

### For whom?
This is made for everyone who enjoys trying out new restaurants but also curious on the money they spend. i.e. Food Travlers, Mukbang lovers, Tourists, Grooms, Visitors ...

### Inspiration
We always see other similar websites on the internet, but lets be honest, they don't have Ethiopian food and you can't use them. That is when we thought there should be a website like that where
 our people enjoy both traditional and junk foods. :)

## How to run the project
The website is made using docker. There are three containers to run on your machine if you like to run it on your PC. 

######
> NOTE: If you want to use Docker to run the application, make sure you have machine with 4 Core CPU, 8GB RAM, 25GB Storage. Also make sure to install all dependencies before running the app, i.e. install `docker`, `docker-compose`, `python3` ... Otherwise you will have issue when running the application !
######

### Running the DataBase container from Docker-Compose Orchestration
>The website uses `PostgreSQL`.
> There is already premade docker image for our application namely `Dockerfile.postgres` and `Dockerfile.flask`
>To run it using docker
```bash
git clone https://github.com/rawidaniel/AddisReview.git
```
to run it interactively or 
```bash
docker-compose up
```
to run it on the background
```bash
docker-compose up -d
```
to stop it
```bash
docker-compose down
```

> This will run all the front end (on PORT 5000), the backend and postgres DB (on PORT 5432)

### Running the DataBase container Individually
If you want to run the postgres SQL DB or the Flask APP separetly, you can do so.
>Clone the github repository
```bash
git clone https://github.com/rawidaniel/AddisReview.git
```
>To build `PostgreSQL` Server Container
```bash
docker build -t my-postgres -f Dockerfile.postgres .
```
>To run the `PostgreSQL` Server Container
```bash
docker run -p 5432:5432 --name my-postgres-container -d my-postgres
```
######
>To build `Flask APP` Server Container
```bash
docker build -t my-flask-app -f Dockerfile.flask .
```
>To run the `Flask APP` Server Container
```bash
docker run -p 5000:5000 --name my-flask-app-container --link my-postgres-container:database -d my-flask-app
```
######
> NOTE: You might need to set up your own docker network for the Flask app to connect to Postgres database

if you have NGINX on your server and you know how to use it, you should use gunicorn for the application server.

## How to use the project
It is pretty simple as using any website on the internet. But here are the steps:
- [Create a new account](http://18.205.104.232:5000/signup).
- This will direct you to login page. You need to login for extra security [Login](http://18.205.104.232:5000/login).
- Now you will be redirected to the `RESTAURANT` page, where you get to see lists of the restaurants in the database. You need to choose one to look there food.
- Now you see the food, there rate and price. click on which ever you want to see reviews and rate as well as to put your own review and rate.
- There you go ! You did it.

## Credits and Remarks
* Thank you all

## How to contribute to the project 
You should contact us:
> See the developer sections below.

## Developers
* [ABENEZER ESHETIE - GitHub](https://github.com/EbenGitHub)
* [RAWI DANIEL - GitHub](https://github.com/rawidaniel)
* [IKRAM AWOL - GitHub](https://github.com/ikramawol)

## Related Projects
* AirBnB Clone

## License
 --
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
                                                                                                                                                           
```



   __    __    _  _           ___  ____     ___  _____  _   _  _____  ____  ____    ___ 
  /__\  (  )  ( \/ )   ___   / __)( ___)   / __)(  _  )( )_( )(  _  )(  _ \(_  _)  | __)
 /(__)\  )(__  )  (   (___)  \__ \ )__)   ( (__  )(_)(  ) _ (  )(_)(  )   /  )(    |__ \
(__)(__)(____)(_/\_)         (___/(____)   \___)(_____)(_) (_)(_____)(_)\_) (__)   (___/




```


[ALX SE School](https://alxafrica.com)
