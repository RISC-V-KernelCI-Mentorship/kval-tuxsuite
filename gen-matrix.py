#!/usr/bin/env python3

import yaml
import json

def get_targets() -> list:
  targets = []
  with open("riscv-targets.yaml", 'r') as stream:
      try:
          targets = yaml.safe_load(stream)
      except yaml.YAMLError as exc:
          print(exc)
  return targets

def gen_targets_conf(target, defconfig, toolchain) -> dict:
  target = target.copy()
  target['defconfig'] = defconfig
  target['toolchain'] = toolchain
  # Convert tests array to string
  target['tests'] = ' '.join(target['tests'])
  return target

def create_matrix() -> None:
    targets = get_targets()
    matrix_items = []
    
    for target in targets:
        for defconfig in target['defconfig']:
            for toolchain in target['toolchain']:
                matrix_items.append(gen_targets_conf(target, defconfig, toolchain))
      
    print(json.dumps(matrix_items, indent=2))

if __name__ == '__main__':
  create_matrix()