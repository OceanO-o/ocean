def common(*args, **kw):
    a = args
    def _common(func):
        def _deco(*args, **kwargs):
            print 'args:', args, a
            return func(*args, **kwargs)
        return _deco
    return _common

@common('c')
def test(p):
    print p


test
test(1)
