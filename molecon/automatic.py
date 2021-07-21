# base_address = 0x00100000

# success_address = 
# failure_address = 0x00101384
import angr
# import claripy

def main():
    p = angr.Project("challenge")
    simgr = p.factory.simulation_manager(p.factory.full_init_state())
    simgr.explore(find=0x00101344, avoid=0x00101354)

    return simgr.found[0].posix.dumps(0).strip(b'\0\n')


if __name__ == '__main__':
    print(main())
# for flag_length in range(13,26):
    

#     project = angr.Project('./challenge')

#     flag_chars = [claripy.BVS('ptm_%i' %i, 8) for i in range(flag_length)]
#     flag = claripy.Concat( *flag_chars + [claripy.BVV(b'\n')]) # so stdin works

#     state = project.factory.full_init_state(
#         args = ['./challenge'],
#         add_options = angr.options.unicorn,
#         stdin = flag
#     )

#     for k in flag_chars:
#         state.solver.add(k >= ord('!'))
#         state.solver.add(k <= ord('-'))

#     sim_manager = project.factory.simulation_manager(state)
#     sim_manager.explore(find = 0x00101344, avoid = 0x00101354)

#     if (len(sim_manager.found) > 0):
#         for found in sim_manager.found:
#             print(found.posix.dumps(0), flag_length)
#             break