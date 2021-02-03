import main
import configparser
import os
import var


def read_ini():
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = configparser.ConfigParser()
    config.sections()
    config.read(os.path.join(path, var.INI_FILE))
    config.sections()
    var.training_word = config['DATA']['training_word']
    var.total_missed_char = int(config['DATA']['total_missed_char'])
    var.total_typed_char = int(config['DATA']['total_typed_char'])
    var.total_minutes = float(config['DATA']['total_minutes'])


def write_ini():
    path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
    config = configparser.ConfigParser()
    config['DATA'] = {'training_word': str(var.training_word),
                      'total_missed_char': str(var.total_missed_char),
                      'total_typed_char': str(var.total_typed_char),
                      'total_minutes': str(var.total_minutes)}
    with open(os.path.join(path, var.INI_FILE), 'w') as configfile:
        config.write(configfile)
