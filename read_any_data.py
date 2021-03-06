def read_any_data(filename, offset, count_read, init_flag):
    """ read in raw data from binary, matlab, or hdf5 file

    :param filename: name of file
    :param offset: offset for reading
    :param count_read: determines how many data points to read
    :param init_flag: init_flag == 1 simply determines fs and file size
    :returns: fs(sampling frequency) and file_size (in bytes) if init_flag == 1
    :returns: ECG and PP data (single np.array) if init_flag == 0
    """
    from read_binary import read_binary
    from read_mat import read_mat
    from read_hdf5 import read_hdf5
    import logging

    if (filename.endswith('.bin')):
        logging.info('Found the file type to be Binary!')
        data = read_binary(filename, offset, count_read, init_flag)
    else:
        try:
            data = read_mat(filename, offset, count_read, init_flag)
            logging.info('Found the file type to be Matlab!')
        except NotImplementedError:
            data = read_hdf5(filename, offset, count_read, init_flag)
            logging.info('Found the file type to be HDF5!')
    return(data)
