import carla


def main():
    try:
        client = carla.Client('localhost', 2000)
        print('clinet: ', client, 'connection alive')

    finally:
        print('destroying actors')

if __name__ == '__main__':

    main()
