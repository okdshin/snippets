import importlib
import fire

def im(module='detnas', model='DetNASSmallCOCO', kwargs='{}'):
    m = importlib.import_module(module)
    #m.DetNASSmallCOCO(**eval(kwargs))
    print(kwargs)
    kwargs = eval(kwargs)
    model = eval('m.'+model)(**kwargs)
    print(model)

import fire
fire.Fire(im)
