# wpc-unofficial.org
This reprository is the clone of ipho-unofficial.org.

The website is static, as it is hosted solely on Github pages. The pages are generated through Python scripts using database files located at src/database/.

You can build the project by running main.py from src folder. This extracts all necessary files to parent folder of src. Building src recreates the whole codebase (except CNAME and README.md files), therefore you should only make your changes in src.

Project is built with Python 2.7, but code is Python 3 compatible as well. Changing the version results in different line endings in some files.

### Known issues etc
* The name of one member of Canadian team in 1992 is missing.
* So are details on competition of the following years: 2010, 2007, 2001 - 1992.
* I want to include the logos and instruction booklets of each competition in the website but I haven't contacted WPF abou this yet.
* I'm not sure if I should make individual pages as imo-official.org does.