# Single-File Python Development (SFPD)
Programming can at times be enjoyable, but it surely is frustrating when you find yourself repeating tasks. Repeatedly typing long multi-line inputs as I try to test and improve my code has been one of these frustrating moments for me. 
**This small project is an attempt in improving the development process of single-file python programs**, as well to document my progress with Python.

## Features
- **Easier Testing:** Store inputs as a text file and a test command for easier testing
- **Version Control:** Create a copy of the current program and its output to be able to easily compare file differences or go back to a previous version

## Considerations
- This project was developed with VS Code in mind. Using other Integrated Development Environments(IDEs) might lead to a different user experience
- This project was developed for efficiently making single-file Python programs intended for submission in OJ(DMOJ)

## Getting Started

1. **Clone or download**

    Create a copy of this project by either cloning the repository or downloading the project as a zip file and unzipping it

    ```bash
    git clone https://github.com/ming-suhi/single-file-python-development.git
    ```

2. **Open in VS Code**

    Open the project in VS Code and a terminal in the project's root directory

3. **Create a new project**

    Create a new project by running the following command, replacing `<projectName>` with your desired project name

    ```bash
    py -m create --name="<projectName>"
    ```

4. **Edit input and expected output**
    
    Now you will see a newly created folder for your project. Edit `input.txt` with the test inputs you wish to test and `expected-output.txt` with the outputs your are expecting

5. **Write your program**

    Create your program in `index.py` like how you normally would

6. **Run your tests**

    To test your program in the terminal run
    
    ```bash
    py -m <projectName>.testing.test
    ```
    
    To save a copy of the current program and its output run

    ```bash
    py -m <projectName>.testing.test --save="<fileName>"
    ```

    The copy is stored as `.txt` file that can be found in the `stream` directory of your project

## License
MIT © Kyle Taton