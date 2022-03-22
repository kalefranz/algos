"""

"""
from collections import deque
from typing import *


class SnapshotArray:

    def __init__(self, length: int):
        pass

    def set(self, index: int, val: int) -> None:
        pass


null = None
CASES = (
    (
        ["SnapshotArray","set","snap","set","get"],
        [[3],[0,5],[],[0,6],[0,0]],
        [null,null,0,null,5],
    ),
    (
        # [272, 272, 272]
        ['SnapshotArray','snap','get','get','get','snap','snap','set','snap','set','set','get','set','set','snap','get','snap','get','get','get','snap','set','snap','get','set','snap','snap','get','get','snap','set','set','snap','set','get','snap','set','get','get','snap','snap','set','set','get','set','get','snap','snap','get','set','snap','set','set','get','snap','set','get','snap','set','set','get','get','snap','snap','snap','snap','snap','get','get','get','snap','set','get','get','set','get','set','set','snap','set','snap','set','set','set','get','get','get','set','set','snap','get','get','snap','set','get','get','snap','snap','set','snap','set','snap','get','get','snap','snap','get','get','get','set','set','set','snap','snap','set','get','get','set','get','set','snap','get','set','get','get','snap','get','set','set','get','set','set','set','get','get','get','get','get','get','snap','snap','set','set','snap','set','snap','snap','snap','snap','set','get','set','get','get','snap','snap','get','get','snap','set','set','set','get','snap','set','snap','set','set','snap','snap','get','snap','snap','set','set','snap','set','get','set','get','get','snap','snap','get','get','set','snap','snap','set','get','get','set','snap','get','get','set','snap','snap','snap','get','snap','set','snap','get','set','snap','snap','snap','set','snap','get','get','get','set','set','set','get','snap','snap','get','snap','get','snap','snap','set','set','snap','snap','snap','get','get','snap','snap','set','snap','snap','set','snap','snap','snap','set','get','set','get','snap','get','snap','snap','snap','snap','snap','snap','get','get','snap','snap','snap','snap','get','get','snap','get','get','get','snap','set','get','set','get','set','get','get'],
        [[100],[],[50,0],[35,0],[78,0],[],[],[74,179820995],[],[51,591818187],[75,884797082],[3,0],[29,923200623],[51,276890797],[],[94,2],[],[47,1],[40,4],[93,1],[],[66,539693765],[],[62,4],[45,464332702],[],[],[10,8],[15,5],[],[37,615208237],[9,248887329],[],[18,49542080],[62,7],[],[76,33929822],[40,2],[66,11],[],[],[91,643494983],[43,33324704],[22,7],[55,338405759],[58,10],[],[],[82,0],[83,714187040],[],[85,17453914],[0,502844009],[12,2],[],[29,281035593],[66,3],[],[20,687289044],[85,266123117],[70,1],[27,3],[],[],[],[],[],[22,3],[83,9],[76,11],[],[60,284773089],[18,0],[82,0],[85,766603386],[71,11],[53,612338013],[45,472336403],[],[71,901350385],[],[16,191371378],[40,55688771],[24,805321444],[2,23],[8,23],[96,18],[89,311550974],[16,590038876],[],[98,19],[66,21],[],[98,439498831],[15,2],[87,2],[],[],[84,244017095],[],[75,470026554],[],[12,31],[75,24],[],[],[48,1],[52,5],[15,13],[18,182195167],[0,358416754],[99,597414548],[],[],[26,300124271],[0,8],[70,23],[98,885773728],[11,0],[38,884438668],[],[19,3],[17,55016891],[99,6],[11,34],[],[97,4],[34,362145390],[22,200719334],[47,34],[12,874492133],[41,567691477],[51,990048311],[24,30],[56,35],[39,37],[58,11],[4,6],[24,18],[],[],[60,788108772],[56,990758846],[],[90,114556686],[],[],[],[],[42,380189426],[7,15],[90,133844371],[14,34],[77,31],[],[],[56,40],[29,23],[],[1,708871437],[44,262629344],[54,717214218],[80,18],[],[88,301669669],[],[33,701937397],[86,229863649],[],[],[74,23],[],[],[72,70257309],[6,749455331],[],[5,173212713],[21,15],[75,887011459],[82,11],[43,35],[],[],[18,28],[30,34],[55,47234033],[],[],[10,839630129],[60,9],[23,9],[54,161322048],[],[13,37],[57,3],[0,993977492],[],[],[],[10,31],[],[73,535927553],[],[0,20],[45,924316559],[],[],[],[96,375322759],[],[11,2],[95,19],[52,11],[93,693747822],[96,88182172],[2,902668813],[68,58],[],[],[12,48],[],[61,12],[],[],[89,908201805],[2,378523443],[],[],[],[92,77],[62,71],[],[],[10,112582852],[],[],[51,505946865],[],[],[],[92,704200533],[14,76],[33,330844936],[74,9],[],[57,55],[],[],[],[],[],[],[75,10],[96,76],[],[],[],[],[0,94],[47,61],[],[27,72],[33,25],[31,57],[],[35,758847353],[9,51],[89,68987168],[8,11],[7,595528447],[22,60],[30,37]],
        [null,0,0,0,0,1,2,null,3,null,null,0,null,null,4,0,5,0,0,0,6,null,7,0,null,8,9,0,0,10,null,null,11,null,0,12,null,0,539693765,13,14,null,null,0,null,0,15,16,0,null,17,null,null,0,18,null,0,19,null,null,0,0,20,21,22,23,24,0,0,0,25,null,0,0,null,0,null,null,26,null,27,null,null,null,0,0,0,null,null,28,0,539693765,29,null,0,0,30,31,null,32,null,33,0,884797082,34,35,0,0,0,null,null,null,36,37,null,0,0,null,0,null,38,0,null,0,0,39,0,null,null,0,null,null,null,805321444,0,0,0,0,0,40,41,null,null,42,null,43,44,45,46,null,0,null,0,0,47,48,0,281035593,49,null,null,null,0,50,null,51,null,null,52,53,179820995,54,55,null,null,56,null,0,null,0,33324704,57,58,49542080,0,null,59,60,null,0,0,null,61,0,0,null,62,63,64,0,65,null,66,502844009,null,67,68,69,null,70,0,0,0,null,null,null,0,71,72,874492133,73,0,74,75,null,null,76,77,78,0,0,79,80,null,81,82,null,83,84,85,null,0,null,179820995,86,0,87,88,89,90,91,92,884797082,88182172,93,94,95,96,993977492,0,97,0,0,0,98,null,248887329,null,0,null,200719334,0],
    ),
)
def test(*test_nums):
    cases = test_nums and [CASES[num] for num in test_nums] or CASES

    failed = 0
    for q, case in enumerate(cases):
        for qq, (func, args, expected) in enumerate(zip(*case)):
            if qq == 0:
                instance = globals()[func](*args)
                instance_init = f"{func}{tuple(args)}"
                continue
            else:
                result = getattr(instance, func)(*args)
                if result == expected:
                    # print(f"{q}: passed")
                    pass
                else:
                    print(f"{q}/{qq}: FAILED  {instance_init}.{func}{tuple(args)}")
                    print(f"  {expected} != {result}")
                    failed += 1
                    break
    if failed:
        print(f"FAILED: {failed}")
    else:
        print(f"SUCCESS: TESTS PASSED == {len(cases)}")
test()
