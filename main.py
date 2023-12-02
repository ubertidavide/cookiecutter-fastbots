import argparse
import logging

from tasks.test_task import TestTask


def main():
    parser = argparse.ArgumentParser(
        prog='MyBot',
        description='Bot builded with the fastbots library.',
        epilog='Made with <3 using fastbots.')

    parser.add_argument('-tt', '--test_task', action='store_true')
    
    args = parser.parse_args()

    if args.test_task:
        logging.info('Launching Test Task')
        TestTask()()


if __name__ == '__main__':
    #main()
    TestTask()()