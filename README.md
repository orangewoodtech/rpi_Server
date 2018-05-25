# rpi_Server

# How to Run the Server : 


Below are the commands that you need to use : 

1. GO to the Code Directory ( as code location is currently on Desktop ) 

```
cd Desktop/code/myapp/
```

2. Now start the uwsgi server , uwsgi is deployed so as to make the webpage
  accessible to multiple users , Flask only offers the webpage to only one user . 

```	
uwsgi --socket 0.0.0.0:8080 --protocol=http -w run:app
```

3. After this command , you can access the Server ( contatining the webpage ) over the Local Network . 


## Reference : 


**To know how to integrate uwsgi for Flask Framework , Read here : **

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)


Note : You need to do some modifications that is change the location where the files will be uploaded to ( onto the Server ) .

Here are the steps that you need to follow : 

1. Go to Code Folder ( which you might have downloaded from Github ) 
2. Go to myapp Folder 
3. Now open the "app.py" inside any editor 
4. Now search for "target" ( using Find ( Ctrl + F ) ) 
5. Change its value as per the Location where you want to save the files 


