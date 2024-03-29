## Getting Started with Catalyst_count

## To run the application server locally follow the below steps:
1. Install git on a system to checkout the project locally.
    > If you don't have Git installed already, follow the relevant link below 
    - Check the link: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

2.	Checkout project
    - use a command to clone
    ``` 
        git clone https://github.com/anantkoli/catalyst_count.git 
    ```
    - Check the link to clone project: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository

3.	Install Docker to run the application server
    > If you don't have Docker installed already, follow the relevant link below to get
    - Windows > https://docs.docker.com/desktop/install/windows-install/
    - MacOS > https://docs.docker.com/desktop/install/mac-install/
    - Linux > https://docs.docker.com/desktop/install/linux-install/

4.	Now go to checkout project folder using cmd
    ``` 
    cd <checked_path>/catalyst_count
    ```

5.	Run docker command on the terminal. Make sure you are inside the project folder. Wait till it builds and runs.
    ```
    docker-compose up -d
    ```

6.	You can now check the container running using cmd
    - windows, macOS > ``` docker ps -a ```
    - Linux > ``` sudo docker ps -a ```

7.  Now install the requirements using the below command make sure you installed Python if not use [this link](https://www.javatpoint.com/how-to-install-python)
    - ``` pip install -r requirements ```

8.  Now, we need to migrate the changes using the following commands
    - ``` python manage.py makemigrations ```
    - ``` python manage.py migrate ```

9.  Now run the server using the command
    - ``` python manage.py runserver ```

10.	Now your app is running **successfully**

11.	Go to the browser and search for (http://127.0.0.1:8000/) to login and try the application.
