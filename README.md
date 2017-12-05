# Installation 

## Windows

1. Install Python-3.6.3 for Windows. You can find the link at:

    [https://www.python.org/downloads/release/python-363/](Download Here)

2. Create PYTHON_HOME environment variable:

    ``` PYTHON_HOME = %LOCALAPPDATA%\Programs\Python\Python3.6 ```

3. Add to Path:

    ``` PATH = %PYTHON_HOME%; %PYTHON_HOME%\Scripts ```

4. Check the installation:

    ``` Run cmd.exe ```
    ``` Run python ```

5. Install PipEnv. To read more about Pipenv have a look here:

    https://docs.pipenv.org/

    To install run:

    ``` pip install pipenv ```

6. Clone the dashboard repository:

    ``` git clone https://github.com/bwghughes/nbenvstatus.git ```

7. Install the dependencies:

    ``` pipenv install ```

8. Run the tests:

    ``` runtests.bat ```

9. Run the dashboard server:

    ``` start-server.bat ```

## Updating Code

1. Pop into the directory and issue the following:

    ``` git pull ```








