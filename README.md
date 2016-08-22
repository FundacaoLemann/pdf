# Easy PDF

This module intends to provide an easy way of distributing data through pdf reports. It is specially usefull when you need to distribute information that will be discussed offline and outside the boundaries of your institution.

To start we think that PDF reports will be composed of charts and tables. 

## Setup

1. Add the template files into the folder `templates/{report_code}`
2. Add the definitions into `report_definitions/{report_code}/config.json`
3. run `python /home/wesleybatista/github/pdf/cli.py generate {report_code} {date}`

> The **date** argument must be in the format **YYYYMMDD**
