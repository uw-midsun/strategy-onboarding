# Task 2 - Coding exercises

These coding exercises are to make sure that you're familar with Python and the tools that we use.

## Step 1

Install [python](https://www.python.org/downloads/) (version 3.10 and above is ok) and [git](https://git-scm.com/downloads). You can check that both exist on your computer with:

```zsh
python --version
git --version
```

## Step 2

- Use command line/terminal to navigate your computer's file system. `cd <directory-name>` to go down a level to the directory, or `cd ..` to go up a level.
- Clone the repo into the location you want using

  ```zsh
  git clone https://github.com/uw-midsun/strategy-onboarding.git
  ```

## Step 3

Using Python's virtualenv is a nice, easy way to manage installation packages: https://docs.python.org/3/library/venv.html. You'll need to install `pytest`. We have all the required packages stored in a `requirements.txt` file, which becomes especially useful once there are more required packages:

```zsh
python -m venv .venv
source .venv/scripts/activate (May be different between on your computer)
pip install -r requirements.txt
```

## Step 4

Complete the coding exercises:

- `q1_arrays.py`
- `q2_debugging.py`
- `q3_data_science.py`

You may want to create a [branch](https://stackoverflow.com/questions/23192713/git-creating-a-branch-from-the-master) and do your edits in those files

## Step 5

Once you're done coding, check that the tests works with:

```zsh
pytest
```

## Step 6

Once you're done, open a pull request (PR) with all these changes and tag `@probro27` and `@rodrigotiscareno` for a review.
If you're waiting on a review, please take a look through the MSXIV work (https://github.com/uw-midsun/strategy) and come up with questions about what we've designed, or how we implemented certain things
