import six.moves.cPickle as pickle
import gzip
import os
import numpy as np
# import scipy.misc
from PIL import Image


def load_data(dataset):
    ''' Loads the dataset

    :type dataset: string
    :param dataset: the path to the dataset (here MNIST)

    copied from http://deeplearning.net/ and revised by hchoi
    '''

    # Download the MNIST dataset if it is not present
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory.
        new_path = os.path.join(
            os.path.split(__file__)[0],
            dataset
        )
        if os.path.isfile(new_path) or data_file == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        from six.moves import urllib
        origin = (
            'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        )
        print('Downloading data from %s' % origin)
        urllib.request.urlretrieve(origin, dataset)

    print('... loading data')

    # Load the dataset
    with gzip.open(dataset, 'rb') as f:
        try:
            train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
        except:
            train_set, valid_set, test_set = pickle.load(f)
    # train_set, valid_set, test_set format: tuple(input, target)
    # input is a numpy.ndarray of 2 dimensions (a matrix)
    # where each row corresponds to an example. target is a
    # numpy.ndarray of 1 dimension (vector) that has the same length as
    # the number of rows in the input. It should give the target
    # to the example with the same index in the input.

    return train_set, valid_set, test_set


if __name__ == '__main__':
    train_set, val_set, test_set = load_data('mnist.pkl.gz')

    train_x, train_y = train_set
    val_x, val_y = val_set
    test_x, test_y = test_set

    print(train_x.shape)
    print(train_y.shape)

    for i in range(100):
        tmp_img = train_x[i].reshape((28, 28)) * 255.9
        samp_img = Image.fromarray(tmp_img.astype(np.uint8))
        samp_img.save('test' + str(i) + '.jpg')
        print(train_y[i])
    # Mean
    temp_img = np.zeros((28, 28))
    total_num = 0
    for i in train_x:
        tmp_img = i.reshape((28, 28)) * 255.9
        temp_img += tmp_img
        total_num += 1

    temp_img = temp_img / total_num

    mean_image = Image.fromarray(temp_img.astype(np.uint8))
    mean_image.save("Mean_vals.jpg")
    mean_img = train_x.mean(1)
    del mean_image

    # Variance
    temp2_img = np.zeros((28, 28))
    total_num = 0
    for i in train_x:
        tmp2_img = i.reshape((28, 28)) * 255.9
        temp2_img += (tmp2_img - temp_img) ** 2
        total_num += 1

    temp2_img /= total_num
    variance_image = Image.fromarray(temp2_img.astype(np.uint8))
    variance_image.save("Variance_vals.jpg")

    print(train_x)
    print(np.sum(train_x <= 0.1))
    print(np.sum(train_x >= 0.9))
    print(mean_img.shape)

    cov = np.cov(train_x.T)
    print(cov)
    print(cov.shape)
    # for eigen decomposition
    # check http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html
