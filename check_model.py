import h5py

with h5py.File('model_ann.h5', 'r') as f:
    config = f.attrs.get('model_config')
    print(config)