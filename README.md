# strategy-onboarding

Hey, welcome to strategy onboarding! We're experimenting with a new onboarding setup, and always welcoming feedback.

This is intended as more of an introduction to Python, which is the primary language we use for strategy projects, and some libraries around it. If you're more familiar with Python, this might only take you a couple minutes.

Feel free to message Emma Wai on Slack with any questions.

## Usage

There's a couple exercises:

- Fibonacci: Implement `fibonacci_term()` in `onboarding/fibonacci.py`. Check your work by running unit tests. The unit test framework we are using is `pytest` -> to run these, install the necessary packages (see below) and run `pytest` in terminal/command line
- Array: Implement `find_min_index()` and `reverse_str_arr()` in `onboarding/array.py`. This time, you'll have to write the test cases in `test_array.py`
- Matplot: We put together some very simple data in `test_data.csv`. Read it and graph it using Matplotlib

Once you're done, open a pull request (PR) with all these changes and tag `@e-wai` for a review.
If you're waiting on a review, please take a look through the MSXIV work (https://github.com/uw-midsun/strategy) and come up with questions about what we've designed, or how we implemented certain things

## Setup Help

- Install python and git. Check that both exist on your computer with:

    ```zsh
    python --version
    git --version
    ```

- Use command line/terminal to navigate your computer's file system. `cd <directory-name>` to go down a level to the directory, or `cd ..` to go up a level.
- Clone the repo into the location you want using

    ```zsh
    git clone https://github.com/uw-midsun/strategy-onboarding.git
    ```

- Using Python's virtualenv is a nice, easy way to manage installation packages: https://docs.python.org/3/library/venv.html. You'll need to install `pytest`. We have all the required packages stored in a `requirements.txt` file, which becomes especially useful once there are more required packages:

    ```zsh
    pip install -r requirements.txt
    ```

- Check that the test suite works with:

    ```zsh
    pytest
    ```

    If you want more information on pytest, see the [docs](https://docs.pytest.org/en/6.2.x/)