# API LFG

The project is the final step of GeeksHub's Python Backend course. 

## Motivation

Due to the health situation, our company has been
working remotely since March 2020. This has involved
that our colleagues have lost human contact
that has always been had, and is something that the company wants
change.

The company wants to give a boost to the way they have
workers to relate, allowing them to contact each other
them creating interest groups.
A first phase of this project is the creation of an api
LFG website, which allows employees to contact
with other classmates to form groups to play a game
video game, with the aim of being able to share a moment of
afterwork leisure.

## Method and results

We use Django and Django rest framework as our main technology stack combined with postressql to create our API.
The Api serve the endpoints to satify the next functional requirements:

∙ RF.1 Users must be able to register to the application, establishing a username / password.
∙ RF.2 Users have to authenticate to the application by logging in.  
∙ RF.3 Users have to be able to create Partías (groups) for a certain video game.  
∙ RF.4 Users have to be able to search for Games by selecting a video game.  
∙ RF.5 Users can enter and exit a Party.  
∙ RF.6 Users must be able to send messages to the Party. These messages must be able to be edited
       and deleted by their creator user.  
∙ RF.7 The messages that exist to a Party have to be viewed as a common chat.  
∙ RF.8 Users can enter and modify their profile data, for example, their Steam user.  
∙ RF.9 Users must be able to log out of the web application.  


## Repository overview

├───LFG_PROJECT  
│	├───API_LFG  
│   │	│	├───admin  
│   │	│	├───apps  
│   │	│	├───serializers  
│   │	│	├───models  
│   │	│	├───test  
│   │	│	├───urls  
│   │	│	├───views  
│	│   │  
│	├───LFG_PROJECT    
│   │	│	├───asgi    
│   │	│	├───settings  
│   │	│	├───urls  
│   │	│	├───wsgi  
│   │	│	├───views  
│	├───templates  

##Avaible Endpoints
###Api_LFG Endpoints
       /videogame',         #ALL CRUD OPERATIONS   
       /partia',            #GET/POST OPERATIONS   
       /partia_user',       #POST/DELETE OPERATIONS
       /ChatEditMsg',       #GET/PUT/DELETE
       /chatlist',          #GET OPERATIONS
       /SendChatMsg         #POST OPERATIONS
       /UserProfile         #ALL CRUD OPERATIONS

###Third party endpoints
  The Api use django rest framework and for this reason its going to be available 
  all endpoints provided by DRF like login/logout/registration

## Running instructions && Package Requirements
    To run this project you will need to install with pip the follow packages at least 
    with the indicated version:
        -Django             v.3.2.7
        -Django-allauth     v.0.4.5
        -Django-rest-auth   v.0.9.5
        -Psycopg2           v.1.91
        -Pillow             v.8.4.0


