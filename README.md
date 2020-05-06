# fragalysis-user-upload
A framework for members of the public to upload their own data to the fragalysis platform

### Rules of file upload
1. For each target a new zip file containing all structures that you want to view together must be uploaded
2. The zip file must be named [target].zip - this is the name that the target will have on the fragalysis platform
3. Each file within the zip file must be of an identical protein structure with the same number of subunits.
4. Each pdb file must have the '.pdb. suffix
5. Each pdb flile must only have 'HET' records for only the ligands of interest
6. You must enter a user upload key so that we have a record of who has uploaded what 
7. Once the data is uploaded it is free for anyone to see and use.

### How to set up
1. Create a virtual environment (python 3.7) with django installed
2. Clone this repository and cd into simpleform
3. run 'python manage.py runserver'
4. copy the url shown into your browser
5. upload your required zip files into the site
6. install the fragalysis-api 
7. amend the paths in 'transfer-data.py' to suit you
8. run transfer-data.py to push the files through the fragalysis api
