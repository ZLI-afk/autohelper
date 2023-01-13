import os
from autohelper_impl import run, check_input


def main():
    cwd = os.getcwd()
    check_input()
    param_relax = os.path.join(cwd, 'param_relax.json')
    param_prop = os.path.join(cwd, 'param_prop.json')
    poscar_bcc = os.path.join(cwd, 'POSCAR.bcc')
    poscar_fcc = os.path.join(cwd, 'POSCAR.fcc')
    poscar_hcp = os.path.join(cwd, 'POSCAR.hcp')
    main_path = os.path.join(cwd, 'autotests')
    strategy_list_path = os.path.join(main_path, 'strategy_list')
    model_list_path = os.path.join(main_path, 'model_list')

    run(param_relax, param_prop,
        poscar_bcc, poscar_fcc, poscar_hcp,
        strategy_list_path, model_list_path)


if __name__ == "__main__":
    main()
