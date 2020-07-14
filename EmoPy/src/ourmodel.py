from keras.models import load_model
import cv2
from scipy import misc
import imageio
import numpy as np
import json
from pkg_resources import resource_filename


from EmoPy.src.backend_helper import _get_available_gpus
# from https://github.com/keras-team/keras/issues/13684#issuecomment-595054461
import keras.backend.tensorflow_backend as tfback
tfback._get_available_gpus = _get_available_gpus



class OURModel:
    """
    Pretrained deep learning model for facial expression recognition.

    :param target_emotions: set of target emotions to classify
    :param verbose: if true, will print out extra process information

    **Example**::

        from fermodel import FERModel

        target_emotions = ['happiness', 'disgust', 'surprise']
        model = FERModel(target_emotions, verbose=True)

    """

    POSSIBLE_EMOTIONS = ['anger', 'fear', 'calm', 'sadness', 'happiness', 'surprise', 'disgust']

    def __init__(self, target_emotions, verbose=False):
        self.target_emotions = target_emotions
        self.emotion_index_map = {
            'anger': 0,
            'disgust': 1,
            'fear': 2,
            'happiness': 3,
            'sadness': 4,
            'surprise': 5,
            'calm': 6
        }
        self._check_emotion_set_is_supported()
        self.verbose = verbose
        self.target_dimensions = (64, 64)
        self.channels = 1
        self._initialize_model()

    def _initialize_model(self):
        print('Initializing OUR model parameters')
        model_file = 'output/conv2d_fullModel.hdf5'
        emotion_map_file = 'examples/output/conv2d_emotion_map.json'
        emotion_map = json.loads(open(resource_filename('EmoPy', emotion_map_file)).read())
        print("model_file =",model_file)
        self.model = load_model(model_file)
        self.emotion_map = emotion_map

    def predict(self, image_file):
        """
        Predicts discrete emotion for given image.

        :param images: image file (jpg or png format)
        """
        image = imageio.imread(image_file)
        return self.predict_from_ndarray(image)

    def predict_from_ndarray(self, image_array):
        """
        Predicts discrete emotion for given image.

        :param image_array: a n dimensional array representing an image
        """
        gray_image = image_array
        if len(image_array.shape) > 2:
            gray_image = cv2.cvtColor(image_array, code=cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray_image, self.target_dimensions, interpolation=cv2.INTER_LINEAR)
        final_image = np.array([np.array([resized_image]).reshape(list(self.target_dimensions)+[self.channels])])
        prediction = self.model.predict(final_image)
        # Return the dominant expression
        dominant_expression = self._print_prediction(prediction[0])
        return prediction

    def _check_emotion_set_is_supported(self):
        """
        Validates set of user-supplied target emotions.
        """
        supported_emotion_subsets = [
            set(['calm', 'anger', 'happiness', 'surprise', 'disgust', 'fear', 'sadness']),
            set(['anger', 'fear', 'surprise', 'calm']),
            set(['happiness', 'disgust', 'surprise']),
            set(['anger', 'fear', 'surprise']),
            set(['anger', 'fear', 'calm']),
            set(['anger', 'happiness', 'calm']),
            set(['anger', 'fear', 'disgust']),
            set(['calm', 'disgust', 'surprise']),
            set(['sadness', 'disgust', 'surprise']),
            set(['anger', 'happiness'])
        ]
        if not set(self.target_emotions) in supported_emotion_subsets:
            error_string = 'Target emotions must be a supported subset. '
            error_string += 'Choose from one of the following emotion subset: \n'
            possible_subset_string = ''
            for emotion_set in supported_emotion_subsets:
                possible_subset_string += ', '.join(emotion_set)
                possible_subset_string += '\n'
            error_string += possible_subset_string
            raise ValueError(error_string)

    def _choose_model_from_target_emotions(self):
        """
        Initializes pre-trained deep learning model for the set of target emotions supplied by user.
        """
        model_indices = [self.emotion_index_map[emotion] for emotion in self.target_emotions]
        sorted_indices = [str(idx) for idx in sorted(model_indices)]
        model_suffix = ''.join(sorted_indices)
        #Modify the path to choose the model file and the emotion map that you want to use
        if(model_suffix == '0123456'):
            model_file = 'models/conv_model_%s.h5' % model_suffix
        else:
            model_file = 'models/conv_model_%s.hdf5' % model_suffix
        emotion_map_file = 'models/conv_emotion_map_%s.json' % model_suffix
        emotion_map = json.loads(open(resource_filename('EmoPy', emotion_map_file)).read())
        print("model_file =",model_file)
        return load_model(resource_filename('EmoPy', model_file)), emotion_map

    def _print_prediction(self, prediction):
        normalized_prediction = [x/sum(prediction) for x in prediction]
        for emotion in self.emotion_map.keys():
            print('%s: %.1f%%' % (emotion, normalized_prediction[self.emotion_map[emotion]]*100))
        dominant_emotion_index = np.argmax(prediction)
        for emotion in self.emotion_map.keys():
            if dominant_emotion_index == self.emotion_map[emotion]:
                dominant_emotion = emotion
                break
        # print('Dominant emotion: %s' % dominant_emotion)
        # print()
        return dominant_emotion
