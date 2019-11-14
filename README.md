# wpc-unofficial.org
This reprository is the clone of ipho-unofficial.org.

The website is static, as it is hosted solely on Github pages. The pages are generated through Python scripts using database files located at src/database/.

You can build the project by running main.py from src folder. This extracts all necessary files to parent folder of src. Building src recreates the whole codebase (except CNAME and README.md files), therefore you should only make your changes in src.

Project is built with Python 2.7, but code is Python 3 compatible as well. Changing the version results in different line endings in some files.

### Known issues etc
* Years with missing informations: 2010, 2007, 2001 - 1992.
* Inclusion of competition logos into timeline_year_index.
* I'm not sure if I should make individual pages as imo-official.org does.
