import memory
import video


class System():

    def __init__(self):
        self.__memory_controller = memory.MemoryController()
        self.__video_controller = video.VideoController()

    def power_on(self):
        print("System.power_on()")
        self.__memory_controller.power_on()
        self.__video_controller.power_on()
