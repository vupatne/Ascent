
def prepare_modify_attr(input):
    return input.split('set')[1].lstrip().split('where')[0].replace(' ','').replace('=%s','')