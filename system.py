import cpu
import memory
import video


class System():

    def __init__(self):
        self._cpu = cpu.Cpu()
        self._memory_controller = memory.MemoryController()
        self._video_controller = video.VideoController()

    def power_on(self):
        print("System.power_on()")
        self._cpu.power_on()
        self._memory_controller.power_on()
        self._video_controller.power_on()
