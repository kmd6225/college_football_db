This repository contains database code used to create and maintain a College Football Database. There are three planned components:

  1). Python Functions used to scrape college football reference during ETL.
  2). SQL Procedures used to load the data scraped via the python functions into fact and dimension tables. Corresponding ddl/dml also included.
  3). A python database application (GUI) for easy querying of the data

The initial focus of the Database will be on Big Ten teams but may expand to other conferences.

The repo is organilzed into three environments: Main, Stage, and Dev. All feature branches are off of DEV and will be merged via Pull Requests.
