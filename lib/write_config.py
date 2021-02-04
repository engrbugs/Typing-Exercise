import configparser
import var


def read_ini():
    config = configparser.ConfigParser()
    config.sections()
    config.read(var.APP_PATH + f'\\{var.INI_FILE}')
    config.sections()
    var.training_word = config['DATA']['training_word']
    var.total_missed_char = int(config['DATA']['total_missed_char'])
    var.total_typed_char = int(config['DATA']['total_typed_char'])
    var.total_minutes = float(config['DATA']['total_minutes'])


def write_ini():
    config = configparser.ConfigParser()
    config['DATA'] = {'training_word': str(var.training_word),
                      'total_missed_char': str(var.total_missed_char),
                      'total_typed_char': str(var.total_typed_char),
                      'total_minutes': str(var.total_minutes)}
    with open(var.APP_PATH + f'\\{var.INI_FILE}', 'w') as configfile:
        config.write(configfile)
