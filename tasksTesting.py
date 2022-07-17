import pytest
from tasks import task4, task2, task3, task5And6
import pandas as pd


@pytest.mark.parametrize("filename,docid,userid", [(None,'100806162735-00000000115598650cb8b514246272b5','')])
def test2a(filename,docid,userid):
    result = task2.task2a(filename).VeiwCountry(docid)
    if docid in result['subject_doc_id']:
        result = True
    else:
        result = False
    assert result == True


@pytest.mark.parametrize("filename,docid,userid", [(None, '100806162735-00000000115598650cb8b514246272b5', '')])
def test2b(filename,docid,userid):
    result = task2.task2b(filename).VeiwContient(docid)
    if docid in result['subject_doc_id']:
        result = True
    else:
        result = False
    assert result == True
@pytest.mark.parametrize("filename,docid,userid", [(None,'100806162735-00000000115598650cb8b514246272b5','')])
def test3b(filename,docid,userid):
    result = task3.task3b(filename).VeiwBrowserName()
    if "The Most Used Browser is :Mozilla" == result:
        result = True
    else:
        result = False
    assert result == True
@pytest.mark.parametrize("filename,docid,userid", [(None,'100806162735-00000000115598650cb8b514246272b5','')])
def test4(filename,docid,userid):
    result = task4.task4d(filename).avid_readers()
    if result['(4) Readers who have spent most time reading']:
        result = True
    else:
        result = False
    assert result == True
@pytest.mark.parametrize("filename,docid,userid", [(None,'100806162735-00000000115598650cb8b514246272b5','')])
def test5d(filename,docid,userid):
    result = task5And6.task5(filename).AlsoLikes(docid,userid)
    if (docid not in result['Users Also Read(5d)']):
        result = True
    else:
        result = False
    assert result == True
