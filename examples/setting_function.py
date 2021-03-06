#!/usr/bin/env python
# ------------------------------------------------------------------------------------------------------%
# Created by "Thieu Nguyen" at 21:02, 16/03/2020                                                        %
#                                                                                                       %
#       Email:      nguyenthieu2102@gmail.com                                                           %
#       Homepage:   https://www.researchgate.net/profile/Thieu_Nguyen6                                  %
#       Github:     https://github.com/thieunguyen5991                                                  %
#-------------------------------------------------------------------------------------------------------%

from opfunu.type_based.uni_modal import Functions
ff = Functions()
print_out = False
problem_size = 50

PF1 = {     # paras for function 1 (PF1)
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._brown__
}
PF2 = {
    "problem_size": problem_size,
    "domain_range": [-10, 10],
    "print_train": print_out,
    "objective_func": ff._chung_reynolds__
}
PF3 = {
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._dixon_price__
}
PF4 = {
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._powell_singular_2__
}
PF5 = {
    "problem_size": problem_size,
    "domain_range": [-30, 30],
    "print_train": print_out,
    "objective_func": ff._powell_result__
}
PF6 = {
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._rosenbrock__
}
PF7 = {
    "problem_size": problem_size,
    "domain_range": [-1.28, 1.28],
    "print_train": print_out,
    "objective_func": ff._rotate_ellipse__
}
PF8 = {
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._schwefel__
}
PF9 = {
    "problem_size": problem_size,
    "domain_range": [-1, 1],
    "print_train": print_out,
    "objective_func": ff._schwefel_1_2__
}

PF10 = {
    "problem_size": problem_size,
    "domain_range": [-10, 10],
    "print_train": print_out,
    "objective_func": ff._schwefel_2_20__
}

PF11 = {
    "problem_size": problem_size,
    "domain_range": [-100, 100],
    "print_train": print_out,
    "objective_func": ff._schwefel_2_21__
}

PF12 = {
    "problem_size": problem_size,
    "domain_range": [-10, 10],
    "print_train": print_out,
    "objective_func": ff._schwefel_2_22__
}

PF13 = {
    "problem_size": problem_size,
    "domain_range": [-5, 10],
    "print_train": print_out,
    "objective_func": ff._schwefel_2_23__
}

PF14 = {
    "problem_size": problem_size,
    "domain_range": [-500, 500],
    "print_train": print_out,
    "objective_func": ff._step__
}

PF15 = {
    "problem_size": problem_size,
    "domain_range": [-5.12, 5.12],
    "print_train": print_out,
    "objective_func": ff._step_2__
}

PF16 = {
    "problem_size": problem_size,
    "domain_range": [-32, 32],
    "print_train": print_out,
    "objective_func": ff._step_3__
}

PF17 = {
    "problem_size": problem_size,
    "domain_range": [-60, 60],
    "print_train": print_out,
    "objective_func": ff._stepint__
}

PF18 = {
    "problem_size": problem_size,
    "domain_range": [-50, 50],
    "print_train": print_out,
    "objective_func": ff._streched_v_sin_wave__
}

PF19 = {
    "problem_size": problem_size,
    "domain_range": [-50, 50],
    "print_train": print_out,
    "objective_func": ff._sum_squres__
}


func_paras = [PF1, PF2, PF3, PF4, PF5, PF6, PF7, PF8, PF9, PF10, PF11, PF12, PF13, PF14, PF15, PF16, PF17, PF18, PF19]
func_names = ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13","F14", "F15", "F16", "F17", "F18", "F19"]
