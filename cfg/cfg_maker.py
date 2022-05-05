from staticfg import CFGBuilder

cfg = CFGBuilder().build_from_file('ifelse.py', './ifelse.py')
cfg.build_visual('ifelse', 'png')

cfg = CFGBuilder().build_from_file('while.py', './while.py')
cfg.build_visual('while', 'png')