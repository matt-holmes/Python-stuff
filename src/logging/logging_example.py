import logging
logging.basicConfig(level=logging.DEBUG, filename='test.log')

class LoggingExample:
    def run_logging(self):
        logging_types = ['debug', 'info', 'warn', 'error']
        for i in range(len(logging_types)):
            print(logging_types[i])
            if(logging_types[i] is 'debug'):
                logging.debug("test logging {0}".format(logging_types[i]))
            elif(logging_types[i] is 'info'):
                logging.info("test logging {0}".format(logging_types[i]))
            elif(logging_types[i] is 'warn'):
                logging.warn("test logging {0}".format(logging_types[i]))
            elif(logging_types[i] is 'error'):
                logging.error("test logging {0}".format(logging_types[i]))

if __name__ == '__main__':
    le = LoggingExample()
    le.run_logging()
