# The Scripter
## Your SQL Scripter

- Are you bored to change the same scripts over and over?
- Do you spend un-necessary time looking for variables buried in the script?
- Would you like to minimise the damage human error could cause?

If you said yes to any of the above, keep reading as this simple app is just what you need.

## What does this WebApp do?

1. The app generates a form from pre-set variables found in one or more .SQL files.
2. You can then use the form to fill the script(s)
3. A .Zip file is generated with all your scripts, ready to be added to your maintenance document, or applied in the database.

## What does this WebApp do NOT?

1. The app will NOT run SQL queries 
2. The app does not guess your variables, uou must add a prefix on them.
3. 

## How to install

1. Download the zip and unpack it in your Linux box (or WSL environment)
2. get into the main folder `$ cd the-scripter`
3. run `$ sh deploy.sh`
> **Please note:** The app will install itself on first run, so give it a minute.
> Following runs will only check installation status, so they should be much quicker to get it up and running.

## Enable Debug

To run the code in debug mode:
1. Ensure to run the code once in normal mode (this will prepare the environment)
2. from the app root folder, run `$ . .venv/bin/activate` or `$ source .venv/bin/activate`
3. run `$ python3 wsgy.py`
4. Voilà! You are in debug mode!

## Warnings and other considerations

- Under the hood, the engine searches the text file(s) for words with a pre-determined prefix, and replace them with the respective info you inserted in the form. 
- **This app should be fully working, but it has rough edges, so review your scripts before apply them in a Production Database.**
- It should work with any text base files
- Use a prefix that is unique in your script, otherwise, it may mix with other content producing un-expected ressults and errors.
- all scripts files upladed are available in plain text, so they can be updated without need to recreate the record
- This app is NOT Windows friendly due the slash/backslash dealbraker, however if you really want it should not be hard to convert it or to make it OS agnostic. Feel free to fork it and let me know the outcome.

## Questions?
[Ask Away!](https://github.com/pnatel/the-scripter/discussions)


