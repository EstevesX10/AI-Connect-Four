<div align="center">

# AI | Connect-4
</div>

<p align="center" width="100%">
    <img src="./Connect 4/Assets/ConnectFour_README_Wallpaper.jpg" width="70%" height="70%" />
</p>

## Project Overview
---
`Connect Four` is a **two-player strategy game** similar to tic-tac-toe. It is played using 42 tokens (21 red & 21 black) inside a grid of **7 columns by 6 rows** where both players take **turns**

A `player's move` consists of dropping one of his tokens into a column of his choice where it falls until it hits the bottom or the top token in that column. In addition, if the chosen column is **already full** then the player must choose another one.

A `player wins` by creating an arrangement in which at least **four of his tokens** are aligned in a **row**, **column** or **diagonal** (**ascending or descending**). Therefore if the **board is full with tokens** whilst not having formed any kind of arrangement, then the match results in a **Tie** between both players.

## Project Development (Dependencies & Execution)
As a request from our professors this project was developed using a `Notebook`. Therefore if you're looking forward to test it out yourself, keep in mind to either use a **[Anaconda Distribution](https://www.anaconda.com/)** or a 3rd party software that helps you inspect and execute it.

### Dependencies

In order to install the necessary **libraries** to execute this `Project` you can either execute the following command in your `environment's terminal`:

    pip install -r requirements.txt

Or use it inside a `jupyter notebook's code cell`:

    !pip install -r requirements.txt

Another approach would be to `Create a New Anaconda Environment` with all the dependencies already installed. To do so, type:

    conda env create -f Connect_4.yml

### Execution
Since the Project was developed using a `Jupyter Notebook` you will need to type the following **command** in order to inspect it:

    jupyter notebook 

You can even access it via `Jupyter Lab` with:

    jupyter lab

Once the local server starts simply access it and navigate through your `Machine's Directories` until you find the folder where the **Notebook** is being held at.