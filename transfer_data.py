import os

for zipfile in os.listdir('simpleform/upload'):
    os.system('mv simpleform/upload/' + zipfile + ' ./fragalysis-api/data/xcimporter/input')
    os.system('unzip ./fragalysis-api/data/xcimporter/input/'+zipfile+' -d ./fragalysis-api/data/xcimporter/input/')

    
os.system('rm ./fragalysis-api/data/xcimporter/input/*.zip')


if os.path.exists('fragalysis-api/data/xcimporter/input/.ipynb_checkpoints'):
    print('deleting checkpoints')
    os.system('rm -r fragalysis-api/data/xcimporter/input/.ipynb_checkpoints')



for target in os.listdir('fragalysis-api/data/xcimporter/input'):
    if not target == 'README.md':
        print(target)
        os.system('python ./fragalysis-api/fragalysis_api/xcimporter/xcimporter.py -i ./fragalysis-api/data/xcimporter/input/' + target + ' -o ./fragalysis-api/data/xcimporter/output -t ' + target)