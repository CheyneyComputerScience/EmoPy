from EmoPy.src.fermodel import FERModel
from pkg_resources import resource_filename

def toCSVrow(filename,emotionLevels):
    # list comprehension modified from Method #3 of
    # https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
    listToStr = ','.join([str(elem) for elem in emotionLevels])
    return filename + "," + listToStr + "\n"


#target_emotions = ['calm', 'anger', 'happiness']
target_emotions = FERModel.POSSIBLE_EMOTIONS
model = FERModel(target_emotions, verbose=True)

faces = open("LIP_face_files.txt",'r')

predictionFile = open("FERmodel_LIP_predictions.csv",'w')

predictionFile.write(toCSVrow("filename",model.emotion_map.keys()))
# Read the first file
for file in faces.readlines():
#file = faces.readline()
#if True:
    fileNamePrefix = file.split('.')[0]
    
    fPath = "LIP_data/" + fileNamePrefix + ".jpg"
    print('Predicting on',fPath)
    prediction = model.predict(resource_filename('EmoPy.examples',fPath))
    predictionFile.write(toCSVrow(fPath,prediction[0]))


predictionFile.close()
