import project


pa = project.password(1, 0, 0)


def test_tryInt():
    assert project.tryInt('1', '_') == 1


def test_yORn():
    assert project.yORn('y', '_') == True
    assert project.yORn('n', '_') == False


def test_createPass():
    assert len(project.createPass(pa)) == 1