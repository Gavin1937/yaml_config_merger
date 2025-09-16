from typing import Any
from copy import deepcopy

__all__ = ['merge_config']

def merge_config(parent_config:dict, child_config:dict, merge_depth:int=2, child_list_on_top:bool=False) -> dict:
    '''
    merge child_config to parent_config, returns merged config as new dict
    '''

    def _merge(parent:Any, child:Any) -> Any:
        if type(parent) != type(child):
            return child
        if type(parent) == dict:
            return {**parent, **child}
        elif type(parent) == list:
            if child_list_on_top:
                return [*child, *parent]
            else:
                return [*parent, *child]
        else: # child override parent for any other types
            return child

    def _traverse(parent:Any, child:Any, max_depth:int) -> Any:
        if max_depth <= 0:
            return _merge(parent, child)
        for ck,cv in child.items():
            if ck in parent:
                pv = parent[ck]
                if type(cv) == dict and type(pv) == dict:
                    parent[ck] = _traverse(pv, cv, max_depth-1)
                else:
                    parent[ck] = _merge(pv, cv)
            else:
                parent[ck] = cv
        return parent

    parent_cp = deepcopy(parent_config)
    # for ck,cv in child_config.items():
    #     if ck in parent_cp:
    #         pv = parent_cp[ck]
    #         if type(cv) == type(pv):
    #             parent_cp[ck] = _merge_same_types(pv, cv)
    #         else:
    #             parent_cp[ck] = cv
    #     else:
    #         parent_cp[ck] = cv

    # return parent_cp

    return _traverse(parent_cp, child_config, merge_depth)