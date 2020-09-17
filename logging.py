import logging
import time
import traceback

logging.basicConfig(filename='myapp.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def func():
    for i in range(10):
        print(i)
    time.sleep(2)

if __name__ == "__main__":
    logging.info('Started')
    logging.info('Execute func')
    func()
    logging.info('Run func successful')

    logging.info('Testing error handling')

    try:
        1/0
    except:
        logging.error('Something is wrong: {}'.format(traceback.format_exc()))


    logging.info('Demonstration error handling')
    alist = [1,2,0,5,7,5,0]
    success = 0
    fail = 0
    for i, item in enumerate(alist):
        try:
            1/item
            logging.info('Processing no: {}, value: {} successful'.format(i,item))
            success +=1
        except:
            logging.error('Error created when processing no: {}, value: {}, error: {}, skip'.format(i, item, traceback.format_exc()))
    logging.info('{} success, {} fail'.format(success, fail))
    logging.info("%d success, %d fail"%(success, fail))

    logging.info('Finished')

    # more examples:
    logging.debug('debug message')
    logging.info('info message')
    logging.warning('warn message')
    logging.error('error message')
    logging.critical('critical message')