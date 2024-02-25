import pymem
import pymem.process
import keyboard

pm = pymem.Pymem("cs2.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

#offsetts#
import offsets, clientdll


dwForceJump = offsets.client_dll.dwForceJump
#dwlpp = offsets.client_dll.dwLocalPlayerPawn
m_fFlags = clientdll.C_BaseEntity.m_fFlags


#method#

def main(pm, client, player):
    force_jump = client + dwForceJump
    on_ground = pm.read_uint(player + m_fFlags)
    if player and on_ground == 257 or on_ground == 263:
        pm.write_int(force_jump, 6)

#starting#
        

if __name__ == '__main__':
    main()