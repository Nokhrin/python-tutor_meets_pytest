import pytest

import problems.dictionaries.accents_dictionary as accents


input_example = [
    (
        4,
        ['cAnnot', 'cannOt', 'fOund', 'pAge'],
        'thE pAge cAnnot be found',
    ),
]


@pytest.mark.smoke
def test_accents_dictionary():
    """checks if number of mistakes found is correct"""
    test_input = [
        4,
        ['cAnnot', 'cannaccentsOt', 'fOund', 'pAge'],
        'thE pAge cAnnot be found'
    ]
    expected_result = 2
    actual_result = accents.check_accents(test_input[0], test_input[1], test_input[2])
    assert expected_result == actual_result

"""
4
cAnnot
cannOt
fOund
pAge
The PAGE cannot be found



4

1
M
M



0

2
Xu
xU
NJ xu xU xu



3

5
gSn
gsN
qY
rkZ
rKz
qy dr DH y Y qy rKz



5

5
nPa
Oc
oC
pT
zjU
Qp Gt oC oG l oc oc



3

5
aZqz
Azqz
lyAi
lYai
zN
xfm Zn frs lyai azqz



5

10
chN
lXp
Lxp
lxP
qXe
Qxe
qxE
uDb
udB
vezV
chn jkn bz j UDb Qxe udb qxE szk Lxp udb chn qXe cx



10

10
De
iKq
ikQ
lL
Mea
meA
uDb
X
zA
Za
IKq H mea qc ln Udb udb lL jr pE X ul Yc ikQ dE dE



10

"""