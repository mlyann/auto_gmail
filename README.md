# In-office Email Script


## Use your own API Key:
API_KEY = "SG.I2........"
.env file to keep key secure


##Install required libraries
pip install "libraries"

##Run with crontab
Cron config:
0 18 * * 0-4 PATH=/usr/local/bin:/usr/bin:/bin /usr/bin/python3 absolute/path/in-office-email-script >> /absolute/path/for/logfile.log 2>&1

#Email will send at 6pm sun-thurs

pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Authors and acknowledgment
Minglai Yang

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
