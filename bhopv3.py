import pymem
import pymem.process
import win32api

import offsets 
import clientdll

#dwfj = offsets.client_dll.dwForceJump
#dwlpp = offsets.client_dll.dwLocalPlayerPawn
#mf = clientdll.C_BaseEntity.m_fFlags


class BunnyHop:
    def __init__(self, dwForceJump, dwLocalPlayer, m_fFlags):
        self.dwForceJump = dwForceJump
        self.dwLocalPlayer = dwLocalPlayer
        self.m_fFlags = m_fFlags

    def run(self, process, module_name):
        mem = pymem.Pymem(process) # начинаем юзать процесс
        client = pymem.process.module_from_name(mem.process_handle, module_name).lpBaseOfDll
        while True:
            if win32api.GetAsyncKeyState(32) != 0:
                mem.write_int(client + self.dwForceJump, 4 if self.flags(client, mem) else 5)

    def flags(self, client, mem):
        localplayer = mem.read_int(client + self.dwLocalPlayer)
        flags_num = mem.read_int(localplayer + self.m_fFlags)
        return True if flags_num == 256 else False

#dwForceJump = 0x17226E0
#dwLocalPlayerPawn = 0x1729348
#dwLocalPlayerController = 0x19038F8
#m_fFlags = 0x3D4

bh = BunnyHop(offsets.client_dll.dwForceJump,offsets.client_dll.dwLocalPlayerPawn,clientdll.C_BaseEntity.m_fFlags)
bh.run("cs2.exe", "client.dll")
