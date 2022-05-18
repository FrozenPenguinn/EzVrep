from Core import vrep
from Core.model import Model


class Client():
    @staticmethod
    def close_all():
        vrep.simxFinish(-1)  # close all connections
        return

    def __init__(self, ip = '127.0.0.1', port = 19999):
        self.ID = vrep.simxStart(ip, port, True, True, 5000, 5)
        if self.ID == -1:
            raise Exception('V-REP API server not found, please launch simualtion first')
        print("hello Vrep!")

    def bind(self, object_name):
        handle = get_handle(self.ID, object_name)
        return handle


def get_handle(client_id, object_name):
    error_code, handle = vrep.simxGetObjectHandle(client_id, object_name, vrep.simx_opmode_oneshot_wait)
    if error_code != 0:
        raise Exception('Object %s not found' % object_name)
    return handle
